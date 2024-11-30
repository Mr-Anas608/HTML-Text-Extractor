# HTML Text Extractor

This Python program is designed to fetch and clean the text content from any given webpage URL. It scrapes all the text in the HTML—whether it's in the title, headers, body, paragraphs, or anywhere else—and returns a clean, readable version.

## How It Works

1. **Fetch HTML Content**  
   The program starts by fetching the raw HTML from the URL you provide.

2. **Remove Unwanted Tags**  
   It then removes non-content elements like JavaScript (`<script>`) and CSS (`<style>`) to ensure the focus is on the main text.

3. **Extract Text**  
   After cleaning up the tags, it strips away all HTML tags, leaving you with the raw text content.

4. **Clean Extra Spaces and Newlines**  
   Finally, the program removes extra spaces, tabs, and newlines to make the output clean and well-formatted.

## Key Features

- **Comprehensive HTML Cleanup**: The program fetches and cleans all the text, no matter where it’s located in the HTML structure.
- **BeautifulSoup & Regex**: The final solution uses **BeautifulSoup** for reliable HTML parsing, but also includes an alternate **regex**-based approach for learning and experimentation.
- **Output**: The program returns a nicely formatted, clean version of the text with minimal spacing and no unnecessary tags.

## How to Use

1. Clone the repository or download the script.
2. Install the required dependencies:
    ```bash
    pip install beautifulsoup4 requests
    ```
3. Run the program by providing the URL you want to extract text from:
    ```python

    Enter URL: "https://www.example.com"

    ```

4. The output will be a clean, readable version of the text from the webpage.

## Why This Approach?

I brainstormed and tried a few different methods to solve this, because there's never just one way to get things done! The final solution uses BeautifulSoup for HTML parsing, ensuring that the process is clean and reliable. But I also included a regex approach to give you some flexibility and options, as sometimes regex can be a great alternative for quick tasks.

This program is all about cleaning up HTML and getting to the core content. It's simple, effective, and easy to use!

## Contributing

Feel free to fork the repository, contribute ideas, or suggest improvements. If you have any enhancements or bug fixes, submit a pull request!

---

Happy coding and exploring the web's data in a cleaner way!
