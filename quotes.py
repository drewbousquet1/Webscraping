from bs4 import BeautifulSoup
import requests
import pandas as pd
import plotly.express as px

def scrape_quotes(base_url, pages):
    """Scrape quotes from the given base_url for the specified number of pages."""
    all_quotes = []
    
    with requests.Session() as session:
        for page in range(1, pages + 1):
            response = session.get(f"{base_url}/page/{page}/")
            soup = BeautifulSoup(response.text, 'html.parser')
            quotes = soup.find_all('div', class_='quote')

            for quote in quotes:
                text = quote.find('span', class_='text').get_text(strip=True)
                author = quote.find('small', class_='author').get_text(strip=True)
                tags = [tag.get_text(strip=True) for tag in quote.find_all('a', class_='tag')]
                
                all_quotes.append({
                    'text': text,
                    'author': author,
                    'tags': tags,
                    'text_length': len(text)
                })
    
    return pd.DataFrame(all_quotes)

def analyze_author_data(df):
    """Analyze the author data from the quotes DataFrame."""
    author_stats = df['author'].value_counts()
    most_quotes = author_stats.idxmax()
    least_quotes = author_stats.idxmin()

    return author_stats, most_quotes, least_quotes

def analyze_quote_data(df):
    """Analyze the quote data from the quotes DataFrame."""
    average_length = df['text_length'].mean()
    longest_quote = df.loc[df['text_length'].idxmax()]['text']
    shortest_quote = df.loc[df['text_length'].idxmin()]['text']

    return average_length, longest_quote, shortest_quote

def analyze_tags(df):
    """Analyze tag data from the quotes DataFrame."""
    tag_counts = df.explode('tags')['tags'].value_counts()
    most_popular_tag = tag_counts.idxmax()
    total_tags = tag_counts.sum()

    return tag_counts, most_popular_tag, total_tags

def plot_top_authors(author_stats):
    """Plot the top 10 authors based on the number of quotes."""
    top_authors = author_stats.head(10)
    fig = px.bar(top_authors, x=top_authors.index, y=top_authors.values, title="Top 10 Authors by Number of Quotes")
    fig.show()

def plot_top_tags(tag_counts):
    """Plot the top 10 tags based on popularity."""
    top_tags = tag_counts.head(10)
    fig = px.bar(top_tags, x=top_tags.index, y=top_tags.values, title="Top 10 Tags by Popularity")
    fig.show()

df = scrape_quotes("http://quotes.toscrape.com", 10)
author_stats, most_quotes, least_quotes = analyze_author_data(df)
avg_len, long_quote, short_quote = analyze_quote_data(df)
tag_counts, popular_tag, total_tags = analyze_tags(df)
plot_top_authors(author_stats)
plot_top_tags(tag_counts)

