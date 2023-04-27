import openai
import pandas as pd
import requests
import re
import csv
from bs4 import BeautifulSoup
from config import CHATGPT_KEY

openai.api_key = CHATGPT_KEY


def read_file(file):
    """
    Reads the database, ignores junk, and retrieves valid URLs.

    Returns a dictionary containing the valid URLs.
    """
    final_urls = {}
    file = pd.read_csv(file)
    for row_number, row in file.iterrows(): # used ChatGPT to learn about iterrows()
        try:
            url = row["link"]
            if url.startswith("http:") or url.startswith("https:") or url.startswith("www."): # used ChatGPT to remember startswith()
                final_urls[row_number] = url
        except:
            continue
    return final_urls


def scrape_website(url):
    """
    Accesses a specific URL and cleans all the information on the page for later implementation.

    Returns a string variable that contains the cleaned content of the URL.
    """
    link = requests.get(url)
    website_content = link.text
    website_content = BeautifulSoup(website_content, "html.parser").get_text() 
    website_content = re.sub(r"\n\s*\n", "\n", website_content) # learned about re library as part of my special assignment research
    return website_content # important to overwrite variable so many times due to space considerations


def summarize(text):
    """
    Uses ChatGPT API to summarize the contents of a string text entry

    Returns the generated summary
    """
    # used ChatGPT incrementally to test/debug this process; tested several methods of adjusting the prompt - I found that less is more
    prompt = "You are an unbiased person who does not reference unneeded information. Only use the information provided. Please summarize this recall:" + text
    summary = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])
    summary = summary["choices"][0]["message"]["content"]
    return summary


def store_summary(text, file, action = "a", encoding="utf-8"): # encoding added to prevent import related error
    """
    Stores the ChatGPT summaries into a new file
    """
    with open(file, action, encoding=encoding, newline="") as csvfile:
        writer = csv.writer(csvfile)
        for summary in text.split("\n"):
            writer.writerow([summary])


def summaries_creation(file):
    """
    Reads a database CSV file, cleans the file and scrapes cleaned web output to store in a variable, uses ChatGPT to summarize the variable and output to new file

    Prints a notification that all entries have generated
    """
    print("Generating the individual summaries:")
    database_urls = read_file(file)
    counter = 1
    for database_url in database_urls.values():
        output = scrape_website(database_url)
        output = summarize(output)
        store_summary(output, "demo_summaries.csv")
        print(f"Entry #{counter} complete")
        counter += 1
    print("All entries have completed")


def main():
    database = "demo_recalls.csv"
    summaries_creation(database)


if __name__ == "__main__":
    main()
