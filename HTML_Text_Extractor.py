"""
This program grabs all the text content from an HTML document fetched from a given URL. 
It pulls text from every corner of the HTML—whether it's in the <title>, headers, body, paragraphs, or any other tag.

How it works:
1. Fetch the raw HTML content from the provided URL.
2. Remove unnecessary <script> and <style> tags (CSS and JavaScript) to focus on the text.
3. Strip all remaining HTML tags to extract only the raw text.
4. Clean up extra spaces, tabs, and newlines for a neat, readable output.

What makes this script cool:
- It offers a clean, reusable solution using BeautifulSoup for parsing and cleaning the HTML.
- It also provides alternative methods (like regex) for experimentation and learning.
- In the end, it gives you a polished way to efficiently extract and format the text.
"""


import requests
import re
from bs4 import BeautifulSoup

def fetch_and_clean_with_bs4(raw_html):
    """Clean HTML using BeautifulSoup."""
    soup = BeautifulSoup(raw_html, 'html.parser')
    for script_or_style in soup(['script', 'style']):
        script_or_style.decompose()
    return re.sub(r'\s+', ' ', soup.get_text()).strip()

def fetch_and_clean_with_regex(raw_html):
    """Clean HTML using regex (alternative method)."""
    remove_script = re.sub(r'<script.*?>.*?</script>', '', raw_html, flags=re.DOTALL)
    remove_style = re.sub(r'<style.*?>.*?</style>', '', remove_script, flags=re.DOTALL)
    text = re.sub('<.*?>', '', remove_style)
    return re.sub(r'\s+', ' ', text).strip()

# Fetching HTML
try:
    url = input("\nEnter Url: ")
    response = requests.get(url, timeout=10)
    raw_html = response.text
except requests.exceptions.RequestException as e:
    print(f"Error fetching the URL: {e}")
    raw_html = ""

# Clean using BeautifulSoup
if raw_html:
    cleaned_text = fetch_and_clean_with_bs4(raw_html)
    print("\nCleaned and Rearranged Text:\n")
    print(cleaned_text)
