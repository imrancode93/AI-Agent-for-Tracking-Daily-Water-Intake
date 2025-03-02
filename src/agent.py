import os
from langchain_openai import ChatOpenAI  # Corrected import
from langchain.schema import HumanMessage
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize the LLM model (OpenAI GPT)
llm = ChatOpenAI(api_key=OPENAI_API_KEY, model="gpt-4", temperature=0.5)  # Fixed 'model_name' -> 'model'

class WaterIntakeAgent:
    """AI agent to track and suggest daily water intake."""

    def __init__(self):
        self.history = []

    def analyze_intake(self, intake_ml):
        """Analyze the user's water intake and provide feedback."""
        prompt = f"""
        You are a hydration assistant. The user has consumed {intake_ml} ml of water today.
        Provide a hydration status and suggest if they need to drink more water.
        """
        response = llm.invoke([HumanMessage(content=prompt)])  # Fixed method call
        return response.content

# Example usage
if __name__ == "__main__":
    agent = WaterIntakeAgent()
    intake = 1500  # Example intake in ml
    feedback = agent.analyze_intake(intake)
    print(f"Hydration Analysis: {feedback}")
