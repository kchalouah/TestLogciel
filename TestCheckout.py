from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

# Connexion
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

driver.find_element(By.CLASS_NAME, "btn_inventory").click()
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()


driver.find_element(By.ID, "checkout").click()
driver.find_element(By.ID, "first-name").send_keys("John")
driver.find_element(By.ID, "last-name").send_keys("Doe")
driver.find_element(By.ID, "postal-code").send_keys("12345")
driver.find_element(By.ID, "continue").click()


summary_page = driver.find_element(By.CLASS_NAME, "summary_info")
assert summary_page.is_displayed(), "La page de récapitulatif n'est pas affichée."
print("Passage à la caisse réussi.")

driver.quit()
