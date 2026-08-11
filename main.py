import json
from pathlib import Path
from src.scraper import SimpleScraper

def main():
    # Target URL for practice (httpbin safely echoes HTML)
    target_url = "https://httpbin.org/html"
    
    print(f"Starting scraper for: {target_url}")
    scraper = SimpleScraper(target_url)
    data = scraper.scrape()
    
    print("\n--- Extracted Data ---")
    print(json.dumps(data, indent=2))
    
    # Optional: Save results to data/ directory
    output_dir = Path("data")
    output_dir.mkdir(exist_ok=True)
    
    output_file = output_dir / "scraped_data.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        
    print(f"\nResults saved to {output_file}")

if __name__ == "__main__":
    main()