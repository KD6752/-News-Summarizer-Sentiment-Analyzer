import requests
import os

from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

# Access the API key
NEWS_API_KEY = os.getenv("NEWS_API_KEY")


NEWS_API_URL = f"https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey={NEWS_API_KEY}"

def fetch_news():
    response = requests.get(NEWS_API_URL)
    news_data = response.json()
    articles = news_data.get("articles", [])
    return [{"title": art["title"], "content": art["content"], "url": art["url"]} for art in articles]
    return [{"title": art["title"], "content": art["content"], "url": art["url"]} for art in articles]

from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_article(article_text):
    if not article_text or not isinstance(article_text, str):  
        return "No content available to summarize."
    summary = summarizer(article_text, max_length=150, min_length=50, do_sample=False)
    return summary[0]['summary_text']



sentiment_analyzer = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

def analyze_sentiment(article_text):
    if not article_text or not isinstance(article_text, str):  
        return "No content available for sentiment analysis."

    sentiment = sentiment_analyzer(article_text[:512])  # Limit text length
    return sentiment[0]['label']


import streamlit as st

st.title("📰 AI-Powered News Summarizer & Sentiment Analyzer")

if st.button("Fetch Latest News"):
    articles = fetch_news()
    
    for article in articles:
        st.subheader(article['title'])
        st.write("🔗", article['url'])
        
        with st.spinner("Summarizing..."):
            summary = summarize_article(article['content'])
        st.write("📌 **Summary:**", summary)
        
        with st.spinner("Analyzing Sentiment..."):
            sentiment = analyze_sentiment(article['content'])
        st.write("🔍 **Sentiment:**", sentiment)
        
        st.markdown("---")
