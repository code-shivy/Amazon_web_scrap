##It takes prices from amazon website and tells us if the prices are lower as we require them to be and if they are lower, it sends an reminder..!

############## Things to install before triggering this scrapper ######################
## pip install requests bs4  -- it is used to access a website or an URL (this is called webscrapping) ..!


import requests
from bs4 import BeautifulSoup
import smtplib


## Putting the URL of Samsung galaxy note 10
URL="https://www.amazon.in/Samsung-Galaxy-Storage-Additional-Exchange/dp/B07PRBL6QD/ref=sr_1_1_sspa?crid=3FNZUGATE06TE&keywords=oneplus+7+pro&qid=1566326179&s=gateway&sprefix=one+plus%2Caps%2C555&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzRzhOQlhCRDRYVkk1JmVuY3J5cHRlZElkPUEwMTk2MDg4MVFGSlpRREc3NVkzMCZlbmNyeXB0ZWRBZElkPUEwNzI1MDAzQldWVEdXTjc1WTVCJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="

## entering info about the browser,the user agent of your browser can be searched googling "my user agent" on the browser
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}



def check_price():
    
    page =requests.get(URL,headers=headers)                   ## This returns all the data from the website.

                                                              ## the page will have all the data from the website. hence BeautifulSoup is used to parse it and gather indiviual data from the website..!

    soup=BeautifulSoup(page.content,'html.parser')

    # print(soup.prettify())                                  ## gives us all the elements of the amazon page

    title=soup.find(id="productTitle").get_text()             ## Taking the product name using "productTitle" as this is how the name of the product has been referred to in amazon page

    #print(title.strip())                                     ## To verify that we get the whole span having only product name
    price =soup.find(id="priceblock_ourprice").get_text()     ## The price is obtained same as the product title.
    

    converted_price=(int(price[1:4]))                         ## Takes the first 3 characters from price
    #print(converted_price)
    #print(type(converted_price))
    
    if converted_price < 20:
        send_mail()
        

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()                                             ## establishes a connection between email servers
    server.starttls()                                         ## for connection encryption
    server.ehlo()

    server.login('shivy95lko@gmail.com', 'xkbdkpyibbvujhis')  ## Helps in connecting to your gmail account, It has user name and password as argument.

    subject= "Hey the price fell down"
    body = "Check the amazon link: https://www.amazon.in/Samsung-Galaxy-Storage-Additional-Exchange/dp/B07PRBL6QD/ref=sr_1_1_sspa?crid=3FNZUGATE06TE&keywords=oneplus+7+pro&qid=1566326179&s=gateway&sprefix=one+plus%2Caps%2C555&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzRzhOQlhCRDRYVkk1JmVuY3J5cHRlZElkPUEwMTk2MDg4MVFGSlpRREc3NVkzMCZlbmNyeXB0ZWRBZElkPUEwNzI1MDAzQldWVEdXTjc1WTVCJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail('shivy95lko@gmail.com','golusstyle@gmail.com',msg)
    print('Yay, Email has been sent')

    server.quit()
    


if __name__ == "__main__":
    check_price()
