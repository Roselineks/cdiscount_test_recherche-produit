# bot_cdiscount5.py
from class_cdiscount5 import CdiscountBot
from selenium.webdriver.common.by import By
import time

if __name__ == "__main__":
    bot = CdiscountBot()
    bot.open_website("https://www.cdiscount.com/")
    print("Opened website")

    # Accepter les cookies
    bot.click_button(By.XPATH, "//*[@id='footer_tc_privacy_button_2']")
    print("Cookies accepted")

    # S'identifier
    bot.click_button(By.XPATH, "//*[@id=\"header\"]/div[1]/div/div[3]/div/div[2]")    
    print("Page d'identification ouverte")

    # Entrer l'email
    bot.enter_text(By.XPATH, "//*[@id=\"CustomerLogin_CustomerLoginFormData_Email\"]", "ricacegos@gmail.com")
    print("Email saisi")

    # Entrer le mot de passe
    bot.enter_text(By.XPATH, "//*[@id=\"CustomerLogin_CustomerLoginFormData_Password\"]", "Roibcaan1")
    print("Mot de passe saisi")

    # Se connecter
    bot.click_button(By.XPATH, "//*[@id=\"LoginForm\"]/div/div/div[1]/div[5]/div/input")
    print("Profile connecté")

    # Rechercher un produit
    bot.enter_text(By.ID, "search", "Clavier sans fil")
    print("Search text entered")

    # Attendre pour afficher les résultats de recherche
    bot.click_button(By.XPATH, "//*[@id='results']/li[2]/a/div[2]")
    print("Clicked on the search result")

    # Sélectionner le produit
    bot.click_product("Pack RF02 Clavier Souris Sans Fil")
    print("Produit cliqué")

    time.sleep(3)

    # Voir la présentation du produit avec sélecteur basé sur l'attribut href
    bot.click_element(By.XPATH, "//*[@id=\"fpMain\"]/div/div/div/div[3]/div/div/div[1]/div/div/p[1]/a")
    print("Product presentation clicked")

    time.sleep(3)

    # Actualiser la page
    # bot.driver.refresh()
    # print("Page refreshed after product presentation")

    # time.sleep(3)

    # Voir la description du produit avec sélecteur basé sur l'attribut href
    bot.click_element(By.CSS_SELECTOR, "a[href='#description-accordion']")
    print("Product presentation clicked")

    time.sleep(3)

    # Actualiser la page
    # bot.driver.refresh()
    # print("Page refreshed after product presentation")

    # time.sleep(3)

    # Voir les avis du produit avec XPATH
    bot.click_element(By.XPATH, "//*[@id=\"fpMain\"]/div/div/div/div[1]/div/div[2]/span[1]")
    print("Product reviews clicked")

    time.sleep(3)

    # Modifier la quantité et ajouter au panier
    bot.set_quantity(2)
    print("Quantity set")

    bot.click_button(By.XPATH, "//*[@id='fpAddBsk']")
    print("Add to basket clicked")

    # Voir le panier avec XPATH
    bot.click_element(By.XPATH, "//*[@id='raContent']/div[1]/div[1]/a[1]")
    print("Cart viewed")

    # Actualiser la page
    # bot.driver.refresh()
    # print("Page refreshed after product presentation")

    time.sleep(4)

    # Modifier la quantité 
    bot.set_quantity(4)
    print("Quantity modified")

    # Fermer le navigateur
    bot.quit()
    print("Browser closed")
