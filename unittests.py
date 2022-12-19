import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


class ChromeUploadImage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_add_image(self):
        driver = self.driver
        driver.get("http://localhost:3000")
        wait = WebDriverWait(driver, 20)

        btnAddImage = '//button[text()="Adicionar imagem"]'
        wait.until(EC.visibility_of_element_located((By.XPATH, btnAddImage)))
        btnAddImage = driver.find_element(By.XPATH, btnAddImage)
        btnAddImage.click()

        inputImage = '//input[@type="file"]'
        writeImage = os.getcwd() + '/static/img/SMPTE_Color_Bars.png'
        inputImage = driver.find_element(By.XPATH, inputImage)
        inputImage.send_keys(writeImage)

        uploadedImage = '//img[contains(@alt, "Uploaded photo")]'
        wait.until(EC.visibility_of_element_located((By.XPATH, uploadedImage)))

        inputTitle = '//input[@placeholder="Título da imagem..."]'
        writeTitle = "SMPTE Color Bars"
        inputTitle = driver.find_element(By.XPATH, inputTitle)
        inputTitle.send_keys(writeTitle)

        inputDescription = '//input[@placeholder="Descrição da imagem..."]'
        writeDescription = "SMPTE Color Bars Test Pattern"
        inputDescription = driver.find_element(By.XPATH, inputDescription)
        inputDescription.send_keys(writeDescription)

        inputSubmit = '//button[@type="submit"]'
        inputSubmit = driver.find_element(By.XPATH, inputSubmit)
        inputSubmit.click()

        success = '//div[contains(text(),"Imagem cadastrada")]'
        success = wait.until(
            EC.visibility_of_element_located((By.XPATH, success)))
        self.assertEqual("Imagem cadastrada", success.text)

    def test_required_image(self):
        driver = self.driver
        driver.get("http://localhost:3000")
        wait = WebDriverWait(driver, 20)

        btnAddImage = '//button[text()="Adicionar imagem"]'
        wait.until(EC.visibility_of_element_located((By.XPATH, btnAddImage)))
        btnAddImage = driver.find_element(By.XPATH, btnAddImage)
        btnAddImage.click()

        inputImage = '//input[@type="file"]'
        inputImage = driver.find_element(By.XPATH, inputImage)

        inputSubmit = '//button[@type="submit"]'
        inputSubmit = driver.find_element(By.XPATH, inputSubmit)
        inputSubmit.click()

        labelImage = '//label[@data-invalid]'
        try:
            labelImage = driver.find_element(By.XPATH, labelImage)
            labelImage = True
        except NoSuchElementException:
            labelImage = False

        self.assertEqual(True, labelImage)

    def tearDown(self):
        self.driver.quit()


class ChromeLoadImages(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_load_images(self):
        driver = self.driver
        driver.get("http://localhost:3000")
        wait = WebDriverWait(driver, 20)

        btnElement = '//button[text()="Carregar mais"]'
        imagesElement = '//div[@class="css-0"]'

        wait.until(EC.visibility_of_element_located((By.XPATH, btnElement)))

        imagesBefore = driver.find_elements(By.XPATH, imagesElement)

        btnloadImages = driver.find_element(By.XPATH, btnElement)
        btnloadImages.click()

        wait.until(EC.visibility_of_element_located((By.XPATH, btnElement)))

        imagesAfter = driver.find_elements(By.XPATH, imagesElement)
        self.assertNotEqual(len(imagesBefore), len(imagesAfter))

    def test_modal_up(self):
        driver = self.driver
        driver.get("http://localhost:3000")
        wait = WebDriverWait(driver, 20)

        imagesElement = '//div[contains(@class,"chakra-skeleton")]//img[contains(@class,"chakra-image")]'
        wait.until(EC.visibility_of_all_elements_located(
            (By.XPATH, imagesElement)))

        images = driver.find_elements(By.XPATH, imagesElement)
        images[0].click()

        modalImage = '//div[contains(@class,"chakra-modal__body")]//img[contains(@class,"chakra-image")]'
        wait.until(EC.visibility_of_element_located((By.XPATH, modalImage)))
        try:
            modalImage = driver.find_element(By.XPATH, modalImage)
            modalImage = True
        except NoSuchElementException:
            modalImage = False

        self.assertEqual(True, modalImage)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
