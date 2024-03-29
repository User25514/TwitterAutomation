from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import pandas as pd
import _thread
import os


class TwitterBot():
    class Twitter():

        def time1(self):
            time.sleep(2)
        def time2(self):
            time.sleep(random.randint(7789,14256))

        def Login(self,Twitter_browser,dicT):
            Twitter_browser.get("https://TwitterBot.Twitter.com/home")
            TwitterBot.Twitter.time1(0)
            usr = Twitter_browser.find_element_by_name(
                "session[username_or_email]")
            usr.send_keys(dicT["Username"])
            password = Twitter_browser.find_element_by_name(
                "session[password]")
            password.send_keys(dicT["Password"])
            TwitterBot.Twitter.time1(0)
            loginbtn = Twitter_browser.find_element_by_xpath(
                "/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div")
            loginbtn.click()
            dicT["Stage3"] = "complete"

        def Tweet(self,Twitter_browser):
            tweetbttn = Twitter_browser.find_element_by_xpath(
                "/html/body/div/div/div/div[2]/header/div/div/div/div[1]/div[3]/a")
            tweetbttn.click()
            TwitterBot.Twitter.time1(0)
            tweetbodymsg = Twitter_browser.find_element_by_xpath(
                "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div")
            tweetbodymsg.send_keys(msg)
            tweetSendbttn = Twitter_browser.find_element_by_xpath(
                "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[4]/div/div/div[2]/div[4]/div")
            tweetSendbttn.click()
            
        def Register(self,dicT):
            opts = webdriver.FirefoxOptions()
            opts.headless = True
            Hash_browser = webdriver.Firefox(options=opts)
            Twitter_browser = webdriver.Firefox("/usr/local/bin")
            _thread.start_new_thread(TwitterBot.File.filelookup, (0,dicT,))
            _thread.start_new_thread(TwitterBot.Hash.getTags, (0,Hash_browser,dicT,))
            _thread.start_new_thread(TwitterBot.Twitter.Login, (0,Twitter_browser,dicT,))
            print("Processing please wait, sometimes this can take 2 mins.")
            while True:
                if ((dicT["Stage1"] == "complete") and (dicT["Stage2"] == "complete") and (dicT["Stage3"] == "complete")):
                    TwitterBot.Twitter.time1(0)
                    TwitterBot.Twitter.Tweet(0,Twitter_browser)
                    print("Successfully Tweeted")
                    break
                else:
                    pass
                time.sleep(1)
                os.system('clear')
                print("File Stage: {}\nHashes gathered: {}\nLogin: {}".format(dicT["Stage1"],dicT["Stage2"],dicT["Stage3"]))

    class File():
        def filelookup(self,dicT):
            factstring = ""
            factsdata = pd.read_csv(
                'facts.csv', delimiter='\n', names=['text'])
            greetings = pd.read_csv(
                'greeting.csv', delimiter='\n', names=['text'])
            greetstring = greetings['text'][random.randint(0, (len(greetings['text'])-1))]
            factstring = factsdata['text'][random.randint(0, (len(factsdata)-1))]
            msg.append(greetstring)
            msg.append(" Did you know: ")
            msg.append(factstring)
            msg.append(" ")
            dicT["Stage1"] = "complete"

    class Hash():
        def getTags(self,Hash_browser, dicT):
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
            dicT["Stage2"] = "complete"


    def Menu(self):
        
        while True:
            try:
                timE = time.ctime(time.time())
                choice = int(input(f"""------------------------
    {timE}
    Menu:
    1. Demonstration
    2. Tweet every 2-4 hours
    3. Quit
    ------------------------
    Your choice: """))
                if choice == 1:
                    dicT = {
                        "Username" : "",
                        "Password" : "",
                        "Stage1" : "un-complete",
                        "Stage2" : "un-complete",
                        "Stage3" : "un-complete"
                    }
                    dicT["Username"] = str(input("""====================\nTwitter Username: """))
                    dicT["Password"] = str(input("""====================\nTwitter Password: """))
                    TwitterBot.Twitter.Register(0,dicT)
                elif choice == 2:
                    dicT = {
                        "Username" : "",
                        "Password" : "",
                        "Stage1" : "un-complete",
                        "Stage2" : "un-complete",
                        "Stage3" : "un-complete"
                    }
                    dicT["Username"] = str(input("""====================\nTwitter Username: """))
                    dicT["Password"] = str(input("""====================\nTwitter Password: """))
                    while True:
                        TwitterBot.Twitter.time2(0)
                        TwitterBot.Twitter.Register(0,dicT)
                elif choice == 3:
                    break
                else:
                    print(f"{choice} is not a choice.")
            except:
                print("error with your input")
os.system('clear')
TwitterBot.Menu(0)
os.system('clear')