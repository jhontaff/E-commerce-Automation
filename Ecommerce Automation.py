import random
import pandas
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome('C:\webdriver_chrome\chromedriver.exe')
driver.get('http://www.tutorialsninja.com/demo/')
driver.maximize_window()
time.sleep(2)

btn_phones = driver.find_element('xpath', '//*[@id="menu"]/div[2]/ul/li[6]/a')

btn_phones.click()
time.sleep(2)

slc_phone = driver.find_element('xpath','//*[@id="content"]/div[2]/div[3]/div/div[2]/div[1]/h4/a')
slc_phone.click()

img_phone = driver.find_element('xpath','//*[@id="content"]/div/div[1]/ul[1]/li[1]/a/img')
img_phone.click()
time.sleep(2)

btn_change_img = driver.find_element('xpath','/html/body/div[2]/div/button[2]')
for i in range(0,2):
    btn_change_img.click()
    time.sleep(2)

#Guardar screenshoot
driver.save_screenshot('Screenshot' + str(random.randint(0,100)) + '.png')

btn_close_img = driver.find_element('xpath','/html/body/div[2]/div/div[1]/div/button')
btn_close_img.click()
time.sleep(1)

phone_cant = driver.find_element('xpath','//*[@id="input-quantity"]')
phone_cant.clear()
phone_cant.send_keys(2)
btn_add_car = driver.find_element('xpath','//*[@id="button-cart"]')
btn_add_car.click()
time.sleep(3)

#otro identificador para laptos es //a[text()="Laptops & Notebooks"]
laptops = driver.find_element('xpath','//*[@id="menu"]/div[2]/ul/li[2]/a')
mouse = ActionChains(driver)
mouse.move_to_element(laptops).perform()

#otro identificador para laptos_choose es //a[text()="Show All Laptops & Notebooks"]
laptops_choose = driver.find_element('xpath','//*[@id="menu"]/div[2]/ul/li[2]/div/a')
laptops_choose.click()
time.sleep(1)

hp_laptop = driver.find_element('xpath','//*[@id="content"]/div[4]/div[1]/div/div[2]/div[1]/h4/a')
hp_laptop.click()
time.sleep(1)

#Seleccionar como fecha diciembre 31 2022
btn_date= driver.find_element('xpath','//*[@id="product"]/div[1]/div/span/button')
btn_date.click()

mes = driver.find_element('xpath','//th[@class="picker-switch"]')
btn_next_click_calendar = driver.find_element('xpath','/html/body/div[4]/div/div[1]/table/thead/tr[1]/th[3]')
#escoger mes/año
while mes.text != 'December 2022' :
    btn_next_click_calendar.click()
time.sleep(1)
#seleccionar día 31
dia = driver.find_element('xpath','//td[text()="31"]')
dia.click()
time.sleep(1)

btn_add_car2=driver.find_element('xpath','//*[@id="button-cart"]')
btn_add_car2.click()
time.sleep(2)

btn_items_buyed = driver.find_element('xpath','//*[@id="cart"]/button')
btn_items_buyed.click()
time.sleep(1)

btn_checkout = driver.find_element('xpath','//*[@id="cart"]/ul/li[2]/div/p/a[2]/strong')
btn_checkout.click()
time.sleep(1)

# Cancelar compra de celular por falta en el inventario
no_product_phone = driver.find_element('xpath','//*[@id="checkout-cart"]/div[1]')
if no_product_phone.is_displayed:
    btn_cancel = driver.find_element('xpath','//*[@id="content"]/form/div/table/tbody/tr[1]/td[4]/div/span/button[2]')
    btn_cancel.click()
time.sleep(1)

btn_checkout2 = driver.find_element('xpath','//*[@id="content"]/div[3]/div[2]/a')
btn_checkout2.click()
time.sleep(2)

guest_checkout = driver.find_element('xpath','//*[@id="collapse-checkout-option"]/div/div/div[1]/div[2]/label/input')
guest_checkout.click()

btn_continue = driver.find_element('xpath','//*[@id="button-account"]')
btn_continue.click()
time.sleep(1)

billing_view = driver.find_element('xpath','//*[@id="collapse-payment-address"]/div')
billing_view.location_once_scrolled_into_view
time.sleep(1)

#datos para registro

excel_datos = r'C:\Users\royber\Desktop\Proyecto Selenium\datos.xlsx'
nombre = pandas.read_excel(excel_datos)

datos = pandas.read_excel(excel_datos)
nombre = str(datos['nombre'][0])
apellido=str(datos['apellido'][0])
correo= str(datos['email'][0])
telefono = str(datos['telefono'][0])
empresa = str(datos['empresa'][0])
dir1 = str(datos['dir1'][0])
ciudad = str(datos['ciudad'][0])
postal = str(datos['postal'][0])

first_name = driver.find_element('xpath','//*[@id="input-payment-firstname"]')
first_name.send_keys(nombre)

last_name = driver.find_element('xpath','//*[@id="input-payment-lastname"]')
last_name.send_keys(apellido)

email = driver.find_element('xpath','//*[@id="input-payment-email"]')
email.send_keys(correo)

phone = driver.find_element('xpath','//*[@id="input-payment-telephone"]')
phone.send_keys(telefono)

company = driver.find_element('xpath','//*[@id="input-payment-company"]')
company.send_keys(empresa)

direccion = driver.find_element('xpath','//*[@id="input-payment-address-1"]')
direccion.send_keys(dir1)

city = driver.find_element('xpath','//*[@id="input-payment-city"]')
city.send_keys(ciudad)

post_code = driver.find_element('xpath','//*[@id="input-payment-postcode"]')
post_code.send_keys(postal)

country = driver.find_element('xpath','//*[@id="input-payment-country"]')
dropdown_country = Select(country)
dropdown_country.select_by_value('47')
time.sleep(1)

zone = driver.find_element('xpath','//*[@id="input-payment-zone"]')
dropdown_zone = Select(zone)
dropdown_zone.select_by_value('738')
time.sleep(2)

btn_continue2 = driver.find_element('xpath','//*[@id="button-guest"]')
btn_continue2.click()
time.sleep(1)

comments_order = driver.find_element('xpath','//*[@id="collapse-shipping-method"]/div/p[4]/textarea')
comments_order.send_keys('Developed By Jhon Tafur')
time.sleep(2)

btn_continue3 = driver.find_element('xpath','//*[@id="button-shipping-method"]')
btn_continue3.click()
time.sleep(2)

terms = driver.find_element('xpath','//*[@id="collapse-payment-method"]/div/div[2]/div/input[1]')
terms.click()
time.sleep(1)

btn_continue4 = driver.find_element('xpath','//*[@id="button-payment-method"]')
btn_continue4.click()

# Uso de ExplicitWait
path_table = '//*[@id="collapse-checkout-confirm"]/div'
wait = WebDriverWait(driver,10)
wait.until(ec.visibility_of_element_located((By.XPATH,path_table)))

# Mostrar el precio total
final_price = driver.find_element('xpath','//table[@class="table table-bordered table-hover"]/tfoot/tr[3]/td[2]')
print('El precio total de la compra es: ' + final_price.text)
time.sleep(1)

btn_confirm_order = driver.find_element('xpath','//*[@id="button-confirm"]')
btn_confirm_order.click()
time.sleep(1)

success_text = driver.find_element('xpath','//*[@id="content"]/h1')
print(success_text.text)
time.sleep(3)