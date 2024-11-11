# Kenya Constitution Chatbot Project

## Overview
The Kenya Constitution Analysis Project is a Jupyter Notebook-based application designed to extract, process, and analyze the text of the Kenya Constitution from a PDF file. This project leverages natural language processing (NLP) techniques to enable users to query specific sections of the constitution, making it a valuable tool for legal studies, civic education, and research.

## Features
- **PDF Text Extraction**: Extracts text from specified pages of the Kenya Constitution PDF using `pdfplumber`.
- **Text Processing**: Organizes the extracted text into structured chapters and sections for easy access.
- **Natural Language Processing**: Utilizes `spaCy` for preprocessing user queries, including lemmatization and stopword removal.
- **Question Answering System**: Allows users to ask questions related to specific sections of the constitution and receive relevant answers.
- **Synonym Mapping**: Enhances query recognition by mapping synonyms to key terms in the constitution.

## Installation
To run this project, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/kenya-constitution-analysis.git
   cd kenya-constitution-analysis
   ```

2. **Install the required libraries**:
   You can install the necessary libraries using pip. Run the following command:
   ```bash
   pip install spacy pdfplumber pyspellchecker
   ```

3. **Download the spaCy model**:
   You will also need to download the English language model for spaCy:
   ```bash
   python -m spacy download en_core_web_sm
   ```

4. **Add the Kenya Constitution PDF**:
   Place the Kenya Constitution PDF file in the project directory and update the file path in the notebook accordingly.

## Usage
1. Open the Jupyter Notebook in your preferred environment (e.g., Jupyter Lab, Jupyter Notebook).
2. Run the cells sequentially to extract and process the text from the Kenya Constitution.
3. Use the provided examples to query specific sections of the constitution. You can modify the example queries or input your own questions.

#python
user_query = "What is the supremacy of the constitution?"
answer = answer_question_nlp(user_query, sections, qa_mapping)
print(answer)


## Contributing
Contributions to this project are welcome! Here’s how you can contribute:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes.
Push to your fork (git push origin feature-branch).
Submit a pull request to the main repository.
If you have suggestions for improvements or new features, please feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](license.txt) file for more details.

## Acknowledgments
- [spaCy](https://spacy.io/) for natural language processing capabilities.
- [pdfplumber](https://github.com/jsvine/pdfplumber) for PDF text extraction.
- [pyspellchecker](https://github.com/bjh21/python-spellchecker) for spelling correction.




