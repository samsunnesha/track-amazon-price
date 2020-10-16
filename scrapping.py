import requests
from bs4 import BeautifulSoup
import smtplib
URL='product URL'

headers = {"User Agent":'your user agent'} #go to google.com and search 'my user agent'

page = requests.get(URL, headers=headers)

soup= BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())

title = soup.find(id="title_feature_div").get_text() #product title id in html console of amazon product page
price = soup.find(id="priceblock_ourprice_row").get_text() #product price id in html console of amazon product page
converted_price = float(price[0:5])

if(converted_price > 1.700):
    send_mail()
print(converted_price)
print(title.strip())

if(converted_price > 1.700):
    send_mail()





def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('your email address')

    subject = 'price fell down'

    body = 'check the amazon link product link'


    msg  = f"Subject: {subject}\n\n{body}"

    server.send_mail(
        'your email address',#from
        'another mail address', #to
        msg
    )

    print('HEY EMAIL HAS BEEN SEND')
    server.quit()


check_price()


