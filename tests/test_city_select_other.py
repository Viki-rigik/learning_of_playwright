from playwright.sync_api import sync_playwright

def test_city_select_other():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto("https://zoocomplex.com.ua/")
 
       
        page.click(".customer_city__confirmation-btn.customer_city__confirmation-no")
 
     
        page.wait_for_selector("#customerCityModal", timeout=5000)
 
      
        page.click("li.def_city_item:has-text('Київ')")
 
        
        city_data = page.evaluate("window.localStorage.getItem('customerCity')")
        assert "Київ" in city_data, f"Очікувалось 'Київ', але збережено: {city_data}"
 
        browser.close()
