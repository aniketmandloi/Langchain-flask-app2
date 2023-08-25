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

        pip install -r requirements.txt

3.Create a PostgreSQL database and configure the config.py file with your database URI and OpenAI API key.

4.Run database migrations:

        python manage.py db init
        python manage.py db migrate
        python manage.py db upgrade

## Usage

1. Start the Flask development server:

        python main.py

2. Access the web interface in your browser at http://localhost:5000.

3. Enter your queries and interact with the AI-driven chatbot. Responses will be displayed on the web page.

## Configuration
Update the config.py file to configure the application settings. You need to provide the following information:

1. SECRET_KEY: Secret key for session management.
2. SQLALCHEMY_DATABASE_URI: PostgreSQL database URI.
3. OPENAI_API_KEY: Your OpenAI API key.

## Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and ensure tests pass.
4. Open a pull request.

Please refer to the CONTRIBUTING.md file for more information.

## License

This project is licensed under the MIT License. See the LICENSE file for details.


    Copy the above markdown content and paste it into your project's `README.md` file. Modify any placeholders such as `aniketmandloi` and ensure that the content fits your project structure and details accurately.




