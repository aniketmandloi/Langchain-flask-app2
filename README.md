# Flask-Langchain-Chatbot

Flask-Langchain-Chatbot is a web application that utilizes LangChain technology to provide AI-generated responses to user inputs. It integrates with OpenAI's ChatGPT model for generating responses and employs PostgreSQL's PGVector technology for efficient response storage and retrieval.

## Features

- AI-driven responses using OpenAI's ChatGPT model
- Efficient response storage and retrieval using PGVector technology
- Response filtering and logging
- User-friendly web interface

## Getting Started

### Prerequisites

- Python (>=3.6)
- PostgreSQL database
- OpenAI API key
- LangChain and related dependencies

### Installation

1. Clone the repository:

   
   git clone https://github.com/your-username/Flask-Langchain-Chatbot.git
   cd Flask-Langchain-Chatbot


2. Install dependencies:
3. Create a PostgreSQL database and configure the config.py file with your database URI and OpenAI API key.
4. Run database migrations:

  ```sh
  python manage.py db init
  python manage.py db migrate
  python manage.py db upgrade

