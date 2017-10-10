from selenium import webdriver
from selenium.webdriver.support.ui import Select

def fillForm(browser):
    # Fill name
    name = browser.find_element_by_name("order[billing_name]")
    name.send_keys("Mickael RANAIVOARISA")
    
    # Fill email
    email = browser.find_element_by_name("order[email]")
    email.send_keys("mickael.ranaivoarisoa@orange.fr")

    # Fill tel
    tel = browser.find_element_by_name("order[tel]")
    tel.send_keys("0652855770")

    # Fill address
    address = browser.find_element_by_name("order[billing_address]")
    address.send_keys("20 rue de l Abreuvoir")

    # Fill city
    address = browser.find_element_by_name("order[billing_city]")
    address.send_keys("Hadancourt le Haut Clocher")

    # Fill postcode
    postCode = browser.find_element_by_name("order[billing_zip]")
    postCode.send_keys("60240")

    # Select country
    countrySelect = Select(browser.find_element_by_name("order[billing_country]"))
    countrySelect.select_by_visible_text("FRANCE")

    # Select credit card
    creditCardSelect = Select(browser.find_element_by_name("credit_card[type]"))
    creditCardSelect.select_by_visible_text("Mastercard")

    # Fill card number
    cardNumber = browser.find_element_by_name("credit_card[cnb]")
    cardNumber.send_keys("4573559911224455")

    # Select the expiration month credit card
    monthExpirationSelect = Select(browser.find_element_by_name("credit_card[month]"))
    monthExpirationSelect.select_by_visible_text("02")

    # Select the expiration year credit card
    yearExpirationSelect = Select(browser.find_element_by_name("credit_card[year]"))
    yearExpirationSelect.select_by_visible_text("2019")

    # Fill the CVV of the credit card
    cvv = browser.find_element_by_name("credit_card[vval]")
    cvv.send_keys("941")

    # Accept the conditions
    browser.find_element_by_class_name("terms").click()

    # Commit the command
    browser.find_element_by_name("commit").click()

    
def main():

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
    fillForm(browser)
    print("[+] Form Filled")
    
main()
