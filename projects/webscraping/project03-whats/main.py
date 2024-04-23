from playwright.sync_api import sync_playwright
import time
import pyautogui as bot
from re import fullmatch

def check_number(number: str) -> bool:
    """Checks the Number to see if contains the Country Code"""
    return "+" in number or "_" in number

def send_message(phone_no, msg):
    phone_no = phone_no.replace(" ", "")
    if not fullmatch(r"^\+?[0-9]{2,4}\s?[0-9]{9,15}", phone_no):
        raise bot.alert("Invalid Phone Number.")
    url_message = f"https://web.whatsapp.com/send?phone={phone_no}&msg=HelloWOrld"

    time.sleep(5)
    return url_message


def send_message_list(list_phone=None):
    if list_phone:
        for phone_no in list_phone:
            send_message(phone_no)
    else:
        raise bot.alert("Please add a list of contacts")


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    ok = bot.confirm(text="This program will controling your computer, are you agree with this?", title='Confirm',
                         buttons=['OK', 'Cancel'])
    if ok == "OK":
        bot.alert("Ok, now DONT touch in your computer")
        msg = bot.prompt(text='Please write your message', title='Write your message', default='')
        phone = bot.prompt(text='Please write your full number', title='Write your number', default='')
        
        if msg and phone:
            page.goto(send_message(phone, msg))

    # url = 'https://web.whatsapp.com/'
    # page.goto(url)
    # initial = page.locator('xpath=//*[@id="app"]/div/div[2]/div[3]/div[1]/div/div/div[2]/div/div')
    # regenarate_code = page.locator('xpath=//*[@id="app"]/div/div[2]/div[3]/div[1]/div/div/div[2]/div/span/button')
    # if initial or regenarate_code:
    #     bot.alert("Please considere doing login on What's App Web befero.")



