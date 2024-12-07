from bs4 import BeautifulSoup

def parse(page_content):
    """Parse the HTml content and get info."""
    soup = BeautifulSoup(page_content , "html.parser")
    titles = soup.find_all("h1") # Find All Html Tag just for e.g
    for title in titles:
        print(f"Title: {title.text}")