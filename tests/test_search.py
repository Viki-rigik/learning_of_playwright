import time
from playwright.sync_api import Playwright, sync_playwright

SEARCH_TEXT = "корм"

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://zoocomplex.com.ua/")

    page.locator("#search-init").click()

    search_input = page.locator("#multisearch")
    search_input.wait_for(state="visible", timeout=5000)

    search_input.fill("корм")

    page.locator("#search-modal button").click()

    time.sleep(3)

    page.screenshot(path="search_results.png", full_page=True)
    print("Скриншот сохранён: search_results.png")

    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
