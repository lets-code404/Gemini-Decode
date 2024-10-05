# Gemini Decode Application

The **Gemini Decode Application** is a powerful tool built using **Streamlit** that leverages the **Gemini Pro AI model** to extract information from multilingual documents. The app enables users to upload images of documents in various languages and get responses to their queries, effectively bridging language barriers.

## Features
- Extracts and translates content from document images.
- Supports multiple languages.
- Simple and user-friendly interface for ease of use.
  
## Requirements
Before running the application, ensure you have the following files set up:
1. `.env` - Stores your Google API Key.
2. `app.py` - Main application code.
3. `requirements.txt` - Lists required Python libraries.

### Required Python Libraries:
- **streamlit**
- **google-generativeai**
- **python-dotenv**
- **langchain**
- **PyPDF2**
- **chromadb**
- **faiss-cpu**
- **streamlit-extras**
- **Pillow**

### Setup Instructions
1. Install Python and pip if not already installed.
2. Clone the repository and navigate to the project directory.
3. Run the following command to install all required libraries:
    ```bash
    pip install -r requirements.txt
    ```
4. Create a `.env` file and add your Google API Key:
    ```
    GOOGLE_API_KEY="your-google-api-key"
    ```

## How to Run the Application
1. Start the application by running the following command in your terminal:
    ```bash
    streamlit run app.py
    ```
2. The app will start on a local server, and you'll see a local URL in your terminal. Open the link in your browser.

## Application Flow
1. Upload an image of a document in a supported format (`.jpg`, `.jpeg`, `.png`).
2. Input your query (e.g., "Translate the document to English").
3. Submit the form and view the AI-generated response.

## Example
If you upload a German document and ask to translate it to English, you will receive a pointwise translation of the content. The same process applies to documents in French or any other supported language.

## Conclusion
The Gemini Decode Application simplifies multilingual document processing and enhances productivity by enabling users to extract and interact with content in a range of languages.
