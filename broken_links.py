import requests
from bs4 import BeautifulSoup
import csv
import time
from urllib.parse import urljoin, urlparse
from tqdm import tqdm

# Configuration
BASE_URL = "https://odcm.hannesdatta.com"  # Change this to the website you want to crawl
OUTPUT_FILE = "broken_links.csv"
CRAWLED_PAGES = set()  # Track crawled pages to avoid loops
BROKEN_LINKS = []  # Store broken links

def get_links_from_page(url):
    """Extract all links from a given page."""
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except requests.RequestException:
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    links = set()
    for link in soup.find_all("a", href=True):
        full_url = urljoin(url, link["href"])
        if is_same_domain(full_url):
            links.add(full_url)
    return links

def is_same_domain(url):
    """Check if URL belongs to the same domain."""
    return urlparse(url).netloc == urlparse(BASE_URL).netloc

def check_link_status(url):
    """Check if a URL is broken."""
    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        if response.status_code >= 400:
            return response.status_code
    except requests.RequestException:
        return "Failed"
    return None

def crawl_site(url):
    """Recursively crawl site and check for broken links."""
    if url in CRAWLED_PAGES:
        return
    CRAWLED_PAGES.add(url)

    print(f"Crawling: {url}")
    links = get_links_from_page(url)
    
    for link in tqdm(links, desc="Checking links", unit="link"):
        status = check_link_status(link)
        if status:
            BROKEN_LINKS.append((url, link, status))
    
    # Recursively crawl internal links
    for link in links:
        if link not in CRAWLED_PAGES:
            time.sleep(1)  # Be polite to the server
            crawl_site(link)

def save_results():
    """Save broken links to a CSV file."""
    with open(OUTPUT_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Page", "Broken Link", "Status Code"])
        writer.writerows(BROKEN_LINKS)
    print(f"Results saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    print("Starting crawl...")
    crawl_site(BASE_URL)
    save_results()
    print("Done!")
