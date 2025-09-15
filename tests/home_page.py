from playwright.sync_api import sync_playwright

def test_site():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # headless=True, якщо не треба вікно
        page = browser.new_page()

        expected_url = "https://zoocomplex.com.ua"
        page.goto(expected_url)
        page.wait_for_load_state("domcontentloaded")

        assert page.url.startswith(expected_url), f"Очікував {expected_url}, але відкрито {page.url}"

        if page.title() == "Зоомагазин - ZOOcomplex - інтернет-магазин зоотоварів для тварин":
            print("Title відповідає")
        else:
            print(f"Сайт не завантажився, title: {page.title()}")

        browser.close()


if __name__ == "__main__":
    test_site()
            