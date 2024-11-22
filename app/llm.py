import json
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
OpenAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OpenAI_API_KEY)

user_request = "Make an entry to my table with key 'name' and value is 'dhruv'. Also remove data with key 'email' and value 'dgb@gmail.com'. also change my existing name from dhruv to dev"

def parse_from_llm(user_request):
    try:
        # Call OpenAI API
        completion = client.chat.completions.create(
            model="gpt-4o-2024-05-13",
            messages=[
                {
                    "role": "user",
                    "content": "You are an assistant that parses natural language requests into structured JSON for backend operations. "
                            "Here are some examples:\n\n"
                            "Example 1:\n"
                            "Input: \"Insert an entry with key 'user.name' and value 'John Doe'.\"\n"
                            "Output: [{\n"
                            "    \"action\": \"insert\",\n"
                            "    \"key\": \"user.name\",\n"
                            "    \"value\": \"John Doe\"\n"
                            "}]\n\n"
                            "Example 2:\n"
                            "Input: \"Update the value of key 'project.status' to 'completed'.\"\n"
                            "Output: [{\n"
                            "    \"action\": \"update\",\n"
                            "    \"key\": \"project.status\",\n"
                            "    \"value\": \"completed\"\n"
                            "}]\n\n"
                            "Example 3:\n"
                            "Input: \"Delete the entry with key 'session.id'.\"\n"
                            "Output: [{\n"
                            "    \"action\": \"delete\",\n"
                            "    \"key\": \"session.id\",\n"
                            "    \"value\": null\n"
                            "}]"
                },
                {
                    "role": "user",
                    "content": f"Input: \"{user_request}\""
                }
            ]
        )
        # Return the structured JSON from the API response
        response_text=completion.choices[0].message.content

        cleaned_response = response_text.strip().replace("```json", "").replace("```", "").strip()

        response_json = json.loads(cleaned_response)  # Parse the string as a JSON list
        return response_json
    except json.JSONDecodeError as e:
        raise e
    except Exception as e:
        raise e
    
# print(parse_from_llm("Insert key: Dev with value: Patel. Update key: Dev with value: Ashishkumar"))