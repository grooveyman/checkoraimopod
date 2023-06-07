import datetime
import requests
import os
from bs4 import BeautifulSoup
from tkinter import *
from winotify import Notification, audio

toast = Notification(app_id="Oraimo Checker", title="Oraimo Pod Availability"
                     ,msg="oraimo FreePods 3 TWS True Wireless Stereo Earbuds is now avalable",
                     duration="long",
                     icon=rf"{os.getcwd()}\oraimo.png")
toast.set_audio(audio.Default, loop=False)

toast.add_actions(label="Order Now!", launch="https://gh.oraimo.com/oraimo-freepods-3-true-wireless-earbuds.html")



file = open(rf'{os.getcwd()}\task.txt', 'a') #a option is for append


url = "https://gh.oraimo.com/oraimo-freepods-3-true-wireless-earbuds.html"
response = requests.get(url)

content = response.content
parsed_content = BeautifulSoup(content, 'html.parser')
main_content = parsed_content.find("span", {"itemprop":"name"}).get_text()

if(main_content == 'oraimo FreePods 3 TWS True Wireless Stereo Earbuds'):
    stock = parsed_content.find("button",{"id":"product-addtocart-button"}).findNext("span").get_text()
    if(stock.lower() != "Out of Stock".lower()):
        #show notification
        toast.show()
        file.write(f'{datetime.datetime.now()} - Available Now \n')
    else:
        file.write(f'{datetime.datetime.now()} - Not available \n')
