# class_cdiscount5.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class CdiscountBot:
    def __init__(self):
        self.service = Service(ChromeDriverManager().install())
        self.options = Options()
        self.options.add_argument("--start-maximized")
        self.options.add_argument("--incognito")
        # self.options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        self.wait = WebDriverWait(self.driver, 10)
    
    def open_website(self, url):
        print(f"Opening website: {url}")
        self.driver.get(url)

    def click_button(self, by, value):
        try:
            print(f"Clicking button: {by} {value}")
            button = self.wait.until(EC.element_to_be_clickable((by, value)))
            button.click()
        except Exception as e:
            print(f"An error occurred while trying to click the button: {e}")
            self.take_screenshot('click_button_error.png')

    def enter_text(self, by, value, text):
        try:
            print(f"Entering text '{text}' in element: {by} {value}")
            input_field = self.wait.until(EC.visibility_of_element_located((by, value)))
            input_field.send_keys(text)
        except Exception as e:
            print(f"An error occurred while trying to enter text: {e}")
            self.take_screenshot('enter_text_error.png')

    def click_product(self, product_name):
        try:
            print(f"Clicking product with name: {product_name}")
            product_xpath = f"//div[contains(@class, 'prdtBloc') and .//h2[contains(text(), '{product_name}')]]"
            print(f"Product XPath: {product_xpath}")
            product = self.wait.until(EC.visibility_of_element_located((By.XPATH, product_xpath)))
            print("Product found, scrolling into view...")
            self.driver.execute_script("arguments[0].scrollIntoView();", product)
            self.take_screenshot('before_click_product.png')
            time.sleep(2)
            print("Attempting to click the product...")
            product.click()
            self.take_screenshot('after_click_product.png')
        except Exception as e:
            print(f"An error occurred while trying to click the product: {e}")
            self.take_screenshot('click_product_error.png')

    def click_element(self, by, value):
        try:
            print(f"Clicking element: {by} {value}")
            element = self.wait.until(EC.element_to_be_clickable((by, value)))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            time.sleep(2)
            attempts = 0
            while attempts < 3:
                try:
                    element.click()
                    break
                except Exception as e:
                    print(f"Attempt {attempts + 1} - Element click intercepted, retrying...")
                    self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
                    time.sleep(2)
                    attempts += 1
            else:
                raise Exception("Failed to click element after multiple attempts")
        except Exception as e:
            print(f"An error occurred while trying to click the element: {e}")
            self.take_screenshot('click_element_error.png')

    def click_element_by_class_name(self, class_name):
        try:
            print(f"Clicking element with class name: {class_name}")
            element = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, class_name)))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            time.sleep(2)
            attempts = 0
            while attempts < 3:
                try:
                    element.click()
                    break
                except Exception as e:
                    print(f"Attempt {attempts + 1} - Element click intercepted, retrying...")
                    self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
                    time.sleep(2)
                    attempts += 1
            else:
                raise Exception("Failed to click element after multiple attempts")
        except Exception as e:
            print(f"An error occurred while trying to click the element by class name: {e}")
            self.take_screenshot('click_element_by_class_name_error.png')

    def set_quantity(self, quantity):
        try:
            print(f"Setting quantity to: {quantity}")
            quantity_field = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='ProductFormData_ProductPostedForm_QuantitySelected']")))
            self.driver.execute_script("arguments[0].scrollIntoView();", quantity_field)
            time.sleep(2)
            quantity_field.click()
            quantity_field.send_keys(str(quantity))
            quantity_field.send_keys(Keys.ENTER)
        except Exception as e:
            print(f"An error occurred while trying to set the quantity: {e}")
            self.take_screenshot('set_quantity_error.png')

    def take_screenshot(self, filename):
        self.driver.save_screenshot(filename)
        print(f"Screenshot saved as {filename}")

    def wait_for_element_not_intercepted(self, by, value):
        while True:
            try:
                element = self.wait.until(EC.element_to_be_clickable((by, value)))
                return element
            except Exception as e:
                time.sleep(0.5)
    
    def quit(self):
        print("Closing browser")
        self.driver.quit()
