# PDF Text Extractor - Beginner-Friendly Setup Guide 📚

Welcome to the PDF Text Extractor! This guide will help you set up and run the application, even if you're new to programming. Follow these steps carefully, and you'll have your PDF processor up and running in no time!

## What Does This Application Do? 🤔

This is a smart web application that can:
- Read PDF files (either uploaded or from URLs)
- Extract all the text from PDFs
- Answer questions about the PDF content using AI
- Remember previously processed PDFs to work faster next time

## Before You Start: Things You'll Need 📋

1. **A Computer** with:
   - Windows 10/11, Mac OS, or Linux
   - At least 4GB of RAM
   - Internet connection

2. **Python** (Don't worry, we'll help you install it!)
   - We'll guide you through installing Python 3.11

3. **OpenAI API Key** (For AI features)
   - We'll show you how to get this
   - It's free to start, but you'll need a credit card to register

## Step-by-Step Installation Guide 🚀

### Step 1: Installing Python 🐍

#### For Windows:
1. Go to [Python Downloads](https://www.python.org/downloads/)
2. Click the big yellow button that says "Download Python 3.11"
3. Run the downloaded file
4. ✨ Important: Check "Add Python to PATH" before clicking Install!
   ![Python Installation](https://i.imgur.com/XXX.png)

#### For Mac:
1. Open Terminal (press Cmd + Space, type "Terminal")
2. Install Homebrew if you don't have it:
   ```
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
3. Install Python:
   ```
   brew install python@3.11
   ```

### Step 2: Getting Your OpenAI API Key 🔑

1. Go to [OpenAI's website](https://platform.openai.com/signup)
2. Create an account or sign in
3. Click on your profile picture → "View API keys"
4. Click "Create new secret key"
5. Copy your API key and save it somewhere safe!

### Step 3: Setting Up The Project 📁

1. Download all project files from [our repository]
2. Create a new folder on your computer called "pdf-extractor"
3. Extract all downloaded files into this folder
4. Open Terminal/Command Prompt:
   - Windows: Press Win + R, type "cmd", press Enter
   - Mac: Press Cmd + Space, type "Terminal", press Enter

5. Navigate to your project folder:
   ```
   cd path/to/your/pdf-extractor
   ```
   Replace "path/to/your" with the actual path!

### Step 4: Installing Required Software 💻

Just copy and paste these commands into Terminal/Command Prompt:

```bash
# Install all required packages
pip install -r dependencies.txt
```

### Step 5: Configuration ⚙️

1. Create a new file named `.env` in your project folder
2. Add these lines to it:
   ```
   OPENAI_API_KEY=your_api_key_here
   FLASK_SECRET_KEY=make-up-any-random-string
   ```
3. Replace "your_api_key_here" with your OpenAI API key from Step 2

### Step 6: Starting the Application 🎉

1. In Terminal/Command Prompt, make sure you're in the project folder
2. Run:
   ```
   python main.py
   ```
3. Open your web browser and go to: http://localhost:5000
4. You should see the PDF Text Extractor interface!

## Using the Application 📝

1. **To Process a PDF**:
   - Either paste a PDF URL in the URL box
   - Or click "Choose File" to upload a PDF from your computer
   - Click "Extract"

2. **To Ask Questions**:
   - After processing a PDF, type your question in the question box
   - Click "Ask Question"
   - Wait for the AI to analyze and answer!

## Common Problems & Solutions 🔧

### "Python is not recognized..."
- Windows: Reinstall Python and make sure to check "Add Python to PATH"
- Mac: Try running `brew link python@3.11`

### "ModuleNotFoundError..."
- Run `pip install -r dependencies.txt` again
- Make sure you're in the right folder!

### "Invalid API key..."
- Double-check your OpenAI API key
- Make sure it's correctly copied into the .env file

### PDF Processing Fails
- Make sure the PDF isn't password protected
- Try a different PDF to see if it's just that file
- Check if the PDF URL is accessible

## Need More Help? 🆘

- Watch our [Video Tutorial](link-to-video)
- Join our [Discord Community](link-to-discord)
- Email support: support@example.com

## Important Notes 📌

- Free OpenAI API credits are limited
- Maximum PDF size: 50MB
- Supported formats: PDF only
- Keep your API key secret!

Remember: This is a learning experience! Don't worry if everything doesn't work perfectly the first time. Follow the steps carefully, and don't hesitate to ask for help if needed! 😊

## License 📄
This project is free to use under the MIT License.
