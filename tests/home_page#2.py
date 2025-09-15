from playwright.sync_api import sync_playwright

def test_site():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        page=browser.new_page()

        expected_url="https://zoocomplex.com.ua"
        page.goto(expected_url)
        page.wait_for_load_state("domcontentloaded")

        assert page.url.startswith(expected_url), f"Очікував {expected_url}, але відкрилося {page.url}"

        if page.title() == "Зоомагазин - ZOOcomplex - інтернет-магазин зоотоварів для тварин":
            print("вірно")
        else:
            print(f"не вірно, title: {page.title()}")

        browser.close()

if __name__ == "__main__":
    test_site()            






    