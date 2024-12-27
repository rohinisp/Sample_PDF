import os
import logging
from flask import Flask, render_template, request, jsonify, g
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_caching import Cache
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging with more detail
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def create_app():
    logger.info("Creating Flask application...")
    
    # Create Flask app
    app = Flask(__name__)
    
    # Configure secret key
    app.secret_key = os.environ.get("FLASK_SECRET_KEY", "default-secret-key-for-pdf-extractor")
    logger.debug("Secret key configured")
    
    # Configure cache with enhanced settings for large datasets
    cache_config = {
        "CACHE_TYPE": "SimpleCache",
        "CACHE_DEFAULT_TIMEOUT": 7200,  # Extended cache timeout (2 hours)
        "CACHE_THRESHOLD": 2000,  # Increased maximum items
        "CACHE_KEY_PREFIX": "pdf_processor_"  # Prefix for better cache management
    }
    app.config.from_mapping(cache_config)
    cache = Cache(app)
    logger.debug(f"Cache initialized using {cache_config['CACHE_TYPE']}")
    
    # Configure rate limiter with enhanced settings
    limiter = Limiter(
        app=app,
        key_func=get_remote_address,
        default_limits=["1000 per day", "60 per minute"],
        storage_uri="memory://",
        strategy="fixed-window-elastic-expiry",  # More forgiving rate limit strategy
        headers_enabled=True,  # Enable rate limit headers
        swallow_errors=True,  # Continue on rate limit errors
        retry_after="delta-seconds"
    )
    logger.info("Rate limiter configured with enhanced settings")
    
    # Add rate limit headers to responses
    @app.after_request
    def add_rate_limit_headers(response):
        try:
            if hasattr(request, '_rate_limit_info'):
                response.headers.add(
                    'X-RateLimit-Limit',
                    str(request._rate_limit_info.limit)
                )
                response.headers.add(
                    'X-RateLimit-Remaining',
                    str(request._rate_limit_info.remaining)
                )
                response.headers.add(
                    'X-RateLimit-Reset',
                    str(request._rate_limit_info.reset)
                )
        except Exception as e:
            logger.warning(f"Rate limit header error: {str(e)}")
        return response
    
    logger.debug("Rate limit headers configured")
    
    # Configure max content length for file uploads (100MB)
    app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024
    logger.info("File upload size limit set to 100MB")
    
    # Configure production settings
    if os.environ.get('FLASK_ENV') == 'production':
        app.config.update(
            SESSION_COOKIE_SECURE=True,
            SESSION_COOKIE_HTTPONLY=True,
            SESSION_COOKIE_SAMESITE='Lax',
            PERMANENT_SESSION_LIFETIME=3600
        )
        logger.info("Production security settings configured")
    
    # Register error handlers
    @app.errorhandler(404)
    def not_found_error(error):
        if request.is_json:
            return jsonify({'error': 'Page not found'}), 404
        return render_template('error.html', error="Page not found"), 404

    @app.errorhandler(500)
    def internal_error(error):
        if request.is_json:
            return jsonify({'error': 'Internal server error'}), 500
        return render_template('error.html', error="Internal server error"), 500

    @app.errorhandler(429)
    def ratelimit_handler(error):
        if request.is_json:
            return jsonify({'error': 'Rate limit exceeded. Please try again later.'}), 429
        return render_template('error.html', error="Rate limit exceeded. Please try again later."), 429

    @app.errorhandler(413)
    def request_entity_too_large(error):
        if request.is_json:
            return jsonify({'error': 'File too large. Maximum size is 50MB'}), 413
        return render_template('error.html', error="File too large. Maximum size is 50MB"), 413
    
    logger.info("Flask application created successfully")
    return app, cache, limiter

# Create the application instance
app, cache, limiter = create_app()

# Import routes
from routes import register_routes
register_routes(app)

# Main application entry point handled by main.py
if __name__ == "__main__":
    logger.info("Starting application via app.py")
    # Use port 5000 as per flask_website guidelines
    app.run(host='0.0.0.0', port=5000, debug=True)
