from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import pandas as pd
import _thread


msg = []


def Twitter():
    try:
        Username = str(input("""====================
Twitter Username: """))
        Password = str(input("""====================
Twitter Password: """))
        opts = webdriver.FirefoxOptions()
        opts.headless = True
        Hash_browser = webdriver.Firefox(options=opts)
        Twitter_browser = webdriver.Firefox("/usr/local/bin")

        def filelookup():
            factstring = ""
            factsdata = pd.read_csv(
                'facts.csv', delimiter='\n', names=['text'])
            greetings = pd.read_csv(
                'greeting.csv', delimiter='\n', names=['text'])
            greetstring = greetings['text'][random.randint(0, 45)]
            factstring = factsdata['text'][random.randint(
                0, (len(factsdata)-1))]
            msg.append(greetstring)
            msg.append(" Did you know: ")
            msg.append(factstring)
            msg.append(" ")

        def time1():
            time.sleep(5)
        def time2():
            time.sleep(7200)

        def processOne(Twitter_browser, Username, Password):
            Twitter_browser.get("https://twitter.com/home")
            time1()
            usr = Twitter_browser.find_element_by_name(
                "session[username_or_email]")
            usr.send_keys(Username)
            password = Twitter_browser.find_element_by_name(
                "session[password]")
            password.send_keys(Password)
            time1()
            loginbtn = Twitter_browser.find_element_by_xpath(
                "/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div")
            loginbtn.click()

        def processOneFinal(Twitter_browser):
            tweetbttn = Twitter_browser.find_element_by_xpath(
                "/html/body/div/div/div/div[2]/header/div/div/div/div[1]/div[3]/a")
            tweetbttn.click()
            time1()
            tweetbodymsg = Twitter_browser.find_element_by_xpath(
                "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div")
            tweetbodymsg.send_keys(msg)

        def processTwo(Hash_browser, Twitter_browser, Username, Password):
            processOne(Twitter_browser, Username, Password)
            Hash_browser.get("https://www.tweeplers.com/hashtags/?cc=WORLD")
            counter = 0
            item = ["item_u_1", "item_u_2", "item_u_3", "item_u_4",
                    "item_u_5", "item_u_6", "item_u_7", "item_u_8"]
            number_history = []
            while counter <= (random.randint(0, 7)):
                number1 = random.randint(0, 7)
                if not(number1 in number_history):
                    number_history.append(number1)
                    msg.append(Hash_browser.find_element_by_id(
                        item[number1]).text)
                    counter += 1
            Hash_browser.quit()
            processOneFinal(Twitter_browser)
        while True:
            time2()
            if (random.randint(0,3) == 1):
                _thread.start_new_thread(filelookup, ())
                _thread.start_new_thread(
                    processTwo, (Hash_browser, Twitter_browser, Username, Password,))
                print("Processing please wait, sometimes this can take 2 mins.")
            else:
                pass
    except:
        Hash_browser.quit()
        Twitter_browser.quit()
        print("error with your login or internet.")




def Menu():
    while True:
        try:
            timE = time.ctime(time.time())
            choice = int(input(f"""------------------------
Welcome to this demonstration, half of this program has been deleted.
{timE}
Menu:
1. Project start
3. Quit
------------------------
Your choice: """))
            if choice == 1:
                Twitter()
            elif choice == 3:
                break
            else:
                print(f"{choice} is not a choice.")
        except:
            print("error with your input")


Menu()
