import os
import logging
from dotenv import load_dotenv
from app import app

# Load environment variables
load_dotenv()

# Configure logging with more detail
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    """Main entry point for the application"""
    try:
        logger.info("Starting Flask application server...")
        
        # Use port 5000 as per flask_website guidelines
        port = int(os.environ.get('PORT', 5000))
        
        # Check for required environment variables
        openai_key = os.environ.get("OPENAI_API_KEY")
        if not openai_key:
            logger.warning("OPENAI_API_KEY not found in environment variables")
            logger.info("Application will start but AI features may be limited")
        
        # Configure production settings
        debug_mode = os.environ.get('FLASK_ENV') != 'production'
        if not debug_mode:
            logger.info("Running in production mode")
        
        # Start the Flask server
        logger.info(f"Starting Flask server on port {port}")
        app.run(
            host='0.0.0.0',
            port=port,
            debug=debug_mode,
            use_reloader=debug_mode,
            threaded=True  # Enable threading for better performance
        )
        
    except Exception as e:
        logger.critical(f"Failed to start server: {str(e)}")
        logger.critical(f"Exception details: {type(e).__name__}: {str(e)}")
        logger.critical("Please ensure port 5000 is available and not in use")
        raise SystemExit(1)

if __name__ == "__main__":
    main()
