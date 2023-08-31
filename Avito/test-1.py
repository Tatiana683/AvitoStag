from selenium import webdriver
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "https://www.avito.ru/nikel/knigi_i_zhurnaly/domain-driven_design_distilled_vaughn_vernon_2639542363" #присваеваем переменной значение url
match = re.search(r'(\d+)$', link)  # Поиск последовательности цифр в конце строки, т.о. вычленяем id товара из URL
if match:
    extracted_number = match.group(1)              #при совпадении вернуть первую группу значений

browser = webdriver.Chrome()                    #Указываем с помощью которого браузера будем обращаться
browser.get(link)                                    #Обращаемся по ссылке в переменной link
auth = WebDriverWait(browser, 10).until(      
    EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Вход и регистрация')]"))).text              #Ожидание до тех пор пока на старнице не появится элемент с текстом "Вход и регистрация"
assert auth == "Вход и регистрация"                              #Проверка на то, что найденный элемент содержит текст "Вход и регистрация", косвенная проверка, что пользователь не авторизован
button_favorites = browser.find_element(By.CSS_SELECTOR, "button[class*=desktop-usq1f1]").click()  # Поиск кнопки добавления в избранное и последующий клик
check_favorites = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'В избранном')]"))).text #Дождаться до тех пор, пока не появится текст в элементе "В избранном"
assert check_favorites == "В избранном"    #Проверка на то, что текст в элементе соответствует ожиданию - "В избранном"
link2 = "https://www.avito.ru/favorites"     #присваеваем переменной значение url раздела избранное
browser.get(link2)            #Обращаемся по ссылке в переменной link2
ids_string = browser.find_element(By.XPATH, f"//div[@data-marker='item-{extracted_number}']")     #Ищем элемент на странице с таким же Id для проверки добавления товара в избранное


