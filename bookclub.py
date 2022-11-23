# Initial imports

from pathlib import Path
import pandas as pd
import json
from urllib.request import urlopen
import webbrowser

# Set the file path and reading CSV into a DataFrame

csvpath = Path("books.csv")
books_df = pd.read_csv(csvpath, on_bad_lines='skip')

# Get rid of irrelevant columns
books_df = books_df.iloc[:,[1,2,3,4,6,7,10]]
# Get a randomized row from the DataFrame
while True:
    # Filter out books with higher average rating
    df = books_df[books_df["average_rating"] > 4.00]
    #Filter out english language
    df = df[df["language_code"] == "eng"]
    # Randomly select a book from the DataFrame
    df_sample = df.sample()
    print(df_sample)

    # Initiate Google Books API
    api = "https://www.googleapis.com/books/v1/volumes?q=isbn:"

    # Use Isbn to locate a previously selected book
    isbn = df_sample.iloc[0,3]
    
    # Send a request and get a JSON response
    resp = urlopen(api + isbn)

    # Parse JSON into Python as a dictionary
    book_data = json.load(resp)

    # Redirect to Google Books website
    volume_info = book_data["items"][0]["volumeInfo"]
    book_link = volume_info['previewLink']
    webbrowser.open(book_link) 

    break


