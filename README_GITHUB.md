# AI-Powered Document Processing Service

## Overview
An advanced AI-powered document processing web service designed to intelligently extract, analyze, and transform unstructured document content into actionable insights. The service leverages cutting-edge natural language processing and machine learning technologies to provide robust, error-resilient document handling capabilities.

## Prerequisites
- Python 3.11 or higher
- OpenAI API key

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd <repository-name>
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the root directory with:
```
OPENAI_API_KEY=your_api_key_here
FLASK_SECRET_KEY=your_secret_key_here
```

## Running the Application

### Development Mode
```bash
python main.py
```
The application will be available at `http://localhost:5000`

### Production Mode
```bash
FLASK_ENV=production gunicorn --bind 0.0.0.0:8080 --workers 4 --threads 2 --timeout 60 app:app
```
The application will be available at `http://localhost:8080`

## Features
- PDF text extraction with advanced error handling
- Intelligent question answering using GPT-4
- Vector-based semantic search
- Support for both URL and file uploads
- Caching system for improved performance
- Rate limiting for API protection

## API Documentation
See [API_DOCUMENTATION.md](API_DOCUMENTATION.md) for detailed API documentation.

## Architecture
See [ARCHITECTURE.md](ARCHITECTURE.md) for detailed architecture documentation.

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
