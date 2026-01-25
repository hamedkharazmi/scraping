import os
from playwright.sync_api import sync_playwright
import csv

# --------------------------
# CONFIG
# --------------------------
START_ID = 1       # starting activation ID
END_ID = 100        # ending activation ID
OPEN_BROWSER_UI = True

os.makedirs("output", exist_ok=True)
OUTPUT_FILE = "output/activation_data.csv"

# --------------------------
# SCRAPER
# --------------------------
def scrape_activation_pages():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=not OPEN_BROWSER_UI)
        context = browser.new_context(storage_state="auth.json")
        page = context.new_page()

        # Open CSV file to save results
        with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([
                "activation_id", "deal_text", "header_text",
                "link_text", "link_href", "full_text"
            ])

            for activation_id in range(START_ID, END_ID + 1):
                url = f"https://www.joinsecret.com/activation/{activation_id}"
                print(f"\nProcessing {url} ...")

                try:
                    page.goto(url, wait_until="domcontentloaded")

                    p_tag = page.query_selector('div.instruction-card div[data-spec="merle"] p a')
                    
                    if p_tag:
                        # -------------------
                        # Extract deal text
                        deal_el = page.query_selector('div.instruction-card .flex > div > p.custom-text-lg')
                        deal_text = deal_el.inner_text() if deal_el else ""

                        # Extract header text
                        header_el = page.query_selector('div.instruction-card .flex > div > p.header-xl')
                        header_text = header_el.inner_text() if header_el else ""

                        # Extract main <p> with link
                        # p_tag = page.query_selector('div.instruction-card div[data-spec="merle"] p a')
                        if p_tag:
                            link_href = p_tag.get_attribute("href")
                            link_text = p_tag.inner_text()
                            full_text = p_tag.evaluate("node => node.parentElement.innerText")
                        else:
                            link_href = ""
                            link_text = ""
                            full_text = ""

                        # Save row
                        writer.writerow([activation_id, deal_text, header_text, link_text, link_href, full_text])
                        print(f"Saved: {deal_text} | {header_text} | {full_text[:50]}...")

                except Exception as e:
                    print(f"Error on {url}: {e}")

        print("\nScraping finished. Browser closed.")
        browser.close()


if __name__ == "__main__":
    scrape_activation_pages()
