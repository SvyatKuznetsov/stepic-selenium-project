import time
import pytest
from pages.product_page import ProductPage


@pytest.mark.parametrize('promo', ["offer0", "offer1", "offer2", "offer3", "offer4",
                                   "offer5", "offer6",
                                   pytest.param("offer7", marks=pytest.mark.xfail(reason="bugged promo")),
                                   "offer8", "offer9"])
def test_guest_can_add_product_to_basket(browser, promo):
    link = f"http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo={promo}"
    page = ProductPage(browser, link)
    page.open()
    page.guest_can_add_product_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(1)
    page.guest_can_see_product_name()
    time.sleep(1)
    page.product_price_is_correct()

