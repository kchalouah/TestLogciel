from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")


users = ["standard_user", "locked_out_user", "problem_user", "performance_glitch_user"]
password = "secret_sauce"

for user in users:

    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")


    username_field.clear()
    username_field.send_keys(user)
    password_field.clear()
    password_field.send_keys(password)
    login_button.click()

    try:

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))
        print(f"Login réussi pour l'utilisateur {user}.")


        menu_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "react-burger-menu-btn")))
        menu_button.click()


        logout_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link")))
        logout_button.click()


        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "login-button")))
        print(f"Déconnexion réussie pour {user}.")

    except Exception as e:
        print(f"Erreur pour l'utilisateur {user}: {str(e)}")

        try:
            error_message = driver.find_element(By.CLASS_NAME, "error-message-container").text
            print(f"Login échoué pour {user} : {error_message}")
        except:
            print("Message d'erreur non trouvé.")

driver.quit()
