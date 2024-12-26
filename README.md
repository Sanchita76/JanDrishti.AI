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
along with source URLs and its summary.<br>
