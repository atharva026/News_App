from flask import Flask, render_template, request
import requests

app = Flask(__name__)

api_key = 'YOUR_API_KEY'
URL = 'https://newsapi.org/v2/top-headlines'

def fetchNews(country=None, category=None, query=None, page_size=30 ):
    params = {
        'apiKey': api_key,
        'language': 'en',
        'pageSize':page_size
    }
    if country:
        params['country'] = country
    if category:
        params['category'] = category
    if query:
        params['q'] = query

    response = requests.get(URL, params=params)
    # print(f"Request URL: {response.url}")  # Log the request URL
    if response.status_code == 200:
        data = response.json()
        # print(f"Response: {data}")  # Log the response data
        return data.get('articles', [])
    else:
        # print(f"Failed to fetch news: {response.status_code}")
        return []

# Main Page
@app.route('/')
def index():
    india_articles = fetchNews(country='in', page_size=15)
    us_articles = fetchNews(country='us', page_size=15)
    articles=india_articles + us_articles
    return render_template('index.html',  articles=articles)

@app.route("/health")
def health():
    articles = fetchNews(category="health", page_size=30)
    return render_template('index.html', articles=articles)

@app.route("/sports")
def sports():
    articles = fetchNews(category="sports", page_size=30)
    return render_template('index.html', articles=articles)

@app.route("/technology")
def technology():
    articles = fetchNews(category="technology", page_size=30)
    return render_template('index.html', articles=articles)     

@app.route("/search", methods=['POST'])
def search():
    if request.method == 'POST':
        title = request.form.get('title')
        if title:
            articles = fetchNews(query=title, page_size=30)
            return render_template('index.html', articles=articles)
        else:
            return []

if __name__ == "__main__": 
    app.run(debug=True)
