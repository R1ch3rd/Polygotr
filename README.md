# Poygotr

Poygotr is a translation service that allows users to translate text into multiple languages of their choice. Users can provide the text they want to translate and specify the target languages. All translations are stored in a PostgreSQL database for easy access and future reference. The translation process is powered by the Gemini API.

## Features

- **Multi-Language Translation**: Translate text into multiple languages at once.
- **Persistent Storage**: All translations are stored in a PostgreSQL database, making them accessible later.
- **FastAPI Backend**: Built using FastAPI for high performance and scalability.
- **Easy-to-Use**: Simple input method for text and target languages.
- **Gemini API Integration**: Uses the Gemini API to provide accurate and reliable translations.

## Tech Stack

- **Backend**: FastAPI
- **Database**: PostgreSQL
- **Translation Service**: Gemini API

## Installation

To get started with Poygotr, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/poygotr.git
   cd poygotr
2. Create a virtual environment and activate it:
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
3. Install the dependencies
     ```
     pip install -r requirements.txt
     ```
     in addition to this, run this command too
     ```
     pip install -q -U google-generativeai
5. Set up the PostgreSQL database. Create a database and update the connection details in the  .env file.
6. Start the application:
     ```
   uvicorn main:app --reload
