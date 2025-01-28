# Scheme-Research-Application
## The goal of this assignment is to develop an automated Scheme Research Tool.
### This tool will take the URL of a scheme article as input, create an accurate and relevant
summary and enable users to ask questions based on the content of the article. The
tool will provide a summary covering four key criteria: Scheme Benefits, Scheme
Application Process, Eligibility, and Documents required; along with the features
mentioned below:-<br>
● Load URLs or upload text files containing URLs to fetch article content.<br>
● Process article content through LangChain's UnstructuredURL Loader.<br>
● Construct an embedding vector using OpenAI's embeddings and leverage FAISS,<br>
a powerful similarity search library, to enable swift and effective retrieval of
relevant information.<br>
● Interact with the LLM's (ChatGPT etc.) by inputting queries and receiving answers<br>
along with source URLs and its summary.<br><br><br>
### Solution <br>
● The web app will open in your browser.<br>
● On the sidebar, users can input URLs directly.<br>
● Data loading and processing are initiated by clicking "Process URLs."<br>
● The system performs text splitting, generates embedding vectors, and efficiently
indexes them using FAISS.<br>
● The embeddings are stored and indexed using FAISS, enhancing retrieval speed.<br>
● The FAISS index is saved in a local file path in pickle format for future use.<br>
● Users can ask a question and receive an answer based on the news articles,
along with the URL and its summary.<br>
## Strea=mlit Application
![image](https://github.com/user-attachments/assets/225bbbb4-bdc9-4230-9a2e-643f8920a5b1)

