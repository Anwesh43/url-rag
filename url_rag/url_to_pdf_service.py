from playwright.sync_api import sync_playwright


class URLToPdfService:

    @staticmethod
    def urlToPdf(url: str, input: str):
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(url)
            page.pdf(path=input, format='A4', landscape=False)
            browser.close()
