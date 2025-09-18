from playwright.sync_api import sync_playwright
import time

def test_phone_input():
    test_numbers = [
        "+380671234567",       
        "+38067",              
        "0671234567",          
        "+38067abc4567",      
        "+38 (067) 123-45-67"  
    ]

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        for number in test_numbers:
           
            page.goto("https://zoocomplex.com.ua/")
            time.sleep(1) 

     
            page.click(".header-account__icon.far.fa-user")
            page.wait_for_selector("#zoo-modal-auth", timeout=5000)

          
            if page.locator("#zoo-wide-view").is_visible():
                modal_container = page.locator("#zoo-wide-view")
                phone_selector = "#zoo-phone-input-wide"
                send_btn_selector = "#zoo-send-code-btn-wide"
            elif page.locator("#zoo-narrow-view").is_visible():
                modal_container = page.locator("#zoo-narrow-view")
                phone_selector = "#zoo-phone-input-narrow"
                send_btn_selector = "#zoo-send-code-btn-narrow"
            else:
                print("Модальное окно не найдено!")
                continue

            phone_input = modal_container.locator(phone_selector)
            send_btn = modal_container.locator(send_btn_selector)
            error_block = modal_container.locator("#zoo-modal-error")

            phone_input.fill(number)
            send_btn.click()
            time.sleep(0.5)  

        
            error_text = error_block.inner_text().strip()
            if error_text:
                print(f"{number} — ❌ НЕ ПРИНЯТ, ошибка: {error_text}")
            else:
                print(f"{number} — ✅ ПРИНЯТ")

        browser.close()

test_phone_input()
