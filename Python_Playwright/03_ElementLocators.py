from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    #launch a new browser 
    browser=playwright.chromium.launch(headless=False,slow_mo=500)
    #Open a new page 
    page=browser.new_page()

    #Navigate to mentioned page
    page.goto ('https://playwright.dev/python/')

    #Locate a link element with "Docs" text
    docs_button=page.get_by_role('Link', name="Docs")
    docs_button.highlight()
    docs_button.click()

    #Close the web browser
    browser.close()