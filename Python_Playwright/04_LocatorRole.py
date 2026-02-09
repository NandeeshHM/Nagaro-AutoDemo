from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    #launch a browser 
    browser = playwright.chromium.launch(headless=False, slow_mo=1500)
    #Launch a blank page
    page = browser.new_page ()

    #Navigate to mentioned URL 
    page.goto("https://bootswatch.com/default")

    default_button=page.get_by_role('Button',name="Default Button")
    default_button.highlight()