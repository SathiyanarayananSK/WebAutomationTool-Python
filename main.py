from AppClasses import WebAutomation
import os


web_automation = WebAutomation()

username = "SathiyanarayananSK"
password = os.getenv("PASSWORD_OLD")

web_automation.login(username, password)

f_name = input("Enter your full name: ")
email = input("Enter your email: ")
c_addr = input("Enter your current Address: ")
p_addr = input("Enter your permanent Address: ")

web_automation.fill_form(f_name, email, c_addr, p_addr)
web_automation.download()

input("Press Enter to close the browser")

web_automation.close()






