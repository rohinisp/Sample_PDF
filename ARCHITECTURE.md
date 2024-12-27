# PDF Processing Service Architecture Documentation

## System Overview

This document provides a comprehensive overview of the PDF processing service architecture, detailing how components interact and process data through the system.

## Architecture Components

### 1. Entry Points and Request Handling
```
[Client] → [Flask Server (main.py, app.py)] → [Route Handlers (routes.py)]
                           ↓
                    [Request Processing]
```

#### Component Details:
- **main.py**: Application entry point
  - Configures logging
  - Loads environment variables
  - Handles server startup
  - Manages production/development modes

- **app.py**: Core application configuration
  - Flask app initialization
  - Cache configuration
  - Rate limiter setup
  - Error handlers
  - Security settings

- **routes.py**: API endpoint handlers
  - `/api/process-pdf`: Main PDF processing endpoint
  - `/api/process-multiple-sources`: Multi-source processing

### 2. PDF Processing Pipeline
```
[PDF Input] → [PDFExtractor] → [Text Extraction] → [Content Processing]
                   ↓               ↓                    ↓
              [Validation]    [Error Handling]    [Cache Storage]
```

#### Component Details:
- **PDFExtractor (pdf_extractor.py)**:
  ```python
  class PDFExtractor:
      # Main processing methods:
      process_document()        # Process local files
      extract_from_bytes()      # Process uploaded content
      semantic_search()         # Search within processed content
  ```
  - Handles PDF loading and validation
  - Extracts text content with layout preservation
  - Implements fallback extraction methods
  - Manages caching of processed content

### 3. LLM Processing Pipeline
```
[Extracted Text] → [LLMProcessor] → [Question Processing] → [Response Generation]
                        ↓               ↓                         ↓
                   [Cache Check]   [Batch Processing]    [Confidence Scoring]
```

#### Component Details:
- **LLMProcessor (llm_processor.py)**:
  ```python
  class LLMProcessor:
      # Core processing methods:
      process_questions()      # Handle multiple questions
      get_answer()            # Process single question
      get_relevant_context()  # Extract context for questions
  ```
  - Manages OpenAI API interactions
  - Implements question batching (10 questions/batch)
  - Handles caching of responses
  - Provides confidence scoring

### 4. Caching Architecture
```
[Request] → [Cache Check] → [Processing Pipeline] → [Cache Storage]
              ↓                                          ↓
         [Cache Hit]                              [Cache Update]
```

#### Cache Levels:
1. **Document Cache**:
   ```python
   cache.set(
       f"doc_content_{cache_key}",
       structured_content,
       timeout=3600  # 1 hour
   )
   ```

2. **Q&A Cache**:
   ```python
   cache.set(
       f"qa_{cache_key}",
       json.dumps(result),
       timeout=24*3600  # 24 hours
   )
   ```

### 5. Data Flow Process

1. **Input Processing**:
   ```
   [Client Request] → [Input Validation] → [Size Check] → [Format Verification]
   ```
   - Handles both URL and file uploads
   - Validates input format and size
   - Performs security checks

2. **Content Processing**:
   ```
   [PDF Content] → [Text Extraction] → [Content Structuring] → [Cache Storage]
   ```
   - Extracts text with layout preservation
   - Structures content by pages
   - Stores in cache for reuse

3. **Question Processing**:
   ```
   [Questions] → [Batch Formation] → [Context Selection] → [LLM Processing]
   ```
   - Groups questions in batches
   - Selects relevant context
   - Processes through LLM

4. **Response Generation**:
   ```
   [LLM Output] → [Confidence Scoring] → [Cache Update] → [Response Formatting]
   ```
   - Scores answer confidence
   - Updates cache if needed
   - Formats JSON response

## Resource Management

### 1. Memory Management
```python
# Streaming large files
with requests.get(url, stream=True) as response:
    for chunk in response.iter_content(chunk_size=1024*1024):
        size += len(chunk)
        buffer.write(chunk)
```

### 2. Processing Limits
- Maximum file size: 100MB
- Maximum text content: 1M chars
- Batch size: 10 questions
- Cache items: 2000 max

### 3. Rate Limiting
```python
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["1000 per day", "60 per minute"]
)
```

## Error Handling

### 1. Global Error Handlers
```python
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({'error': 'Page not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500
```

### 2. Process-Specific Error Handling
```python
try:
    content = page.extract_text(layout=True)
    if not content:
        # Try alternate extraction
        content = '\n'.join(
            text.get_text() 
            for text in page.extract_text_lines()
        )
except Exception as e:
    logger.error(f"Error extracting text: {str(e)}")
```

## Deployment Configuration

### 1. Development Mode
```python
app.run(
    host='0.0.0.0',
    port=5000,
    debug=True,
    use_reloader=True
)
```

### 2. Production Mode
```python
app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax',
    PERMANENT_SESSION_LIFETIME=3600
)
```

## Security Measures

1. **Input Validation**
   - File type verification
   - Size limits
   - Content validation

2. **Rate Limiting**
   - Per-IP limits
   - Global rate limits

3. **Error Handling**
   - Secure error messages
   - Logging without sensitive data

4. **Session Security**
   - Secure cookies
   - HTTPS enforcement
   - Session lifetime limits

## Monitoring and Logging

```python
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Performance monitoring
logger.info(f"PDF processed in {load_time:.2f}s ({num_pages/load_time:.1f} pages/s)")
```

## Future Scalability Considerations

1. **Horizontal Scaling**
   - Redis for distributed caching
   - Load balancing support
   - Stateless design

2. **Performance Optimization**
   - Async processing
   - Enhanced batching
   - Improved caching

3. **Feature Extensions**
   - Additional document formats
   - Enhanced text analysis
   - Custom model support
