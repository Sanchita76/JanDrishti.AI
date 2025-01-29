# JanDrishti : Government Scheme-Research-Application
## Overview
The **Automated Scheme Research Tool** is a web application that processes scheme-related articles, generates relevant summaries, and enables users to ask questions based on the content of the articles. It leverages the power of LangChain, OpenAI embeddings, FAISS for similarity search, and Streamlit for a user-friendly interface. 

## Key Features
- **URL Input**: Users can input URLs of scheme articles or upload text files containing URLs.
- **Content Processing**: The tool uses LangChain's UnstructuredURLLoader to fetch article content and process it into manageable chunks.
- **Summarization**: The tool generates summaries for the following key criteria:
  - Scheme Benefits
  - Scheme Application Process
  - Eligibility
  - Documents Required
- **Similarity Search**: Using OpenAI embeddings and FAISS, users can ask questions, and the tool retrieves relevant answers along with source URLs and summaries.
- **Persistent Storage**: The FAISS index is stored locally in a pickle file for future use.

## Tech Stack
- **Python**: Core programming language.
- **Streamlit**: Framework for building the web application.
- **LangChain**: For processing and splitting text from URLs.
- **OpenAI**: For generating embeddings.
- **FAISS**: For efficient similarity search and fast information retrieval.
- **Unstructured**: For loading article content from URLs.
- **configparser**: To securely store and load the OpenAI API key.

## Setup Instructions
### Prerequisites
Ensure you have Python 3.x installed on your machine. Additionally, you will need an OpenAI API key. Follow the steps below to set up the project:
1. Clone the repository:
   git clone https://github.com/Sanchita76/JanDrishti-Tool.git<br>
   cd JanDrishti
2. Install the required dependencies:
   pip install -r requirements.txt
3. Set up your OpenAI API key:
Create a .config file in the root directory of the project.
Add the following content to the .config file, replacing YOUR_OPENAI_API_KEY with your actual OpenAI API key:
 [openai]
api_key = YOUR_OPENAI_API_KEY
4. Run the application: streamlit run main.py
5. Open the web app in your browser (usually at http://localhost:8501)
## File Structure
|-- main.py                     # The main Streamlit application script<br>
|-- requirements.txt            # List of dependencies for the project<br>
|-- .config                     # Configuration file for storing OpenAI API key<br>
|-- faiss_store_openai.pkl      # FAISS index file (generated after processing URLs)<br>

## Streamlit Application
![image](https://github.com/user-attachments/assets/225bbbb4-bdc9-4230-9a2e-643f8920a5b1)
## How to Use
Process URLs:
Input the URLs of the scheme articles in the sidebar.
Click on "Process URLs" to process the articles. The tool will fetch the content, split it into chunks, and create embeddings.
## Ask Questions:
Once the URLs are processed, enter a question in the "Ask Question" section on the sidebar.
Click "Ask Question", and the tool will display relevant answers along with the source URLs and summaries.
### Example of a typical question:
"What is the eligibility for this scheme?"
## Contributing
Feel free to fork the repository and submit pull requests. Any contributions are welcome!

## License
This project is licensed under the MIT License - see the LICENSE file for details.
This project is licensed under the MIT License - see the LICENSE file for details.

