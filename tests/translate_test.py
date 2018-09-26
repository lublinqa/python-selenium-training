import pytest
from pages.translate_page import GoogleTranslatePage
from setup.setup import driver_init


@pytest.mark.usefixtures('driver_init')
class TranslateTest:

    @pytest.fixture(autouse=True)
    def class_setup(self, driver_init):
        self.gt = GoogleTranslatePage(self.driver)

    def test_translate(self):
        self.driver.get('https://translate.google.pl/?hl=pl&tab=wT&authuser=0')
        self.gt.check_google_translate()
