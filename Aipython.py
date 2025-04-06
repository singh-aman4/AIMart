# ai_agents.py

from llama_index import VectorStoreIndex, SimpleKeywordTableIndex, ServiceContext, LLMPredictor
from llama_index.llms import OpenAI
import sqlite3

# Setting up LLM
llm_predictor = LLMPredictor(llm=OpenAI(temperature=0, model_name="gpt-3.5-turbo"))
service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)

# Connect to SQLite Database
conn = sqlite3.connect('user_data.db')
cursor = conn.cursor()

# Example of fetching user preferences
def get_user_preferences(user_id):
    cursor.execute("SELECT preferences FROM users WHERE user_id=?", (user_id,))
    result = cursor.fetchone()
    return result[0] if result else None

# Agent to recommend products
def product_recommendation_agent(user_id):
    preferences = get_user_preferences(user_id)
    if preferences:
        # Simulating AI recommendation based on preferences
        recommended_products = ["Smartwatch", "Wireless Earbuds", "Fitness Tracker"]
        return f"Recommended Products for you: {', '.join(recommended_products)}"
    else:
        return "No preferences found. Please update your profile."

# Example usage
if __name__ == "__main__":
    user_id = 1
    print(product_recommendation_agent(user_id))
