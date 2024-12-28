from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os


class WebAutomation:
    def __init__(self):
        # Define driver, options and service
        self.chrome_options = Options()
        self.chrome_options.add_argument("--disable-search-engine-choice-screen")
        self.download_path = os.getcwd()
        self.prefs = {'download.default_directory': self.download_path}
        self.chrome_options.add_experimental_option('prefs', self.prefs)
        self.service = Service("chromedriver-win64/chromedriver.exe")
        self.driver = webdriver.Chrome(options=self.chrome_options, service=self.service)

    def login(self, username, password):
        # Load the webpage
        url = "https://demoqa.com/login"
        self.driver.get(url)
        # Locate username, password and login button
        username_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
        password_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
        button_field = self.driver.find_element(By.ID, 'login')

        # Fill the details and click the button
        username_field.send_keys(username)
        password_field.send_keys(password)
        self.driver.execute_script("arguments[0].click();", button_field)

    def fill_form(self, f_name, email, c_addr, p_addr):
        # Locate Elements dropdown and Text Box
        elements = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div')))
        elements.click()
        text_box = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-0')))
        text_box.click()

        # Locate the form fields and submit button
        fullname_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
        email_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userEmail')))
        current_address_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'currentAddress')))
        permanent_address_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'permanentAddress')))
        submit_button_field = self.driver.find_element(By.ID, 'submit')

        # Fill in the form fields
        fullname_field.send_keys(f_name)
        email_field.send_keys(email)
        current_address_field.send_keys(c_addr)
        permanent_address_field.send_keys(p_addr)
        self.driver.execute_script("arguments[0].click();", submit_button_field)

    def download(self):
        # Locate the download section and download button
        upload_download_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-7')))
        upload_download_field.click()
        download_button_field = self.driver.find_element(By.ID, 'downloadButton')
        self.driver.execute_script("arguments[0].click();", download_button_field)

    def close(self):
        self.driver.quit()



