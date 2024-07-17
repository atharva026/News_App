# [News Application](https://atharvamane02.pythonanywhere.com/)

Welcome to the News Application! This Flask-based web application fetches and displays news articles from various categories and countries using the NewsAPI.

## Features

- Fetches and displays top headlines from India and the US on the main page.
- Allows users to browse news articles by category: Health, Sports, and Technology.
- Provides a search functionality to find news articles based on a keyword.
- Responsive design using Tailwind CSS.

## Technologies Used

- HTML
- Tailwind CSS
- Flask
- Python
- NewsAPI

## Getting Started

Follow these instructions to set up the project on your local machine.

### Prerequisites

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Tailwind CSS](https://tailwindcss.com/)

### API Reference
This application uses the [NewsAPI](https://newsapi.org/) to fetch news articles.

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/atharva026/News_App.git
    ```

2. Navigate to the project directory:

    ```bash
    cd News_App
    ```

3. Install the dependencies:

    ```bash
    pip install flask requests
    ```

4. Get your API key from [NewsAPI](https://newsapi.org/) and add it to the project in `app.py`:

    ```python
    api_key = 'your_api_key_here'
    ```
    
5. Start the Flask application:

    ```bash
    flask run
    ```

## Usage

1. Open your web browser and go to `http://127.0.0.1:5000`.
2. Browse the top headlines from India and the US on the main page.
3. Use the navigation links to view articles by category: Health, Sports, and Technology.
4. Use the search bar to find news articles based on a keyword.

## Contact

For any inquiries or feedback, please reach out to:

- Email: atharvam99@gmail.com

Happy Coding!
