from selenium.webdriver.common.by import By

class OrderPageLocators:
    NAME_INPUT = By.XPATH, "//input[@placeholder='* Имя']"
    LASTNAME_INPUT = By.XPATH, "//input[@placeholder='* Фамилия']"
    ADDRESS_INPUT = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"
    METRO_FIELD = By.XPATH, "//input[@placeholder='* Станция метро']"
    PHONE_FIELD = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"

    NEXT_BTN = By.XPATH, "//button[text()='Далее']"
    DATE_INPUT = By.XPATH, "//input[@placeholder='* Когда привезти самокат']"
    RENTAL_PERIOD_DROPDOWN = By.XPATH, "//div[text()='* Срок аренды']"
    ORDER_BTN = By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']"
    CONFIRM_BTN = By.XPATH, "//div[contains(@class, 'Order_Modal')]//button[text()='Да']"
    STATUS_BTN = By.XPATH, "//button[text()='Посмотреть статус']"
    COOKIE_BTN = By.ID, "rcc-confirm-button"

    @staticmethod
    def period_locator(period: str):
        return By.XPATH, f"//div[contains(text(), '{period}')]"

    @staticmethod
    def date_locator(day_number: str):
        return By.XPATH, f"//div[contains(text(), '{day_number}')]"

    @staticmethod
    def station_locator(station: str):
        return By.XPATH, f"//div[contains(text(), '{station}')]"
