import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

client = MongoClient(os.getenv("MONGODB_URI"))

db = client["GenAI"]
collection = db["api_usage"]

collection.insert_one({
    "prompt": "Explain Generative AI",
    "response": "Generative AI creates new content using AI models."
})

print("Data inserted successfully!")