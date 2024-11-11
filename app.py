import logging
import json
import spacy
from spellchecker import SpellChecker
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackContext
import nest_asyncio
import asyncio
import os
from dotenv import load_dotenv

logging.basicConfig(level=logging.DEBUG)


# Load the environment variables
load_dotenv()  # Loads the .env file
bot_token = os.getenv("BOT_TOKEN")
logging.info("Environment variables loaded.")


# Apply the nest_asyncio patch
nest_asyncio.apply()

# Initialize spaCy and load the language model
nlp = spacy.load("en_core_web_sm")

# Initialize spell checker
spell = SpellChecker()

# Load combined_sections from JSON file
with open("combined_sections.json", "r", encoding="utf-8") as json_file:
    sections = json.load(json_file)

# Load synonyms and qa_mapping from JSON file
with open("synonyms.json", "r", encoding="utf-8") as json_file:
    synonyms = json.load(json_file)

with open("qa_mapping.json", "r", encoding="utf-8") as json_file:  # Corrected file name
    qa_mapping = json.load(json_file)

with open("citizenship_mapping.json", "r", encoding="utf-8") as json_file:  # Corrected file name
    citizenship_mapping = json.load(json_file)

# Function to preprocess query
def preprocess_query(query):
    doc = nlp(query)
    tokens = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct]
    return " ".join(tokens)

# Function to correct spelling
def correct_spelling(processed_query):
    words = processed_query.split()
    misspelled_words = spell.unknown(words)
    corrected_words = [spell.correction(word) if word in misspelled_words else word for word in words]
    return " ".join(corrected_words)

# Function to match with synonym support
def match_with_synonyms(query, qa_mapping, synonyms, citizenship_mapping):
    processed_query = preprocess_query(query)
    corrected_query = correct_spelling(processed_query)

    # Check for specific citizenship subtopics first
    for subtopic, section_key in citizenship_mapping.items():
        if subtopic in corrected_query:
            return section_key

    # General citizenship check
    if "citizenship" in corrected_query:
        return "citizenship"

    # Synonym matching
    for key in qa_mapping:
        for synonym in synonyms.get(key, [key]):
            if synonym in corrected_query:
                return key
    return None

# Answer function
def answer_question_nlp(query):
    prioritized_keys = []

    if "language" in query and "culture" in query:
        prioritized_keys.append('language culture')
    elif "implementation" in query and "rights" in query:
        prioritized_keys.append("implementation right")
    elif "authority" in query and "court" in query and "bill" in query and "right" in query:
        prioritized_keys.append("authority court bill right")
    elif "secretary" in query and "cabinet" in query:
        prioritized_keys.append("secretary cabinet")
    elif "special" in query:
        prioritized_keys.append("special bill county government")
    elif "ordinary" in query and "county" in query:
        prioritized_keys.append("ordinary bill county government")
    elif "vote" in query and "parliament" in query:
        prioritized_keys.append("vote parliament")
    elif "defence" in query and "forces" in query:
        prioritized_keys.append("defence forces")
    elif "legislative" in query and "authority" in query:
        prioritized_keys.append("legislative authority")
    elif "equitable" in query and "sharing" in query and "revenue" in query:
        prioritized_keys.append("equitable share national revenue")
    elif "national" in query and "debt" in query:
        prioritized_keys.append("national debt")
    elif "commission" in query and "revenue" in query:
        prioritized_keys.append("commission on revenue allocation")
    elif "central" in query and "financial" in query and "authority" in query:
        prioritized_keys.append("central financial authority")
    elif "division" in query and "revenue" in query:
        prioritized_keys.append("division revenue")
    elif "revenue" in query and "distribution" in query:
        prioritized_keys.append("revenue distribution")
    elif "allocation" in query and "revenue" in query:
        prioritized_keys.append("allocation of revenue")
    elif "budget" in query and "content" in query:
        prioritized_keys.append("budget content")
    elif "budget" in query and "structure" in query:
        prioritized_keys.append("budget structure")
    elif "budget" in query and "framework" in query:
        prioritized_keys.append("budget framework")
    elif "amendment" in query and "parliamentary" in query:
        prioritized_keys.append("parliamentary initiative")
    elif "amendment" in query and "popular" in query:
        prioritized_keys.append("popular initiative")
    elif "decision" in query and "cabinet" in query:
        prioritized_keys.append("decision cabinet")
    elif "incorporation" in query and "independent" in query:
        prioritized_keys.append("incorporation commission independent office")
    elif "principle" in query and "security" in query:
        prioritized_keys.append("principle national security")
    elif "national" in query and "security" in query and "organ" in query:
        prioritized_keys.append("national security organ")
    elif "security" in query and "council" in query:
        prioritized_keys.append("national security council")
    elif "function" in query and "police" in query:
        prioritized_keys.append("function national police service")
    elif "command" in query and "police" in query:
        prioritized_keys.append("command national police service")
    elif "police" in query and "commission" in query:
        prioritized_keys.append("national police service commission")
    elif "national" in query and "police" in query:
        prioritized_keys.append("national police service")
    
    # Check for a prioritized match
    for key in prioritized_keys:
        if key in sections:
            return sections[key]
    
    # Fallback to general synonym mapping if no priority match is found
    section_key = match_with_synonyms(query, qa_mapping, synonyms, citizenship_mapping)
    if section_key in sections:
        return sections.get(section_key, "Section not found.")
    elif section_key == "citizenship":
        return (f"It seems you're interested in citizenship. "
                f"Available subtopics include: {list(citizenship_mapping.keys())}.")
    return "Sorry, I couldn't find an answer to your question."

# Handler for messages
async def handle_message(update: Update, context: CallbackContext) -> None:
    user_query = update.message.text
    logging.info(f"Received message: {user_query}")
    answer = answer_question_nlp(user_query)
    await update.message.reply_text(answer)

# Main function to set up the bot
async def main() -> None:
    # Initialize the application and start the bot
    application = ApplicationBuilder().token(bot_token).build()
    
    # Adding the message handler for text messages
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Start the bot
    await application.initialize()
    await application.start()
    await application.updater.start_polling()

# Run the bot in the script
if __name__ == "__main__":
    asyncio.run(main())