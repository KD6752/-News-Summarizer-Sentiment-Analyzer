# News-Summarizer-Sentiment-Analyzer

This is AI-powered news summariser and sentiment analyser of those news content.

AI Powered News Summarizer &amp; Sentiment Analyzer

## local enviroment

python3 -m venv analyser_bot

## activate enroment

source analyser_bot/bin/activate

## install the requirements

pip install -r requirements.txt

### Step 1: In this step it scrape the news from newsapi.org

### Step 2:Inthis step, it uses the contents from step 1 and summarise it using transformer using model "facebook/bart-large-cnn"

### Step 3: In this step it analyse the content perform sentiment analysis provide sentiment analysis out of 5 stars.

### Step 4: In this step is to make a UI using Streamlit where I make a normal UI to view content title, its link, its summary view and its senstiment analysis score.
