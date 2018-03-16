from selenium import webdriver
from selenium.webdriver.support.ui import Select
import datetime

def checkKeywords(keywords, description):
    for i in keywords:
        if i not in description:
            return False
    return True

def searchArticle(browser, category, keywords, color):    
    print("[*] Searching Article ...")
    browser.get("http://www.supremenewyork.com/shop/all/" + category)
    links = browser.find_elements_by_class_name("name-link")

    i = 0
    while i < len(links):
        if (checkKeywords(keywords, links[i].text) & (color in links[i+1].text)):
            print("Description : " + links[i].text)
            print("Color : " + links[i+1].text)
            links[i].click()
            print("[+] Article found")
            return True
        i += 2
    print("[-] Article not found")
    return False

def fillForm(browser, datas):
    # Fill name
    name = browser.find_element_by_name("order[billing_name]")
    name.send_keys(datas["order[billing_name]"])
    
    # Fill email
    email = browser.find_element_by_name("order[email]")
    email.send_keys(datas["order[email]"])

    # Fill tel
    tel = browser.find_element_by_name("order[tel]")
    tel.send_keys(datas["order[tel]"])

    # Fill address
    address = browser.find_element_by_name("order[billing_address]")
    address.send_keys(datas["order[billing_address]"])

    # Fill city
    address = browser.find_element_by_name("order[billing_city]")
    address.send_keys(datas["order[billing_city]"])

    # Fill postcode
    postCode = browser.find_element_by_name("order[billing_zip]")
    postCode.send_keys(datas["order[billing_zip]"])

    # Select country
    countrySelect = Select(browser.find_element_by_name("order[billing_country]"))
    countrySelect.select_by_visible_text(datas["order[billing_country]"])

    # Select credit card
    creditCardSelect = Select(browser.find_element_by_name("credit_card[type]"))
    creditCardSelect.select_by_visible_text(datas["credit_card[type]"])

    # Fill card number
    cardNumber = browser.find_element_by_name("credit_card[cnb]")
    cardNumber.send_keys(datas["credit_card[cnb]"])

    # Select the expiration month credit card
    monthExpirationSelect = Select(browser.find_element_by_name("credit_card[month]"))
    monthExpirationSelect.select_by_visible_text(datas["credit_card[month]"])

    # Select the expiration year credit card
    yearExpirationSelect = Select(browser.find_element_by_name("credit_card[year]"))
    yearExpirationSelect.select_by_visible_text(datas["credit_card[year]"])

    # Fill the CVV of the credit card
    cvv = browser.find_element_by_name("credit_card[vval]")
    cvv.send_keys(datas["credit_card[vval]"])

    # Accept the conditions
    browser.find_element_by_class_name("terms").click()

def initDatas():
    datas = {}
    datas["order[billing_name]"] = "Mickael RANAIVOARISOA"
    datas["order[email]"] = "mickael.ranaivoarisoa@orange.fr"
    datas["order[tel]"] = "0611223344"
    datas["order[billing_address]"] = "Adress"
    datas["order[billing_city]"] = "City"
    datas["order[billing_zip]"] = "Zip Code"
    datas["order[billing_country]"] = "FRANCE"
    datas["credit_card[type]"] = "Mastercard"
    datas["credit_card[cnb]"] = "0000111122223333"
    datas["credit_card[month]"] = "02"
    datas["credit_card[year]"] = "2019"
    datas["credit_card[vval]"] = "000"
    return datas

def main():
    datas = initDatas()
    
    print("[*] Opening Browser ...")
    profile = webdriver.FirefoxProfile()
    profile.set_preference("network.proxy.type", 1)
    profile.set_preference("network.proxy.http", "127.0.0.1")
    profile.set_preference("network.proxy.http_port", 8080)
    profile.update_preferences()
    
    #browser = webdriver.Firefox(firefox_profile = profile) 
    browser = webdriver.Firefox()
    browser.implicitly_wait(10)
    print("[+] Browser Opened")

    input("[*] Press Enter to continue and start ...")

    print("Beginning at : " + str(datetime.datetime.now()))
    category = "accessories"
    keywords = []
    keywords.append("Socks")
    color = "Black"
    size = ""

    if (searchArticle(browser, category, keywords, color) == False):
        return -1

    print("[*] Preparing the product ...")

    if (size != ""):
        try:
            # Select size
            sizeSelect = Select(browser.find_element_by_id("size"))
            sizeSelect.select_by_visible_text(size)
        except:
            print("[-] Article sold out or article not available")
            return -1

    try:
        # Add to the basket
        browser.find_element_by_name("commit").click()
    except:
         print("[-] Article sold out")
         return -1

    # Checkout the brasket
    browser.find_element_by_class_name("checkout").click()
    print("[+] Product checkout")
    
    print("[*] Filling the form ...")
    fillForm(browser, datas)
    print("[+] Form Filled")

    # Confirm the command
    print("[*] Confirmation of the  ...")
    browser.find_element_by_name("commit").click()
    print("[+] Command confirmed")
    
    print("Ending at : " + str(datetime.datetime.now()))

main()
