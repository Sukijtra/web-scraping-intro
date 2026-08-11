import requests
from bs4 import BeautifulSoup
from typing import Optional, Dict, Any

class SimpleScraper:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()
        # Custom User-Agent header to avoid basic scraping blocks
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        })

    def fetch_page(self, url: str) -> Optional[str]:
        """Fetch the HTML content of a given URL."""
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"[ERROR] Failed to fetch {url}: {e}")
            return None

    def parse_title(self, html_content: str) -> Optional[str]:
        """Extract the main title/heading from the page HTML."""
        soup = BeautifulSoup(html_content, "html.parser")
        
        # Priority: h1 tag -> title tag -> fallback None
        h1 = soup.find("h1")
        if h1:
            return h1.get_text(strip=True)
            
        title = soup.find("title")
        if title:
            return title.get_text(strip=True)
            
        return None

    def scrape(self) -> Dict[str, Any]:
        """Main orchestrator for scraping data."""
        html = self.fetch_page(self.base_url)
        if not html:
            return {"url": self.base_url, "title": None, "status": "failed"}

        title = self.parse_title(html)
        return {
            "url": self.base_url,
            "title": title,
            "status": "success"
        }