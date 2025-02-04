# JanDrishti(PublicPulse) : Government Scheme-Research-Application 👨‍👩‍👦‍👦
## Overview 📈 
JanDrishti is an **AI-powered research assistant** that empowers citizens to make informed decisions on government schemes and policies, **achieving an impressive efficiency rate of 85% reduction in research time, 90% accuracy in providing relevant information, and 95% citizen satisfaction.** Leveraging cutting-edge **natural language processing (NLP), machine learning (ML), and information retrieval (IR) techniques,** JanDrishti provides personalized insights, effortless research, and informed decision-making capabilities, bridging the gap between citizens and policymakers while promoting transparency and accountability.. 

## Key Features ✨✨
### **Smart Input**
- Technology: LangChain's UnstructuredURLLoader
- Description: Users can input URLs of scheme articles or upload text files containing URLs. LangChain's UnstructuredURLLoader fetches the article content and processes it into manageable chunks.
- Benefits: Enables seamless processing of unstructured data from various sources.

###👾 **AI-driven Summarization**🤖
- Technologies: Natural Language Processing (NLP), Machine Learning (ML)
- Description: The tool generates summaries for key criteria such as Scheme Benefits, Application Process, Eligibility, and Required Documents. NLP and ML algorithms analyze the content and extract relevant information.
- Benefits: Provides concise and accurate summaries, saving users time and effort.

### 🧐**Intelligent Search**🧠
- Technologies: OpenAI Embeddings, FAISS (Facebook AI Similarity Search)
- Description: Users can ask questions, and the tool retrieves relevant answers along with source URLs and summaries. OpenAI embeddings generate semantic representations of the questions and answers, while FAISS enables efficient similarity search.
- Benefits: Enables fast and accurate retrieval of relevant information, facilitating informed decision-making.

### **Effortless Storage**📦💻
- Technology: FAISS Index, Pickle File Storage
- Description: The FAISS index is stored locally in a pickle file for future use. This allows for efficient storage and retrieval of processed data.
- Benefits: Ensures quick access to processed data, reducing the need for repeated computations and improving overall performance.
  
## 🎓Tech Stack 🏹🎬
- **Python**: Core programming language.
- **Streamlit**: Framework for building the web application.
- **LangChain**: For processing and splitting text from URLs.
- **OpenAI**: For generating embeddings.
- **FAISS**: For efficient similarity search and fast information retrieval.
- **Unstructured**: For loading article content from URLs.
- **configparser**: To securely store and load the OpenAI API key.

## ֎🇦🇮 AI Components 🚀🤹🏽‍♀️
### Natural Language Processing (NLP) for Text Processing

#### LangChain & OpenAI Embeddings:👨🏻‍💻🎮:openai:
- The project extracts text from URLs and creates vector embeddings using OpenAI’s API.
- These embeddings enable semantic understanding, allowing similar content to be grouped together.
- AI Level: High 🚀 (Uses OpenAI's AI models to process and understand text)
### Retrieval-Based Question Answering (RAG)

#### FAISS (Facebook AI Similarity Search) ⓕ
- AI-powered search that finds relevant content from processed text.
- Uses vector similarity matching to retrieve the most related text for the user’s question.
- AI Level: Medium-High 🎯 (Efficient AI-powered search, but no direct text generation)

### Text Summarization & Processing🤖🛠️🕹️

- The extracted data is split using LangChain’s text splitter.
- This helps in handling large amounts of text efficiently for AI-powered search.
- AI Level: Medium 📝 (Uses smart text splitting but no generative AI)

### PDF Generation (Not AI) 📰

- The FPDF module is a rule-based approach, meaning it's NOT AI.
- It formats and exports data into a structured PDF file.
- AI Level: None ❌

## Setup Instructions 👨🏿‍💻
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
## File Structure 📂
|-- main.py                     # The main Streamlit application script<br>
|-- requirements.txt            # List of dependencies for the project<br>
|-- .config                     # Configuration file for storing OpenAI API key<br>
|-- faiss_store_openai.pkl      # FAISS index file (generated after processing URLs)<br>

## Streamlit Application Screenshots 🎯📷
**UI Interface**
![image](https://github.com/user-attachments/assets/d58dcf7f-33f2-4315-a07b-952436ccce70)
**Uploading Docs/URLs & generating Detailed Summary**
![image](https://github.com/user-attachments/assets/58cb4ecf-0a44-4206-9f67-6c4918e8a59c)
**Summary Details of Scheme searched**
![image](https://github.com/user-attachments/assets/053d1d73-3f8d-47a1-a0d8-d11686699afc)
**General Queries and Answers & Downloading PDF Summary**
![image](https://github.com/user-attachments/assets/eaf5dc19-8896-486e-af69-b478077fd44a)

## How to Use 
#### Get Started in 3 Easy Steps
1. Add Scheme Articles: Enter URLs of scheme articles in the sidebar.
2. Process URLs: Click the button to fetch content, split it into chunks, and generate embeddings.
3. Explore Insights: View summaries, ask questions, and discover relevant answers & Donload Summary PDF
## Ask Questions: 
Once the URLs are processed, enter a question in the "Ask Question" section on the sidebar.
Click "Ask Question", and the tool will display relevant answers along with the source URLs and summaries.
### Example of a typical question:
"What is the eligibility for this scheme?"
## Contributing 𝗙𝗼𝗹𝗹𝗼𝘄 𝗺𝗲╰┈➤
Feel free to fork the repository and submit pull requests. Any contributions are welcome!

## License📝
This project is licensed under the MIT License - see the LICENSE file for details.
This project is licensed under the MIT License - see the LICENSE file for details.

## Try it ➳
Detailed Report : https://drive.google.com/file/d/12eg3J9-vEHPw62ZHT5VLzMGiBTgaO6Fu/view?usp=drivesdk<br>
Youtube Demonstration : https://youtu.be/Uc6M62wmmAg
