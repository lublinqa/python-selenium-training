import pytest
from pages.google_page import GooglePage
from setup.setup import driver_init


@pytest.mark.usefixtures('driver_init')
class TestGoogle:

    @pytest.fixture(autouse=True)
    def class_setup(self, driver_init):
        self.gp = GooglePage(self.driver)

    def test_search(self):
        self.driver.get('http://google.com')
        self.gp.search_google()
