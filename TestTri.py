from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()


sort_dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
select = Select(sort_dropdown)


select.select_by_value("lohi")
sorted_products = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
prices = [float(price.text.replace("$", "")) for price in sorted_products]
assert prices == sorted(prices), "Les produits ne sont pas triés par prix croissant."
print("Tri par prix croissant : OK.")

driver.quit()
