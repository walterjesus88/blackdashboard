from undetected_chromedriver   import Chrome, ChromeOptions
import pandas as pd
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import datetime
from datetime import datetime, timedelta
import os
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from selenium.webdriver.firefox.options import Options

# options = webdriver.ChromeOptions()
# options.add_argument('--no-sandbox')  
def find_element_key(path,sendkey,browser):
    while True:
        try:
            browser.find_element(By.XPATH,path).send_keys(sendkey)
            break
        except Exception as e:
            print(e)

    return browser

def find_element_key_enter(path,sendkey,browser):
    while True:
        try:
            b=browser.find_element(By.XPATH,path).send_keys(sendkey).send_keys('Keys.ENTER')
            time.sleep(1)
            b.click()
            break
        except Exception as e:
            print(e)

    return browser

def find_element_click(path,browser):
    while True:
        try:
            browser.find_element(By.XPATH,path).click()
            break
        except Exception as e:
            print(e)

    return browser

def find_element_inner_html(path,browser):
    while True:
        try:
            data = browser.find_element(By.XPATH,path).get_attribute("innerHTML")
            break
        except Exception as e:
            print(e)

    return data

#options = webdriver.ChromeOptions()
#options = Options()
#options.binary_location = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
#"C:\diendaonline\geckodriver.exe"
# ua = UserAgent()
# userAgent = ua.random
# print(userAgent)
#options.add_argument(f'user-agent={userAgent}')
#options.add_argument("--incognito")
#options.add_argument('--no-sandbox')
#prefs = {'download.default_directory' : 'C:\dina2\dina2\src\perf_filtro1'}
#options.add_experimental_option('prefs', prefs)
#options.add_argument("--headless")
#options = Options()
#options.add_argument("--disable-extensions")
#options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36")

#options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

chrome_options = ChromeOptions()
chrome_options.add_argument("--headless")
#chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--force-device-scale-factor=0.7")
chrome_driver_path='C:\\dina2\\dina2\\src\\chromedriver.exe'
driver = Chrome(executable_path=chrome_driver_path,chrome_options=chrome_options)
#driver.execute_script("document.body.style.zoom='80%'")


#driver = webdriver.Chrome(executable_path="C:\dina2\dina2\src\chromedriver.exe",chrome_options=options)
#driver = Chrome(use_subprocess=True,options)
time.sleep(3)
#driver = webdriver.Chrome(executable_path="C:\\diendaonline\\chromedriver.exe",chrome_options=options)
#driver = webdriver.Firefox(options=options, executable_path='C:\diendaonline\geckodriver.exe')

#driver = webdriver.Firefox(options=options,executable_path="C:\\diendaonline\\geckodriver.exe")

#driver.maximize_window()
#driver.get("https://accounts.google.com/")   
driver.get("https://lookerstudio.google.com/u/0/reporting/3fafde27-29f8-4f5d-a0f9-2395c501d6dd/page/p_orqnip6fmc")   

time.sleep(60)

find_element_key('/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input',"wjesus88@gmail.com",driver)
find_element_click('/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button',driver)

find_element_key('/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input','88theosys88',driver)
time.sleep(3)

#driver.get("https://lookerstudio.google.com/u/0/reporting/3fafde27-29f8-4f5d-a0f9-2395c501d6dd/page/p_orqnip6fmc") 
#                   '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button  
find_element_click('/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button',driver)
time.sleep(60)

time.sleep(3)

#zx= driver.find_element(By.XPATH,'/html/body/app-bootstrap/ng2-bootstrap/lego-router-outlet/reporting-view-manager/ng2-reporting-view/div/div[2]/div/ng2-reporting-plate/plate/div/div/div/div[1]/div/div/div/div/div/canvas-pancake-adapter/canvas-layout/div/div[1]/div/div/div/ng2-report/ng2-canvas-container/div/div[107]/ng2-canvas-component/div/div/div/div/kpimetric-wrapper/div/ng2-kpimetric/div/div[2]').get_attribute("innerHTML")

visitas=find_element_inner_html('/html/body/app-bootstrap/ng2-bootstrap/lego-router-outlet/reporting-view-manager/ng2-reporting-view/div/div[2]/div/ng2-reporting-plate/plate/div/div/div/div[1]/div/div/div/div/div/canvas-pancake-adapter/canvas-layout/div/div[1]/div/div/div/ng2-report/ng2-canvas-container/div/div[107]/ng2-canvas-component/div/div/div/div/kpimetric-wrapper/div/ng2-kpimetric/div/div[2]',driver)
                                 
#print(zx)
#print(visitas)

CR=find_element_inner_html('/html/body/app-bootstrap/ng2-bootstrap/lego-router-outlet/reporting-view-manager/ng2-reporting-view/div/div[2]/div/ng2-reporting-plate/plate/div/div/div/div[1]/div/div/div/div/div/canvas-pancake-adapter/canvas-layout/div/div[1]/div/div/div/ng2-report/ng2-canvas-container/div/div[105]/ng2-canvas-component/div/div/div/div/kpimetric-wrapper/div/ng2-kpimetric/div/div[2]',driver)

print(CR)

PEDIDOS=find_element_inner_html('/html/body/app-bootstrap/ng2-bootstrap/lego-router-outlet/reporting-view-manager/ng2-reporting-view/div/div[2]/div/ng2-reporting-plate/plate/div/div/div/div[1]/div/div/div/div/div/canvas-pancake-adapter/canvas-layout/div/div[1]/div/div/div/ng2-report/ng2-canvas-container/div/div[10]/ng2-canvas-component/div/div/div/div/kpimetric-wrapper/div/ng2-kpimetric/div/div[2]',driver)
print(PEDIDOS)


PREVENTAS=find_element_inner_html('/html/body/app-bootstrap/ng2-bootstrap/lego-router-outlet/reporting-view-manager/ng2-reporting-view/div/div[2]/div/ng2-reporting-plate/plate/div/div/div/div[1]/div/div/div/div/div/canvas-pancake-adapter/canvas-layout/div/div[1]/div/div/div/ng2-report/ng2-canvas-container/div/div[11]/ng2-canvas-component/div/div/div/div/kpimetric-wrapper/div/ng2-kpimetric/div/div[2]',driver)
print(PREVENTAS)


EFECT = find_element_inner_html('/html/body/app-bootstrap/ng2-bootstrap/lego-router-outlet/reporting-view-manager/ng2-reporting-view/div/div[2]/div/ng2-reporting-plate/plate/div/div/div/div[1]/div/div/div/div/div/canvas-pancake-adapter/canvas-layout/div/div[1]/div/div/div/ng2-report/ng2-canvas-container/div/div[12]/ng2-canvas-component/div/div/div/div/kpimetric-wrapper/div/ng2-kpimetric/div/div[2]',driver)
print(EFECT)

time.sleep(10)
###BUTTON desplegar datepicker
find_element_click('/html/body/app-bootstrap/ng2-bootstrap/lego-router-outlet/reporting-view-manager/ng2-reporting-view/div/div[2]/div/ng2-reporting-plate/plate/div/div/div/div[1]/div/div/div/div/div/canvas-pancake-adapter/canvas-layout/div/div[1]/div/div/div/ng2-report/ng2-canvas-container/div/div[89]/ng2-canvas-component/div/div/div/div/ga-date-range-picker-wrapper/ng2-date-range-picker/lego-date-duration-control/control-layout-wrapper/button',driver)
                  #'/html/body/app-bootstrap/ng2-bootstrap/lego-router-outlet/reporting-view-manager/ng2-reporting-view/div/div[2]/div/ng2-reporting-plate/plate/div/div/div/div[1]/div/div/div/div/div/canvas-pancake-adapter/canvas-layout/div/div[1]/div/div/div/ng2-report/ng2-canvas-container/div/div[89]/ng2-canvas-component/div/div/div/div/ga-date-range-picker-wrapper/ng2-date-range-picker/lego-date-duration-control/control-layout-wrapper/button
time.sleep(3)

find_element_click('/html/body/div[5]/div[1]/div[1]/md-select/md-select-value/span[2]',driver)
                   #'/html/body/div[5]/div[1]/div[1]/md-select/md-select-value/span[2]
#es opcion mes pasado
find_element_click('/html/body/div[7]/md-select-menu/md-content/md-option[16]',driver)

#button aplica
find_element_click('/html/body/div[5]/div[2]/button[1]',driver)

# #producto tipo
# find_element_click('//*[@id="body"]/div[2]/div/ng2-reporting-plate/plate/div/div/div/div[1]/div/div/div/div/div/canvas-pancake-adapter/canvas-layout/div/div[1]/div/div/div/ng2-report/ng2-canvas-container/div/div[97]/ng2-canvas-component/div/div/div/div/canvas-control-wrapper/ng2-canvas-control/canvas-control-host/control-layout-wrapper/button/div[1]/span[2]',driver)
# time.sleep(10)

# #movil
# find_element_click('/html/body/canvas-control-editor/div/div/div/list-control/div/md-virtual-repeat-container/div/div[2]/div[1]/md-checkbox',driver)
# #fijo
# find_element_click('/html/body/canvas-control-editor/div/div/div/list-control/div/md-virtual-repeat-container/div/div[2]/div[2]/md-checkbox',driver)

# time.sleep(30)

# #producto tipo deseleccionar
# find_element_click('//*[@id="body"]/div[2]/div/ng2-reporting-plate/plate/div/div/div/div[1]/div/div/div/div/div/canvas-pancake-adapter/canvas-layout/div/div[1]/div/div/div/ng2-report/ng2-canvas-container/div/div[97]/ng2-canvas-component/div/div/div/div/canvas-control-wrapper/ng2-canvas-control/canvas-control-host/control-layout-wrapper/button/div[1]/span[2]',driver)
# time.sleep(10)

# Obtén la altura de la ventana del navegador
#scroll
# scrolldown = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
# match=False
# while(match==False):
#     last_count = scrolldown
#     time.sleep(3)
#     scrolldown = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
#     if last_count==scrolldown:
#         match=True


# Desplazar hacia abajo usando JavaScript
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# # También puedes utilizar la biblioteca ActionChains para desplazarte
# # hasta el final de la página
# actions = ActionChains(driver)
# actions.send_keys(Keys.END).perform()
time.sleep(10)
# driver.execute_script("document.body.style.zoom='60%'")
# driver.execute_script("document.body.style.zoom='60%'")
# driver.execute_script("document.body.style.zoom='60%'")
# driver.execute_script("document.body.style.zoom='60%'")
time.sleep(10)

#ATM´PAGE
find_element_click('/html/body/app-bootstrap/ng2-bootstrap/lego-router-outlet/reporting-view-manager/ng2-reporting-view/div/div[2]/div/ng2-reporting-plate/plate/div/div/div/div[1]/div/div/div/div/div/canvas-pancake-adapter/canvas-layout/div/div[1]/div/div/div/ng2-report/ng2-canvas-container/div/div[65]/ng2-canvas-component/div/div/div/div/canvas-control-wrapper/ng2-canvas-control/canvas-control-host/control-layout-wrapper/button',driver)

time.sleep(5)

# etiqueta='#body > div.lego-reporting-view.activity-view.no-licensed.new-resizer > div > ng2-reporting-plate > plate > div > div > div > div:nth-child(1) > div > div > div > div > div > canvas-pancake-adapter > canvas-layout > div > div.mainBlockHolder > div > div > div > ng2-report > ng2-canvas-container > div > div:nth-child(65) > ng2-canvas-component > div > div > div > div > canvas-control-wrapper > ng2-canvas-control > canvas-control-host > control-layout-wrapper > button'

# driver.find_element(By.CSS_SELECTOR, etiqueta)

time.sleep(5)

#INPUT CANAL ONLINE  O CATALOGO
id='/html/body/canvas-control-editor/div/div/div/text-control/div/div/md-input-container/input'
find_element_key(id,'tiendaonline',driver)

#ATM´PAGE doble click
#find_element_click('/html/body/app-bootstrap/ng2-bootstrap/lego-router-outlet/reporting-view-manager/ng2-reporting-view/div/div[2]/div/ng2-reporting-plate/plate/div/div/div/div[1]/div/div/div/div/div/canvas-pancake-adapter/canvas-layout/div/div[1]/div/div/div/ng2-report/ng2-canvas-container/div/div[3]/ng2-canvas-component/div/div/div/div',driver)
time.sleep(2)

# #producto tipo
find_element_click('//*[@id="body"]/div[2]/div/ng2-reporting-plate/plate/div/div/div/div[1]/div/div/div/div/div/canvas-pancake-adapter/canvas-layout/div/div[1]/div/div/div/ng2-report/ng2-canvas-container/div/div[97]/ng2-canvas-component/div/div/div/div/canvas-control-wrapper/ng2-canvas-control/canvas-control-host/control-layout-wrapper/button/div[1]/span[2]',driver)
time.sleep(10)

#movil
find_element_click('/html/body/canvas-control-editor/div/div/div/list-control/div/md-virtual-repeat-container/div/div[2]/div[1]/md-checkbox',driver)
# #fijo
# find_element_click('/html/body/canvas-control-editor/div/div/div/list-control/div/md-virtual-repeat-container/div/div[2]/div[2]/md-checkbox',driver)


#find_element_click('/html/body/app-bootstrap/ng2-bootstrap/lego-router-outlet/reporting-view-manager/ng2-reporting-view/div/div[2]/div/ng2-reporting-plate/plate/div/div/div/div[1]/div/div/div/div/div/canvas-pancake-adapter/canvas-layout/div/div[1]/div/div/div/ng2-report/ng2-canvas-container/div/div[72]/ng2-canvas-component/div/div/div/div/canvas-control-wrapper/ng2-canvas-control/canvas-control-host/control-layout-wrapper/button',driver)
#time.sleep(2)
#find_element_click('/html/body/app-bootstrap/ng2-bootstrap/lego-router-outlet/reporting-view-manager/ng2-reporting-view/div/div[2]/div/ng2-reporting-plate/plate/div/div/div/div[1]/div/div/div/div/div/canvas-pancake-adapter/canvas-layout/div/div[1]/div/div/div/ng2-report/ng2-canvas-container/div/div[109]/ng2-canvas-component/div/div/div/div/canvas-control-wrapper/ng2-canvas-control/canvas-control-host/control-layout-wrapper/button',driver)

#esto es para el anio
#//*[@id="datepicker-674-9124-title"]

#boton anio izquierda                
#----- find_element_click('/html/body/div[5]/div[1]/div[2]/div[2]/table/thead/tr[1]/th[2]/button',driver)
#boton anio derecha                
#------find_element_click('/html/body/div[5]/div[1]/div[3]/div[2]/table/thead/tr[1]/th[2]/button',driver)
#find_element_click('/html/body/div[5s]/div[1]/div[3]/div[2]/table/tbody/tr[2]/td[3]/button',driver)
                    #/html/body/div[5]/div[1]/div[3]/div[2]/table/thead/tr[1]/th[2]/button

#driver.find_element(By.XPATH,'/html/body/div[8]/div[1]/div[2]/div[2]/table/thead/tr[1]/th[2]/button').click()
##button_b= driver.find_element(By.XPATH,'/html/body/div[8]/div[1]/div[3]/div[2]/table/thead/tr[1]/th[2]/button')#.click()


#find_element_click('//*[@id="body"]/div[2]/div/ng2-reporting-plate/plate/div/div/div/div[1]/div/div/div/div/div/canvas-pancake-adapter/canvas-layout/div/div[1]/div/div/div/ng2-report/ng2-canvas-container/div/div[89]/ng2-canvas-component/div/div/div/div/ga-date-range-picker-wrapper/ng2-date-range-picker/lego-date-duration-control/control-layout-wrapper/button/div[1]/span[1]/span[1]/main-section[text()="15 may 2023 - 29 may 2023"]',driver)
#path = '/html/body/div[5]/div[1]/div[2]/div[2]/table/thead/tr[1]/th[2]/button[strong()="Jun de 2023"]'
#driver.find_element(By.XPATH,path)

#button = driver.find_element_by_css_selector("#body > div.lego-reporting-view.activity-view.no-licensed.new-resizer > div > ng2-reporting-plate > plate > div > div > div > div:nth-child(1) > div > div > div > div > div > canvas-pancake-adapter > canvas-layout > div > div.mainBlockHolder > div > div > div > ng2-report > ng2-canvas-container > div > div:nth-child(89) > ng2-canvas-component > div > div > div > div > ga-date-range-picker-wrapper > ng2-date-range-picker > lego-date-duration-control > control-layout-wrapper > button")
#driver.execute_script("arguments[0].setAttribute('span', '15 may 2023 - 30 may 2023')", button)

# Espera hasta que el datepicker sea visible
# wait = WebDriverWait(driver, 10)
# datepicker = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'body > div.cd-jjqo4v9qsc.menulist')))
# datepicker.send_keys('2023-05-31')

#datepicker-258-3867-title
#estos son dias
#find_element_click('/html/body/div[5]/div[1]/div[2]/div[2]/table/tbody/tr[2]/td[5]/button',driver) #dia 11 mayo
                   #/html/body/div[5]/div[1]/div[2]/div[2]/table/tbody/tr[2]/td[2]/button #3 april  //*[@id="datepicker-258-8733-8"]/button  ##datepicker-258-8733-8 > button  
                   #/html/body/div[5]/div[1]/div[2]/div[2]/table/tbody/tr[2]/td[5]/button #6 april  //*[@id="datepicker-258-8733-11"]/button ##datepicker-258-8733-11 > button
                   #/html/body/div[5]/div[1]/div[2]/div[2]/table/tbody/tr[5]/td[5]/button #27 april //*[@id="datepicker-258-8733-32"]/button ##datepicker-258-8733-32 > button
                   #/html/body/div[5]/div[1]/div[2]/div[2]/table/tbody/tr[6]/td[1]/button #30 april //*[@id="datepicker-258-8733-35"]/button ##datepicker-258-8733-35 > button
                   #/html/body/div[5]/div[1]/div[2]/div[2]/table/tbody/tr[5]/td[4]/button #31 may   //*[@id="datepicker-258-8733-31"]/button ##datepicker-258-8733-31 > button
                                                                                                    #//*[@id="datepicker-258-8300-23"]/button
#find_element_click('/html/body/div[5]/div[1]/div[3]/div[2]/table/tbody/tr[5]/td[3]/button',driver) #dia 29 agosto
                    #/html/body/div[5]/div[1]/div[3]/div[2]/table/tbody/tr[4]/td[7]/button 27 may //*[@id="datepicker-259-8778-27"]/button ##datepicker-259-8778-27 > button
                    #/html/body/div[5]/div[1]/div[3]/div[2]/table/tbody/tr[5]/td[2]/button 29 may //*[@id="datepicker-259-8778-29"]/button ##datepicker-259-8778-29 > button
                    #/html/body/div[5]/div[1]/div[3]/div[2]/table/tbody/tr[5]/td[3]/button 30 may //*[@id="datepicker-259-8778-30"]/button ##datepicker-259-8778-30 > button //*[@id="datepicker-259-1736-30"]/button 
                    #/html/body/div[5]/div[1]/div[3]/div[2]/table/tbody/tr[5]/td[4]/button 31 may
                    #/html/body/div[5]/div[1]/div[3]/div[2]/table/tbody/tr[5]/td[2]/button 24 avril //*[@id="datepicker-259-8778-29"]/button //*[@id="datepicker-259-8778-29"]/button ##datepicker-259-8778-29 > button
                    #/html/body/div[5]/div[1]/div[3]/div[2]/table/tbody/tr[5]/td[4]/button 31 may
                    #/html/body/div[5]/div[1]/div[3]/div[2]/table/tbody/tr[5]/td[4]/button 31 may //*[@id="datepicker-259-1736-31"]/button

xo=find_element_inner_html('/html/body/app-bootstrap/ng2-bootstrap/lego-router-outlet/reporting-view-manager/ng2-reporting-view/div/div[2]/div/ng2-reporting-plate/plate/div/div/div/div[1]/div/div/div/div/div/canvas-pancake-adapter/canvas-layout/div/div[1]/div/div/div/ng2-report/ng2-canvas-container/div/div[89]/ng2-canvas-component/div/div/div/div/ga-date-range-picker-wrapper/ng2-date-range-picker/lego-date-duration-control/control-layout-wrapper/button/div[1]/span[1]/span[1]',driver)
                           
print(xo)
#elemento = str(xo).find_element(By.TAG_NAME, 'main-section')
#xo.find_element_by_css_selector('.dateLabel') 
#elemento.send_keys(Keys.BACKSPACE * len(elemento.text))
#elemento.send_keys('1 jun 2023 - 31 jun 2023')
#/html/body/div[8]/div[1]/div[2]/div[2]/table/tbody/tr[2]/td[5]/button
#/html/body/div[5]/div[1]/div[2]/div[2]/table/tbody/tr[2]/td[5]/button
#/html/body/div[8]/div[1]/div[2]/div[2]/table/tbody/tr[2]/td[5]/button

#dia_elemento = driver.find_element(By.CSS_SELECTOR, '#datepicker-258-6713-title') 
#dia_elemento.click()
time.sleep(50)

print('fxvxdxxbxbfb')
# find_element_click('/html/body/div[8]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[1]/button',driver) #january

# find_element_click('/html/body/div[8]/div[1]/div[2]/div[2]/table/tbody/tr[2]/td[3]/button',driver) #june

# ###datepicjer
# find_element_click('/html/body/div[10]/div[1]/div[2]/div[2]/table/thead/tr/th[2]/button',driver)
# find_element_click('/html/body/div[10]/div[1]/div[2]/div[2]/table/thead/tr/th[2]/button',driver)


# ##igual a 
# find_element_key('/html/body/canvas-control-editor/div/div/div/text-control/div/md-select','tiendaonline',driver)