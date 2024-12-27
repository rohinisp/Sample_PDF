# PDF Text Extractor API Documentation

## Environment Variables
```
OPENAI_API_KEY=your_openai_api_key_here
FLASK_SECRET_KEY=your_secure_secret_key_here
```

## API Endpoints

### 1. Process PDF
**Endpoint**: `/api/process-pdf`
**Method**: POST
**Description**: Unified endpoint that handles both URL and file uploads with optional question answering

#### A) Process PDF from URL
```bash
# Example curl command
curl -X POST http://localhost:5000/api/process-pdf \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://example.com/sample.pdf",
    "question": "What is the main topic?"
  }'
```

**Request Body**:
```json
{
    "url": "https://example.com/sample.pdf",
    "question": "What is the main topic?" // Optional
}
```

#### B) Process PDF from File Upload
```bash
# Example curl command
curl -X POST http://localhost:5000/api/process-pdf \
  -F "file=@/path/to/your/document.pdf" \
  -F "question=What is the main topic?"
```

**Request Format**: `multipart/form-data`
- `file`: PDF file
- `question`: Optional question string

#### Response Format
```json
{
    "text": "Extracted text content from PDF",
    "cache_key": "unique_cache_key_for_future_reference",
    "success": true,
    "answers": {
        "answer": "The main topic is artificial intelligence",
        "confidence": 0.95,
        "context": "The document discusses advances in artificial intelligence...",
        "reasoning": "Based on the first paragraph and recurring themes..."
    },
    "metadata": {
        "document": {
            "title": "Document Title",
            "page_count": 10,
            "processing_time": 1.5
        }
    }
}
```

### 2. Ask Questions About Processed PDF
**Endpoint**: `/api/ask`
**Method**: POST
**Description**: Ask questions about previously extracted text

```bash
# Example curl command
curl -X POST http://localhost:5000/api/ask \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Previously extracted text content",
    "question": "What are the key findings?"
  }'
```

**Request Body**:
```json
{
    "text": "Previously extracted text content",
    "question": "What are the key findings?"
}
```

**Response Format**:
```json
{
    "answer": "The key findings include...",
    "confidence": 0.92,
    "context": "Relevant section from the text...",
    "reasoning": "Analysis based on context..."
}
```

## Rate Limits
- 200 requests per day
- 20 requests per minute

## Error Responses

### 1. Bad Request (400)
```json
{
    "error": "No PDF URL or file provided"
}
```

### 2. Rate Limit Exceeded (429)
```json
{
    "error": "Rate limit exceeded. Please try again later."
}
```

### 3. Server Error (500)
```json
{
    "error": "Internal server error",
    "details": "Error description..."
}
```

## Testing the API

1. Start the server:
```bash
python main.py
```

2. Test URL processing:
```bash
curl -X POST http://localhost:5000/api/process-pdf \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://example.com/sample.pdf",
    "question": "What is this document about?"
  }'
```

3. Test file upload:
```bash
curl -X POST http://localhost:5000/api/process-pdf \
  -F "file=@/path/to/your/document.pdf" \
  -F "question=Summarize this document"
```

## Notes
- Maximum file size: 50MB
- Supported file format: PDF only
- All responses are in JSON format
- Times are in seconds
- Confidence scores are between 0 and 1
