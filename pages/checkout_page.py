from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import Page

class CheckoutPage(Page):

    FIRST_NAME = (By.CSS_SELECTOR,"#billing_first_name")
    LAST_NAME = (By.ID,"billing_last_name")
    COMPANY_NAME = (By.ID,"billing_company")
    DIFFERENT_COUNTRIES = (By.ID,"billing_country")
    STREET_ADDRESS = (By.ID,"billing_address_1")
    APARTMENT_NUMBER = (By.ID, "billing_address_2")
    CITY_NAME = (By.ID,"billing_city")
    BILLING_COUNTRY = (By.ID,"select2-billing_country-container")
    DiFFERENT_STATES = (By.ID,"billing_state")
    BILLING_STATE = (By.ID,"select2-billing_state-container")
    ZIP_CODE = (By.ID,"billing_postcode")
    PHONE_NUMBER = (By.ID,"billing_phone")
    EMAIL_ADDRESS = (By.ID,"billing_email")
    TOTAL_INPUT_FIELDS = (By.CSS_SELECTOR,".woocommerce-billing-fields p.form-row label")
    REQUIRED_FIELD = (By.CSS_SELECTOR,".required")
    ADDITIONAL_INFORMATION = (By.ID,"order_comments")
    PLACE_ORDER = (By.CSS_SELECTOR,("#place_order"))
    ERROR_MESSAGE = (By.CSS_SELECTOR,".woocommerce-error")
    SHOPPING_CART = (By.CSS_SELECTOR,"a[href='https://gettop.us/cart/']")
    REQUIRED_FIELD_NAMES = (By.CSS_SELECTOR, ".form-row label")


    def enter_first_name(self,firstname):
        self.Firstname = self.find_element(*self.FIRST_NAME)
        self.Firstname.send_keys('sumitha')

    def enter_last_name(self,lastname):
        self.Lastname = self.find_element(*self.LAST_NAME)
        self.Lastname.send_keys('sundaresan')


    def enter_company_name(self,company_name):
        self.company_name = self.find_element(*self.COMPANY_NAME)
        self.company_name.send_keys('ABC company')

    def select_country(self,any):
        self.country_dropdown = Select(self.find_element(*self.DIFFERENT_COUNTRIES))
        self.country_dropdown.select_by_value(f'{any}')


    def enter_street_address(self,valid):
        self.street_address = self.find_element(*self.STREET_ADDRESS)
        self.street_address.send_keys('ABC street')
        self.appartment_num = self.find_element(*self.APARTMENT_NUMBER)
        self.appartment_num.send_keys("123")

    def enter_city(self,city):
        self.city_name = self.find_element(*self.CITY_NAME)
        self.city_name.send_keys('Seattle')

    def select_state(self,any):
        self.select_state = Select(self.find_element(*self.DiFFERENT_STATES))
        self.select_state.select_by_value('WA')

    def enter_zipcode(self,zipcode):
        self.zipcode = self.find_element(*self.ZIP_CODE)
        self.zipcode.send_keys('98133')

    def enter_phone_number(self,valid):
        self.phone_number = self.find_element(*self.PHONE_NUMBER)
        self.phone_number.send_keys("9876543210")

    def enter_email_address(self,valid):
        self.email_address = self.find_element(*self.EMAIL_ADDRESS)
        self.email_address.send_keys("abc@gmail.com")

    def additional_information(self):
        self.additional_information = self.find_element(*self.ADDITIONAL_INFORMATION)
        self.additional_information.send_keys(" ")

    def required_field_not_blank(self):
        input_fields = self.find_elements(*self.TOTAL_INPUT_FIELDS)
        print(len(input_fields))
        for i in input_fields:
            if "*" in i.text:
                if ("First name") in i.text:
                    assert (self.Firstname.get_attribute('value')) != " "

                if ("Last name") in i.text:
                    assert(self.Lastname.get_attribute('Value')) != " "

                if ("Company name") in i.text:
                    assert(self.company_name.get_attribute('value')) != " "

                if ("Country / Region ") in i.text:
                    assert(self.find_element(*self.BILLING_COUNTRY).get_attribute('value')) != " "

                if("Town / City") in i.text:
                    assert(self.city_name.get_attribute('value')) != " "

                if ("State / County") in i.text:
                    assert(self.find_element(*self.BILLING_STATE).get_attribute('value')) != " "

                if ("Postcode / ZIP") in i.text:
                    assert(self.zipcode.get_attribute('value')) != " "

                if ("Phone") in i.text:
                    assert(self.phone_number.get_attribute('value')) != " "

                if ("Email address") in i.text:
                    assert(self.email_address.get_attribute('value')) != " "

                if("Additional Information") in i.text:
                    assert(self.additional_information.get_attribute()) != " "


    def click_place_order(self):
        WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.CSS_SELECTOR,"#place_order")))
        flag = self.find_element(*self.PLACE_ORDER)
        action = ActionChains(self.driver)
        action.move_to_element(flag).click().perform()


    def verify_correct_country(self,selected_country):
        actual_country = self.find_element(*self.BILLING_COUNTRY).text
        print(actual_country)
        assert actual_country == selected_country,f'{actual_country} does not match {selected_country}'

    def error_message(self):
        expected_text = "Billing First name is a required field.\nBilling Last name is a required field.\nBilling Street address is a required field.\nBilling Town / City is a required field.\nBilling ZIP is a required field.\nBilling Phone is a required field.\nBilling Email address is a required field.\nInvalid payment method."
        actual_text = self.find_element(*self.ERROR_MESSAGE).text
        assert expected_text in actual_text,f'actual text {actual_text} doesnot macth expected text{expected_text}'

    def click_shopping_cart(self):
        self.click(*self.SHOPPING_CART)


