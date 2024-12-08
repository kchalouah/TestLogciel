from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")


driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()


add_to_cart_buttons = driver.find_elements(By.CLASS_NAME, "btn_inventory")
for button in add_to_cart_buttons[:3]:  # Ajouter les 3 premiers produits
    button.click()


driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
assert len(cart_items) == 3, "Les produits ajoutés ne sont pas visibles dans le panier."
print("Produits ajoutés au panier avec succès.")


remove_buttons = driver.find_elements(By.CLASS_NAME, "cart_button")
remove_buttons[0].click()
cart_items_after_removal = driver.find_elements(By.CLASS_NAME, "cart_item")
assert len(cart_items_after_removal) == 2, "Le produit n'a pas été retiré du panier."
print("Produit retiré du panier avec succès.")

driver.quit()
