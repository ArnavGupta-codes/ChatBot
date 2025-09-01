# ChatBot: RAG-powered Web Chatbot

A conversational chatbot web app that uses Retrieval-Augmented Generation (RAG) to answer questions about your PDF dataset. Built with Flask, Gemini API, and modern NLP tools.
Build above our team project Chatbot: https://github.com/Zeusius1407/RAG_Project

https://github.com/user-attachments/assets/f2d114e8-57bb-46a2-8918-87dd6a4dd2a2

## Features
- Chat interface (remembers last 4-5 messages for context)
- Answers questions using information from a PDF
- Uses Google Gemini API for answer generation
- Embeds and retrieves relevant PDF chunks with Sentence Transformers and ChromaDB
- Easy to run locally or deploy to cloud (Render, Railway, etc.)

## Tech Stack / Libraries Used
- Python 3
- Flask
- PyPDF2
- google-generativeai (Gemini API)
- sentence-transformers
- transformers
- chromadb
- numpy
- python-dotenv

## How to Run Locally
1. **Clone the repository:**
   ```
   git clone <your-repo-url>
   cd ChatBot
   ```
2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```
3. **Add your Gemini API key:**
   - Create a `.env` file in the project root:
     ```
     GEMINI_API_KEY=your_gemini_api_key_here
     ```
4. **Add your PDF:**
   - Place your PDF (e.g., `Inductions_Catalogue.pdf`) in the `static/` folder.
   - Update the PDF path in `main.py` if needed.
5. **Run the app:**
   ```
   python webapp.py
   ```
   - Open your browser at [http://localhost:5000](http://localhost:5000)

## Deployment
- Ready for Render, Railway, or Heroku.
- Make sure to set your `GEMINI_API_KEY` as an environment variable on the platform.
- The app will use the correct port automatically.

## Security
- **Never commit your `.env` file or API keys to GitHub.**
- Add `.env` to your `.gitignore`.

## Customization
- To use a different PDF, replace the file in `static/` and update the path in `main.py` if needed.
- The chat UI and memory can be further customized in `templates/index.html`.






