import asyncio
from playwright.sync_api import sync_playwright
import pyautogui as bot
import re
import time

def validar_email(email):
    # Expressão regular para validar o formato do e-mail
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    # Verifica se o e-mail corresponde à expressão regular
    if re.match(regex, email):
        return True
    else:
        return False

def main():
    with sync_playwright() as p:
        ok = bot.confirm(text="Now, we'll collect some informations about you, ok?", title='Confirm',
                         buttons=['OK', 'Cancel'])
        if ok == "OK":
            while True:
                email = bot.prompt(text='Please write your e-mail', title='E-mail', default='')
                if validar_email(email):
                    break
            time.sleep(1)
            pwd = bot.password(text='Whats your password', title='Password', default='', mask='*')
            # Get your passwd:


            browser = p.firefox.launch(headless=False)
            page = browser.new_page()
            page.goto("https://contacts.google.com/new")

            # Field email xpath: //*[@id="identifierId"]
            page.locator('xpath=//*[@id="identifierId"]').click()
            bot.write(email)
            # Btn identifierNext xpath: //*[@id="identifierNext"]/div/button
            page.locator('xpath=//*[@id="identifierNext"]/div/button').click()
            # Field password xpath: //*[@id="password"]/div[1]/div/div[1]/input
            page.locator('xpath=//*[@id="password"]/div[1]/div/div[1]/input').click()
            bot.write(pwd)
            # Btn passwordNext xpath: //*[@id="passwordNext"]/div/button
            page.locator('xpath=//*[@id="passwordNext"]/div/button').click()

            # Login success: //*[@id="yDmH0d"]/c-wiz[2]/div/div/div[2]/div/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/img
            # page.locator('xpath=//*[@id="yDmH0d"]/c-wiz[2]/div/div/div[2]/div/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/img').click()

            time.sleep(2)

            # Field name xpath: //*[@id="c181"]
            page.locator('xpath=//*[@id="c181"]').click()
            bot.write("Test Bot Python")
            # Field email xpath: //*[@id="c197"]
            page.locator('xpath=//*[@id="c197"]').click()
            bot.write("teste@botpython.com")
            # Field phone xpath: //*[@id="c209"]
            page.locator('xpath=//*[@id="c209"]').click()
            bot.write("41987654321")
            # Btn save xpath: //*[@id="yDmH0d"]/c-wiz[3]/div/div/div[2]/div/div[1]/div[1]/div/div/div/div[3]/div/div/button/span[5]
            page.locator('xpath=//*[@id="yDmH0d"]/c-wiz[3]/div/div/div[2]/div/div[1]/div[1]/div/div/div/div[3]/div/div/button/span[5]').click()

            browser.close()
        else:
            bot.alert(text="Ok bye...", title="Bye")

main()
