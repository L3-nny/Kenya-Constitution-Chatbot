Kenya Constitution Chatbot
This project is designed to create a chatbot that can answer questions about the Kenya Constitution using Natural Language Processing (NLP) techniques. The chatbot extracts and processes text from the Kenya Constitution PDF to provide accurate and real-time responses to user queries.
Table of Contents
Business Understanding
2. Data Understanding
3. Data Preparation
Modeling
5. Evaluation
6. Deployment
Usage
Contributing
9. License
Business Understanding
The Constitution of Kenya is a critical document that outlines the structure of government, the rights and duties of citizens, and the principles guiding the rule of law. However, many citizens face challenges in accessing and understanding it due to its complex legal language. This project aims to bridge this gap by developing a user-friendly question-answering system that simplifies access to constitutional knowledge.
Objectives
Create a User-Friendly Interface: Develop an intuitive interface for seamless interaction with the Q&A system.
Improve Legal Literacy: Educate users about their constitutional rights and responsibilities.
Support Legal Practitioners: Assist legal professionals in retrieving relevant constitutional information quickly.
Leverage NLP Techniques: Use advanced NLP to interpret questions and match them with the appropriate sections of the Constitution.

Data Understanding
Data Source: The primary data source is the full PDF of the Kenyan Constitution.
Content and Structure Analysis: The document contains 18 chapters, each addressing distinct themes such as judicial authority, human rights, and governance.
Data Preparation
Text Extraction: Using pdfplumber, the text is extracted while maintaining the original structure.
Text Cleaning and Preprocessing: Includes tokenization, stopword removal, and lemmatization.
Synonym and Keyword Mapping: A dictionary is created to map legal terms to layperson synonyms.
Modeling
The core functionality is the Question-Answering Mechanism, which uses NLP and Natural Language Understanding (NLU) to interpret user queries and retrieve relevant constitutional sections.
Key Techniques
Named Entity Recognition (NER): Identifies essential entities in user queries.
Semantic Similarity Scoring: Matches terms with similar or alternative wording.
Query Expansion: Captures synonyms and related terms to broaden understanding.
Evaluation
Testing and Accuracy: Sample questions are tested to ensure accurate retrieval of relevant sections.
User Feedback: Feedback collected via Telegram helps refine the system.
Deployment
Telegram Integration: The chatbot is deployed on Telegram, allowing users to interact in a familiar environment.
Real-time Response: The system processes queries and responds with the best-matching constitutional article.
Usage
To use the chatbot, simply ask questions about the Kenya Constitution via the Telegram interface. The system will process your query and provide the most relevant section from the Constitution.
Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.
