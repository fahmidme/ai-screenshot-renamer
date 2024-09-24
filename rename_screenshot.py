# Documents/rename_screenshot.py
import sys
import os
from datetime import datetime
from dotenv import load_dotenv
import base64
from openai import OpenAI

# Load environment variables
load_dotenv()

def describe_image(image_path):
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in environment variables")

    client = OpenAI(api_key=api_key)

    # Encode the image
    with open(image_path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode('utf-8')

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Describe this image concisely in up to 20 words. Use keywords."},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        max_tokens=300
    )

    return response.choices[0].message.content.strip()

def rename_file(image_path, description):
    # Check if the file has already been processed
    if "_20" in os.path.basename(image_path) and len(os.path.basename(image_path).split('_')) > 2:
        print(f"File {image_path} has already been processed. Skipping.")
        return

    # Format description to a valid filename
    valid_filename = ''.join(c if c.isalnum() or c in (' ', '-') else '_' for c in description)
    base_path = os.path.dirname(image_path)
    current_date = datetime.now().strftime("%Y-%m-%d")
    new_filename = f"{valid_filename}_{current_date}.png"
    new_path = os.path.join(base_path, new_filename)

    # Normalize paths to avoid issues with spaces and special characters
    image_path = os.path.normpath(image_path)
    new_path = os.path.normpath(new_path)

    try:
        os.rename(image_path, new_path)
        print(f"File renamed to: {new_path}")
    except FileNotFoundError as e:
        print(f"Error renaming file: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    # Check if a file path is provided
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        print(f"Processing file: {file_path}")

        # Normalize the file path to handle any inconsistencies
        file_path = os.path.normpath(file_path)

        try:
            description = describe_image(file_path)
            rename_file(file_path, description)
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
    else:
        print("No file path provided.")