
from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    #Launch the browser 
    browser = playwright.chromium.launch(headless=False,slow_mo=500)

    #open a new page
    page = browser.new_page()
    #go to the menstioned url 
    page.goto('https://playwright.dev/python/')

    #Locate a link element with "Docs" text
    docs_button=page.get_by_role('Link', name="Docs")
    docs_button.click()

    #Get the page URL
    print("Docs:", page.url)

    release_notes=page.get_by_role('Link',name="Release notes")
    release_notes.click()

    #close the browser 
    browser.close()
