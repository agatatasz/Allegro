# Import bibliotek
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

#Zmienne

produkt = "Barbie Extra"
email = "kasia.wp.pl"
haslo = "kasia123$"

class AllegroPageObject:
    Cookies = "//*[@id='opbox-gdpr-consents-modal']/div/div[2]/div[2]/button[1]"
    Kategoria = "//*[@id='tab-dzialy']/div/div/div[5]"
    Barbie = "/html/body/div[2]/div[1]/div/div/div/div/div/div[3]/header/div[1]/div/div/div/form/input"
    Szukaj = "/html/body/div[2]/div[1]/div/div/div/div/div/div[3]/header/div[1]/div/div/div/form/button"
    Sortowanie = "allegro.listing.sort"
    Wybierz = "//*[@id='search-results']/div[6]/div/div/div[1]/div/div/section[2]/article[16]/div/div/div[2]/div[1]/h2/a"
    Dodaj = "add-to-cart-button"
    Koszyk = "/html/body/div[3]/div/div/div[2]/div/div/div/div/div[3]/a"
    Dostawa = "/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div[1]/div[1]/app-root/cart/div/aside/div/div[1]/cart-footer/div/sticky-buttons/div/div/div/submit-button/button/span[2]"
    Login = "login"
    PassWord = "password"
    Zaloguj = "//*[@id='authForm']/div/div/div[2]/button"
    Error = "login-form-submit-error"

class BaseTestHome(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://allegro.pl/")
        self.driver.implicitly_wait(10)

    def test_shopping(self):
        driver = self.driver
        # zaakceptuj cookies
        driver.find_element(By.XPATH, AllegroPageObject.Cookies) .click()
        sleep(2)
        # wybierz kategorię dziecko
        driver.find_element(By.XPATH, AllegroPageObject.Kategoria).click()
        sleep(2)
        # wyszukaj produkt
        wyszukaj_input = driver.find_element(By.XPATH, AllegroPageObject.Barbie)
        wyszukaj_input.send_keys(produkt)
        sleep(2)
        # kliknij szukaj
        driver.find_element(By.XPATH, AllegroPageObject.Szukaj) .click()
        sleep(2)
        # kliknij sortuj po cenie: od najniższej
        sortuj = Select(driver.find_element(By.ID, AllegroPageObject.Sortowanie))
        sortuj.select_by_value("p")
        sleep(2)
        # zeskroluj stronę
        driver.execute_script("window.scrollBy(0,1000)")
        sleep(5)
        # kliknij lalkę
        driver.find_element(By.XPATH, AllegroPageObject.Wybierz) .click()
        # dodaj lalkę do koszyka
        driver.find_element(By.ID, AllegroPageObject.Dodaj) .click()
        # kliknij idź do koszyka
        driver.find_element(By.XPATH, AllegroPageObject.Koszyk) .click()
        # kliknij dostawa i płatnośći
        driver.find_element(By.XPATH, AllegroPageObject.Dostawa) .click()
        # wpisz e-mail
        email_input = driver.find_element(By.ID, AllegroPageObject.Login)
        email_input.send_keys(email)
        sleep(2)
        # wpisz hasło
        password_input = driver.find_element(By.ID, AllegroPageObject.PassWord)
        password_input.send_keys(haslo)
        sleep(2)
        # kliknij zaloguj się
        driver.find_element(By.XPATH, AllegroPageObject.Zaloguj) .click()
        # potwierdzenie błędu
        error_info = driver.find_element(By.ID, AllegroPageObject.Error).text
        self.assertEqual("Login, e-mail lub hasło są nieprawidłowe", error_info)
        sleep(3)





    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

