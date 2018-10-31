from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pyttsx3
import json

chrome_options = Options()
chrome_options.add_argument("--window-size=1024x768")
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options)


def ask_google(query):

    query = query.replace(' ', '+')
    driver.get('http://www.google.com/search?q=' + query)
    answer = driver.execute_script(
            "return document.elementFromPoint(arguments[0], arguments[1]);",
            350, 230).text

    return answer


question = input("Please ask me a question> ")
variable = ask_google(question)
stringify = str(variable)
print("The question is: %s \n" % question)
print(stringify)

data = json.dumps(variable)
print(data)


engine = pyttsx3.init()
engine.setProperty("voice", 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
engine.setProperty('rate', 140)

engine.say(stringify)
engine.runAndWait()


class Query:
    response = ""

    def __init__(self):
        pass

    def ask_google(self, query):

        __response = ""
        self.response = __response
        return __response
    

