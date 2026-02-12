# 📚 DocuMind - PDF Q&A Chatbot

DocuMind is an intelligent PDF question-answering chatbot powered by RAG (Retrieval-Augmented Generation). Upload any PDF document and ask questions about its content through an intuitive web interface.

## ✨ Features

- **PDF Document Processing**: Upload and analyze PDF documents in real-time
- **AI-Powered Q&A**: Ask natural language questions and get accurate answers from your documents
- **RAG Architecture**: Utilizes Retrieval-Augmented Generation for context-aware responses
- **Modern UI**: Clean and intuitive interface built with vanilla JavaScript
- **LangSmith Integration**: Built-in tracing and monitoring for debugging and optimization
- **Multiple LLM Support**: Easily switch between different language models (Google Gemini, OpenAI, Ollama, HuggingFace)

## 🏗️ Architecture

The project follows a modular RAG (Retrieval-Augmented Generation) pipeline:

```
PDF Upload → Document Loading → Text Splitting → Embedding Generation 
→ Vector Store Creation → Retrieval → LLM Processing → Answer Generation
```

### Tech Stack

**Backend:**
- FastAPI - Modern web framework for building APIs
- LangChain - Framework for developing LLM applications
- ChromaDB - Vector database for storing document embeddings
- Google Gemini - Default LLM for question answering
- HuggingFace Embeddings - For document vectorization
- LangSmith - For tracing and monitoring

**Frontend:**
- HTML5, CSS3, JavaScript (Vanilla)
- Responsive design with modern UI/UX

## 📁 Project Structure

```
PDF_Q_AND_A_CHATBOT/
├── backend/
│   ├── app/
│   │   ├── main.py          # FastAPI application entry point
│   │   └── routes.py        # API endpoints for upload and Q&A
│   ├── rag/
│   │   ├── chain.py         # RAG chain construction
│   │   ├── embeddings.py    # Embedding model configuration
│   │   ├── loader.py        # PDF document loader
│   │   ├── pipeline.py     # Main RAG pipeline orchestration
│   │   ├── prompt.py       # Prompt templates
│   │   ├── retriever.py    # Document retriever setup
│   │   ├── splitter.py     # Text splitting logic
│   │   └── vectorstore.py  # Vector database operations
├── frontend/
│   ├── index.html           # Main HTML file
│   ├── app.js               # Frontend JavaScript logic
│   └── style.css            # Styling
├── .env                     # Environment variables (API keys)
├── README.md                # Project documentation
└── requirements.txt         # Python dependencies
```

## 🚀 Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- A Google API key (for Gemini)
- LangChain API key (for LangSmith tracing)
- Hugging Face API key (for embedding model)

### Step 1: Clone the Repository

```bash
git clone https://github.com/Arpit-saxena-2004/documind_rag_pdf_qa.git
cd documind-a_pdf_question_answer_chatbot-
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Configure Environment Variables

The project uses a `.env` file for configuration. **Important:** You must add your own API keys before running the project.

1. Open the `.env` file in the root directory
2. Add your API keys:

```env
# Required: Get from https://makersuite.google.com/app/apikey
GOOGLE_API_KEY = "your-google-api-key-here"

# LangSmith Configuration (for tracing and monitoring)
LANGCHAIN_TRACING_V2 = true
LANGCHAIN_ENDPOINT = "https://api.smith.langchain.com"
LANGCHAIN_API_KEY = "your-langsmith-api-key-here"  # Get from https://smith.langchain.com
LANGCHAIN_PROJECT = "pdf_q_&_a_chatbot"


HUGGINGFACEHUB_API_TOKEN = "your hf token here"
```

**🔑 Where to Get API Keys:**

- **Google API Key**: Visit [Google AI Studio](https://makersuite.google.com/app/apikey) and create a new API key
- **LangChain API Key**: Sign up at [LangSmith](https://smith.langchain.com) and generate an API key from your settings
- **LHuggingFace API Key**: Sign up at [HuggingFace](https://huggingface.co/settings/tokens) and generate an API key .

**⚠️ Security Note:** 
- Never commit your actual API keys to GitHub
- The `.env` file in this repository contains placeholder values
- Replace them with your own keys before running the project

### Step 4: Run the Backend Server

Navigate to the project root directory and run:

```bash
uvicorn backend.app.main:app --reload
```

The backend server will start at `http://127.0.0.1:8000`

**Optional flags:**
- `--reload`: Auto-reload on code changes (development mode)
- `--host 0.0.0.0`: Make server accessible from other devices on your network
- `--port 8080`: Change the port (default is 8000)

### Step 5: Run the Frontend

You have multiple options to serve the frontend:

**Option 1: Using Python's built-in server**
```bash
cd frontend
python -m http.server 3000
```
Then open `http://localhost:3000` in your browser

**Option 2: Using VS Code Live Server**
- Install the "Live Server" extension in VS Code
- Right-click on `index.html` and select "Open with Live Server"

**Option 3: Direct file opening**
- Simply open `frontend/index.html` in your browser
- Note: Some features may require a proper server

## 📖 Usage

1. **Start the backend server** using the uvicorn command
2. **Open the frontend** in your web browser
3. **Upload a PDF**: Click "Choose PDF" in the sidebar and select your document
4. **Click "Analyze Document"**: Wait for the processing to complete
5. **Ask questions**: Type your question in the chat input and press Enter or click the send button
6. **Get answers**: The AI will retrieve relevant information from your document and provide answers

## 🔧 Configuration

### Changing the LLM Model

The default model is Google Gemini. To use a different model, edit `backend/rag/pipeline.py`:

```python
# Current (Google Gemini - Default)
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# OpenAI GPT-4
# llm = ChatOpenAI(model="gpt-4o")

# Local Ollama Model
# llm = ChatOllama(model="mistral:latest", num_gpu=0)

# HuggingFace Model
# llm = HuggingFaceEndpoint(repo_id="google/flan-t5-base", task="text2text-generation")
```

### Adjusting Embedding Device

By default, embeddings run on CPU. To use GPU, edit `backend/rag/embeddings.py`:

```python
return HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "cuda"},  # Change from "cpu" to "cuda"
    encode_kwargs={"normalize_embeddings": True}
)
```


## 🐛 Troubleshooting

### Common Issues

**1. "GOOGLE_API_KEY is not set" error**
- Make sure you've added your Google API key to the `.env` file
- Ensure the `.env` file is in the root directory (same level as backend folder)

**2. Backend server won't start**
- Check if port 8000 is already in use
- Try changing the port: `uvicorn backend.app.main:app --port 8080`

**3. Frontend can't connect to backend**
- Verify the backend is running at `http://127.0.0.1:8000`
- Check if CORS is enabled (it's configured in `main.py`)
- Ensure `BACKEND_URL` in `app.js` matches your backend address

**4. PDF upload fails**
- Ensure the file is a valid PDF
- Check if the PDF is not corrupted
- Large PDFs may take longer to process

**5. Slow response times**
- First query after upload is slower (embedding generation)
- Subsequent queries should be faster
- Consider using GPU for embeddings if available

## 🔍 LangSmith Tracing

This project is configured to use LangSmith for tracing and debugging. Once configured:

1. Visit [LangSmith](https://smith.langchain.com)
2. Navigate to your project: "pdf_q_&_a_chatbot"
3. View detailed traces of each query, including:
   - Document retrieval steps
   - LLM prompts and responses
   - Execution time for each component

This helps you understand and optimize the RAG pipeline performance.

## ⚠️ Known Limitations & Deployment Status

### Why This Project is Not Deployed

Currently, this project is **not deployed to production** due to significant embedding generation challenges:

**Embedding Model Limitations:**

1. **Google's Embedding API** (via API):
   - Frequently hits rate limits even with moderate usage
   - Results in "Quota exceeded" or "Rate limit" errors
   - Not suitable for production deployment without paid tier

2. **HuggingFace Embeddings** (Current Implementation - Local):
   - Uses `sentence-transformers/all-MiniLM-L6-v2` model
   - Runs locally on CPU by default
   - **Very slow** for large documents (can take several minutes)
   - Acceptable for local testing but not ideal for production

**Current Recommendation:**
- This project works best for **local development and testing**
- For production deployment, you would need:
  - A paid embedding API service (OpenAI, Cohere, etc.)
  - A GPU-enabled server for faster local embeddings
  - Or a hybrid solution with caching mechanisms

### 🆘 Looking for Solutions

If you have experience with:
- Efficient embedding generation strategies
- Cost-effective embedding API alternatives
- Optimizing HuggingFace embeddings for production
- GPU-based deployment solutions

**Please reach out! I'd love to hear your suggestions:**
- 📧 Email: [arpitsaxena1009@gmail.com](mailto:arpitsaxena1009@gmail.com)
- 💼 LinkedIn: [Arpit Saxena](https://www.linkedin.com/in/arpit-saxena1009)
- 📱 WhatsApp: +91-9045280754

Your insights could help make this project production-ready!

## 📝 API Endpoints

### POST `/upload`
Upload a PDF document for processing.

**Request:**
- Content-Type: `multipart/form-data`
- Body: PDF file

**Response:**
```json
{
  "message": "PDF uploaded and processed"
}
```

### POST `/ask`
Ask a question about the uploaded document.

**Request:**
```json
{
  "question": "What is the main topic of this document?"
}
```

**Response:**
```json
{
  "answer": "The main topic is..."
}
```

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 📧 Contact

For any queries or technical support:

- **Email**: [arpitsaxena1009@gmail.com](mailto:arpitsaxena1009@gmail.com)
- **LinkedIn**: [Arpit Saxena](https://www.linkedin.com/in/arpit-saxena1009)

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- LangChain for the excellent LLM framework
- Google for Gemini API
- HuggingFace for embedding models
- FastAPI for the robust backend framework

---

**Made with ❤️ by Arpit Saxena**
