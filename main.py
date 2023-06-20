import traceback

from playwright.sync_api import sync_playwright


def main(company_number, employee_id, password):
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False, timeout=0)
            page = browser.new_page()
            page.goto("https://c.timewatch.co.il/punch/punch.php")

            # fill the form
            page.type("#login-comp-input", company_number)
            page.type("#login-name-input", employee_id)
            page.type("#login-pw-input", password)
            page.click("button[type='submit']")

            # wait for the next page
            page.wait_for_load_state("networkidle")
            page.click(".edit-info a.new-link")

            page.wait_for_load_state("networkidle")
            punch_next_available_day(page)

            browser.close()

    except Exception:
        print(traceback.format_exc())


def punch_next_available_day(page):
    days = page.query_selector_all(".table-regular-f tr")
    for day in days:
        columns = day.query_selector_all("td")
        for column in columns:
            column_text = column.text_content()
            if "חסרה כניסה/יציאה" in column_text:
                day_to_punch = day
                day_to_punch.click()
                page.locator("#ehh0").wait_for()

                page.type("#ehh0", "09")  # start time hour
                page.type("#emm0", "30")  # start time minutes
                page.type("#xhh0", "19")  # end time hour
                page.type("#xmm0", "30")  # end time minutes
                page.click(".btn.modal-popup-btn-confirm")
                page.locator("#ehh0").wait_for(state="detached")
                return punch_next_available_day(page)

    print("No more days to punch")


if __name__ == "__main__":
    main(company_number="", employee_id="", password="")
