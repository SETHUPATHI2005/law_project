
Built by https://www.blackbox.ai

---

```markdown
# Indian Constitution AI Assistant

## Project Overview

The Indian Constitution AI Assistant is a web application that provides users with access to the Indian Constitution through an AI-powered interface. Users can search articles and ask legal questions related to the Constitution. This project combines modern web technologies with AI functionalities to offer a user-friendly experience for legal inquiries.

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/indian-constitution-ai.git
    cd indian-constitution-ai
    ```

2. **Set up a virtual environment** (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies**:

    Make sure you have `Flask` and `python-dotenv` installed. You can use pip to install them:

    ```bash
    pip install Flask python-dotenv openai
    ```

4. **Set up environment variables**:

    Create a `.env` file in the root directory of the project and add your OpenAI API key:

    ```bash
    OPENAI_API_KEY=your-api-key-here
    ```

5. **Prepare the constitution data**:

    Make sure to have the `constitution.json` file in the `data` directory, containing your constitution data.

6. **Run the application**:

    You can start the application using the following command:

    ```bash
    python wsgi.py
    ```

    The application will be available at `http://127.0.0.1:5000/` by default.

## Usage

Once the application is running, you can:

- Search for articles of the Indian Constitution using the search box.
- Ask legal questions about the Constitution, and get AI-powered responses.

## Features

- **Article Search**: Quickly find articles by entering search terms.
- **AI Legal Assistant**: Interact with an AI that can provide explanations and answers based on the Indian Constitution.
- **Responsive Design**: Built using Tailwind CSS, the application functions well on various screen sizes.

## Dependencies

The following dependencies are used in this project:

- Flask: A lightweight WSGI web application framework.
- python-dotenv: Helps in loading environment variables from a `.env` file.
- openai: Provides the OpenAI API client for Python.

## Project Structure

The project has the following structure:

```
indian-constitution-ai/
├── app.py                  # Main Flask application logic
├── data/                   # Directory containing constitution data (includes constitution.json)
│   └── constitution.json
├── index.html              # HTML template for the frontend
├── .env                    # Environment variables file (not included in version control)
├── wsgi.py                 # Entry point for the web server
└── README.md               # Project documentation
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This application is not intended to provide legal advice. For legal matters, please consult a qualified lawyer.
```