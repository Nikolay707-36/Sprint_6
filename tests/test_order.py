import allure
import pytest

from data import OrderData
from pages.order_page import OrderPage
from pages.main_page import MainPage
from urls import Urls


@allure.feature("Заказы")
class TestOrder:
    @allure.title("Проверка верхней кнопки заказа")
    def test_top_order_button(self, driver):
        page = MainPage(driver)
        page.open_page(Urls.MAIN_PAGE)
        page.click_top_order_btn()
        assert page.get_current_url() == Urls.ORDER_PAGE, "Верхняя кнопка заказа ведёт на неправильную страницу"

    @allure.title("Проверка нижней кнопки заказа")
    def test_bottom_order_button(self, driver):
        page = MainPage(driver)
        page.open_page(Urls.MAIN_PAGE)
        page.click_bottom_order_btn()
        assert page.get_current_url() == Urls.ORDER_PAGE, "Нижняя кнопка заказа ведёт на неправильную страницу"

    @allure.title("Полная процедура заказа самоката через верхнюю кнопку")
    @pytest.mark.parametrize(
        "first_name,last_name,address,metro_station,phone,delivery_date,rental_period",
        OrderData.value,
    )
    def test_order_scooter_via_top_button(
        self,
        driver,
        first_name,
        last_name,
        address,
        metro_station,
        phone,
        delivery_date,
        rental_period,
    ):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        # 1. Открываем главную и кликаем верхнюю кнопку
        main_page.open_page(Urls.MAIN_PAGE)
        main_page.click_top_order_btn()
        
        # 2. Выполняем полный заказ
        order_page.order_scooter(
            name=first_name,
            second_name=last_name,
            address=address,
            metro_station=metro_station,
            phone_number=phone,
            day_number=delivery_date,
            period=rental_period,
        )
        
        # 3. Проверяем, что появилась кнопка статуса заказа (успешный заказ)
        assert order_page.find_status_button(), "Кнопка 'Посмотреть статус' не появилась после заказа"

    @allure.title("Полная процедура заказа самоката через нижнюю кнопку")
    @pytest.mark.parametrize(
        "first_name,last_name,address,metro_station,phone,delivery_date,rental_period",
        OrderData.value,
    )
    def test_order_scooter_via_bottom_button(
        self,
        driver,
        first_name,
        last_name,
        address,
        metro_station,
        phone,
        delivery_date,
        rental_period,
    ):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        # 1. Открываем главную и кликаем нижнюю кнопку
        main_page.open_page(Urls.MAIN_PAGE)
        main_page.click_bottom_order_btn()
        
        # 2. Выполняем полный заказ
        order_page.order_scooter(
            name=first_name,
            second_name=last_name,
            address=address,
            metro_station=metro_station,
            phone_number=phone,
            day_number=delivery_date,
            period=rental_period,
        )
        
        # 3. Проверяем, что появилась кнопка статуса заказа
        assert order_page.find_status_button(), "Кнопка 'Посмотреть статус' не появилась после заказа"
