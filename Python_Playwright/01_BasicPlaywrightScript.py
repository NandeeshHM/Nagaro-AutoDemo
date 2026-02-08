from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    #Launch a new browser 
    browser = playwright.chromium.launch(headless=False, slow_mo=100)

    #Create a new plan page 
    page = browser.new_page()
    #Visit the playwright page 
    page.goto("https://playwright.dev/python/")

    #Close the bwoser
    browser.close()