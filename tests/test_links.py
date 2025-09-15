from playwright.sync_api import sync_playwright

def test_top_links():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
 
        page.goto("https://zoocomplex.com.ua/")
 
        expected_links = {
            "Про нас": "/ua-about_us/",
            "Послуги грумінгу": "/ua-uslugi-gruminga/",
            "Наш застосунок": "/app/",
            "Наші магазини": "/ua-contact-us/"
        }
 
        all_passed = True  # флаг, чтобы увидеть общий результат теста

        for title, href in expected_links.items():
            link = page.locator(f"a.top-links__a[title='{title}']")
            
            visible = link.is_visible()
            actual_href = link.get_attribute("href")
            
            if visible and actual_href == href:
                print(f"✅ Лінк '{title}' відображається правильно з href '{actual_href}'")
            else:
                all_passed = False
                if not visible:
                    print(f"❌ Лінк '{title}' не відображається")
                if actual_href != href:
                    print(f"❌ Невірний href для '{title}': очікувалося '{href}', отримано '{actual_href}'")
        
        if all_passed:
            print("\n🎉 Всі лінки перевірені успішно!")
        else:
            print("\n⚠️ Є помилки в перевірці лінків")

        browser.close()

# Запуск теста
if __name__ == "__main__":
    test_top_links()