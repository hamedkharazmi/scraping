from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()  # ⬅️ NO auth.json yet
    page = context.new_page()

    page.goto("https://www.joinsecret.com", wait_until="domcontentloaded")

    print("👉 Log in manually, then press ENTER here")
    input()

    context.storage_state(path="auth.json")
    browser.close()