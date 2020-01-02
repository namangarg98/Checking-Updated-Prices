print("Hello I am here")
import requests
from bs4 import BeautifulSoup
import smtplib


url = "https://www.amazon.in/Patanjali-Cows-Ghee-1L/dp/B01DKPA876/ref=sr_1_3?keywords=patanjali+ghee&qid=1576919643&sr=8-3"

headers = {"User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0'}

def check_price():
    page = requests.get(url , headers = headers)

    soup = BeautifulSoup(page.content , 'html.parser')

    #Extracting the name of the product
    title = soup.find(id = "productTitle").get_text()
    price = soup.find(id = "priceblock_ourprice").get_text()
    converted_price = float(price[2:5])

    if(converted_price <= 530.0):
        send_mail()

    print(converted_price)
    print(title.strip())


def send_mail():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("namangarg753@gmail.com", "namangarg619")

    subject = "price fell down"
    body = "Please check the amazon link for updated price : https://www.amazon.in/Patanjali-Cows-Ghee-1L/dp/B01DKPA876/ref=sr_1_3?keywords=patanjali+ghee&qid=1576919643&sr=8-3"
    msg = f"subject: {subject}\n\n{body}"

    server.sendmail(
        'namangarg753@gmail.com',
        'ashutosh.dumiyan@gmail.com',
        msg
    )
    print("Email has been sent")

    server.quit()

check_price()