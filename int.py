# Importa le librerie necessarie
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configura il servizio Chrome con ChromeDriverManager
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()

# Avvia il driver con il servizio configurato
driver = webdriver.Chrome(service=service, options=options)
driver.get('https://web.whatsapp.com/')

# Chrome si apre
# Scansiona il codice QR

print("\n\nPlease MAXIMIZE the WhatsApp window before proceeding...")
print("\n\nPlease ignore all warnings and enter the name of user or group...\n\n")

name = input('Enter the name of user or group: ')
msg = input('Enter your message: ')
count = int(input('Enter the count: '))
gap = float(input('Interval (in seconds) between messages: '))
bot_prompt = input('Do you want to add bot prompt to your message? (Y/N) ').upper()

input('Enter anything after scanning QR code...')

# Trova l'utente o il gruppo specificato
try:
    user = driver.find_element(By.XPATH, f'//span[@title = "{name}"]')
    user.click()
except Exception as e:
    print(f"Error locating user/group '{name}': {e}")
    driver.quit()
    exit()

# Entrato nella chat
msg_box = driver.find_element(By.XPATH, '//div[@data-tab = "9"]')  # Controlla il valore di @data-tab se il codice non funziona

for i in range(count):
    if bot_prompt == 'Y':
        msg_final = f'<Status: {i+1}/{count}> {msg}'
    else:
        msg_final = msg
    msg_box.send_keys(msg_final)
    button = driver.find_element(By.CLASS_NAME, '_4sWnG')  # Aggiorna questa classe se necessario
    button.click()
    if gap > 0:
        time.sleep(gap)

# Messaggio finale
msg_final = 'Messages sent successfully!'
msg_box.send_keys(msg_final)
button = driver.find_element(By.CLASS_NAME, '_4sWnG')
button.click()

time.sleep(30)  # Permette il tempo necessario per l'invio dei messaggi prima della chiusura
driver.quit()
