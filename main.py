import os
import sys
import argparse
from google import genai
from google.genai import types
from dotenv import load_dotenv

parser = argparse.ArgumentParser()
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

user_prompt = input("Enter your prompt: ")
if not user_prompt:
    print("No prompt provided. Exiting.")
    sys.exit(1)

messages = [
    types.Content(
        role="user",
        parts = [types.Part(text=user_prompt)]
    )
]

response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents = messages
)

metadata = response.usage_metadata

print(f"RESPONSE: {response.text} \n")

args = parser.parse_args()
if args.verbose:
    print("Response metadata:")
    print(f"User prompt: {user_prompt}")
    print(f"Prompt token count: {metadata.prompt_token_count}")
    print(f"Candidates token count: {metadata.candidates_token_count}")
