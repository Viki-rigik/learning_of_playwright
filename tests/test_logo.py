import pytest
from playwright.sync_api import Playwright, expect

BASE_URL = "https://zoocomplex.com.ua/"

def test_logo(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    page.goto(BASE_URL)

    try:
        modal_button = page.get_by_role("button", name="Ні")
        if modal_button.is_visible():
            modal_button.click()
    except:
        pass 

    logo = page.get_by_role("img", name="Зоомагазин ZooComplex")

    expect(logo).to_be_visible()
    print("✅ Логотип видим")

    alt = logo.get_attribute("alt")
    assert alt and alt.strip() != "", "У логотипа пустой alt"
    print(f"✅ Атрибут alt: {alt}")

    natural_width = page.evaluate("el => el.naturalWidth", logo.element_handle())
    assert natural_width > 0, "Логотип не загрузился (naturalWidth=0)"
    print(f"✅ Логотип загрузился, naturalWidth={natural_width}")

    logo.click()
   
    assert page.url.startswith(BASE_URL), f"Клик по логотипу не ведёт на главную, url={page.url}"
    print(f"✅ Клик по логотипу ведёт на главную: {page.url}")

    context.close()
    browser.close()
