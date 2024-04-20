import pyautogui as bot
import time
import re

# bot.press("win")
# bot.write("noteTeste.txt")
# time.sleep(1)
# bot.press("enter")  

# time.sleep(2)
# bot.confirm(text='Welcome to automation world', title='Hello World!', buttons=['OK', 'Cancel'])

def validar_email(email):
    # Expressão regular para validar o formato do e-mail
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    # Verifica se o e-mail corresponde à expressão regular
    if re.match(regex, email):
        return True
    else:
        return False

ok = bot.confirm(text="Now, we'll collect some informations about you, ok?", title='Confirm', buttons=['OK', 'Cancel'])
print(ok)

if ok == "OK":
    while True:
        email = bot.prompt(text='Please write your e-mail', title='E-mail' , default='')
        if validar_email(email):
            break
    print(email)
    time.sleep(1)
    pwd = bot.password(text='Whats your password', title='Password', default='', mask='*')
    # Get your passwd:
    print(pwd)
else:
    bot.alert(text="Ok bye...", title="Bye")