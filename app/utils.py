import google.generativeai as genai
from sqlalchemy.orm import Session
from crud import update_translation_task
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GEMINI_KEY")
if not api_key:
    raise ValueError("GEMINI_KEY not found in environment variables")
genai.configure(api_key=api_key)

def perform_translation(task_id: int, text: str, Languages:list, db:Session):
    translations = {}
    model = genai.GenerativeModel("gemini-1.5-flash")
    for lang in Languages:
        try:
            prompt = f"Translate the following text into {lang}:\n\n{text}"
            response = model.generate_content(prompt)
            
            if response.text:
                translated_text = response.text.strip()

                translations[lang] = translated_text
                
            else:
                raise ValueError("No text in response")
        except Exception as e:
            print(f"error handling to {lang}:{e}")
            translations[lang]= f"Error: {e}"

    try:
        update_translation_task(db, task_id, translations)
    except Exception as e:
        print(f"Error updating translation task: {e}")
    return