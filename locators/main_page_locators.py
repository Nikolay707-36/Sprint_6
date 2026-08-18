from selenium.webdriver.common.by import By

class MainPageLocators:
    @staticmethod
    def question_locator(question_index: int):
        return By.ID, f"accordion__heading-{question_index}"

    @staticmethod
    def answer_locator(answer_index: int):
        return By.ID, f"accordion__panel-{answer_index}"

    TOP_ORDER_BTN = By.XPATH, "//div[contains(@class, 'Header_Nav')]/button[contains(@class, 'Button_Button')]"
    BOTTOM_ORDER_BTN = By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[contains(@class, 'Button_Button')]"
    FAQ_SECTION = By.CLASS_NAME, "Home_FAQ__3uVm4"
    SCOOTER_LOGO = By.XPATH, "//img[@alt='Scooter']"
    YANDEX_LOGO = By.XPATH, "//img[@alt='Yandex']"
    DZEN_NEWS = By.XPATH, "//div[text()='Новости']"
