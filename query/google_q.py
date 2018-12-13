from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Query:

    def __init__(self):
        pass

    @staticmethod
    def ask_google(query):
        chrome_options = Options()
        chrome_options.add_argument("--window-size=1024x768")
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(chrome_options=chrome_options)

        query = query.replace(' ', '+')
        driver.get('http://www.google.com/search?q=' + query)
        __response = driver.execute_script(
            "return document.elementFromPoint(arguments[0], arguments[1]);",
            350, 230).text

        return __response
