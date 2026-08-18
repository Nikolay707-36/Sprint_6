import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_page_locators import OrderPageLocators

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Закрыть cookies-баннер")
    def close_cookie_banner(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(OrderPageLocators.COOKIE_BTN)
            ).click()
        except Exception:
            pass

    @allure.step("Открыть страницу")
    def open_page(self, url: str):
        self.driver.get(url)
        self.close_cookie_banner()

    @allure.step("Поиск элемента с ожиданием")
    def wait_and_find_element(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        return element

    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Переключиться на окно {window_index}")
    def switch_to_window(self, window_index: int):
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > window_index)
        self.driver.switch_to.window(self.driver.window_handles[window_index])

    @allure.step("Получить текущий URL")
    def get_current_url(self) -> str:
        return self.driver.current_url
