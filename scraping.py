def DoThing(numeroExpediente):
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions
    from selenium.webdriver.common.by import By
    import time
    import pandas as pd

    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')

    driver_path = 'C:\\Users\\Menem Lo Hizo\\Desktop\\Scripts\\Scraping\\chromedriver.exe'

    driver = webdriver.Chrome(driver_path, chrome_options=options)

    driver.get('https://www.justiciacordoba.gob.ar/marcopolo/menu/index.aspx')

    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.ID, 'txtUserName'))).send_keys('1-20816')

    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.ID, 'txtUserContrasenia'))).send_keys('nildarosa')

    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.ID, 'cmdLogin'))).click()

    driver.get('https://www.justiciacordoba.gob.ar/marcopolo/_Expedientes/ExpedientesAlta.aspx')

    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'input#txtNumeroExpediente'))).send_keys(numeroExpediente)

    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.ID, 'btnBuscar'))).click()

    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'img#grdExpedientes_Row_0_column7_control_0'))).click()

    driver.implicitly_wait(10)
    texto_columnas = driver.find_element_by_xpath('//*[@id="grdOperaciones_Row_0_column3"]/div')
    texto_columnas = texto_columnas.text

    print(texto_columnas)
    input("dsadsa")

def main():
    DoThing('6798347')

if __name__ == '__main__':
    main()