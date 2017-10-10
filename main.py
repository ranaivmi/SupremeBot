from selenium import webdriver
from selenium.webdriver.support.ui import Select

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
    

def main():
    datas = {}
    datas["order[billing_name]"] = "Mickael RANAIVOARISOA"
    datas["order[email]"] = "mickael.ranaivoarisoa@orange.fr"
    datas["order[tel]"] = "0652855770"
    datas["order[billing_address]"] = "20 rue de l Abreuvoir"
    datas["order[billing_city]"] = "Hadancourt le Haut Clocher"
    datas["order[billing_zip]"] = "60240"
    datas["order[billing_country]"] = "FRANCE"
    datas["credit_card[type]"] = "Mastercard"
    datas["credit_card[cnb]"] = "4573559911224455"
    datas["credit_card[month]"] = "02"
    datas["credit_card[year]"] = "2019"
    datas["credit_card[vval]"] = "941"
          
    print("[*] Opening Browser ...")
    browser = webdriver.Firefox()
    print("[+] Browser OK")
    print("[*] Redirection URL ...")
    browser.get('http://www.supremenewyork.com/shop/accessories/x2ft7j1p5/zotpigjlv')
    print("[+] Redirection URL OK")


    print("[*] Preparing the product ...")
    # Select size
    sizeSelect = Select(browser.find_element_by_id("size"))
    sizeSelect.select_by_visible_text("Medium")

    # Add to the bracket
    browser.find_element_by_name("commit").click()

    # Checkout the bracket
    browser.find_element_by_class_name("checkout").click()
    print("[+] Product checkout")
    
    print("[*] Filling the form ...")
    fillForm(browser, datas)
    print("[+] Form Filled")

    # Confirm the command
    print("[*] Confirmation of the  ...")
    browser.find_element_by_name("commit").click()
    print("[+] Command confirmed")

main()
