# ISW Juan Amaya - Data Engineering

repositorio para registro de mis practicas respecto a la ruta de ingenieria de datos de Platzi y algún otro proyecto de practica más.

python
    algorithms
        algunos retos que me encontré por internet, son problemas que resolver con python
    cienciaDeDatos
        un curso de ciencia de datos de platzi, el curso fue muy básico, solo tiene unos recursos pero en local
    python avanzado
        curso de python avanzado: closures, decorators, generators, iterators, typing

matplotlib
    curso de platzi sobre la librería de graficaciçon matplotlib

seaborn
    curso de graficacion de platzi sobre seaborn

regular expressions
    curso de expresiones regulares, hay código muestra de un proyecto que trabajé.

webScrapping
    cursos de web scrapping con beatifoulsoup4, xpath, selenium, y scrapy

from datetime import date, timedelta, datetime
from email.message import EmailMessage
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoAlertPresentException, ElementNotInteractableException
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from dateutil.relativedelta import relativedelta

import argparse
import calendar
import csv
import gzip
import imghdr
import os
import pandas as pd
import re
import smtplib
import ssl
import sys
import shutil
import time
import random

chrome_options = Options()
if os.name != "nt": chrome_options.add_argument("--headless")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--window-size=1024,768")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("-allow-running-insecure-content")
chrome_options.add_argument(
    "--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36")
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches",["enable-automation"])
chrome_options.add_argument("--disable-blink-features")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument('--disable-infobars')
#para que aparezca en inglés
chrome_options.add_argument("--lang=en-GB")

print('Iniciando driver.')
driver = webdriver.Chrome(chrome_options=chrome_options,
                                  executable_path='C:\\chromedriver.exe')


driver.get("https://es.wikipedia.org/w/index.php?title=Anexo:Entidades_federativas_de_M%C3%A9xico_por_superficie,_poblaci%C3%B3n_y_densidad")


def r(de:int, a:int) -> int:
    """genera un randomint(@de, @a)"""
    return random.randint(de, a)

    
def duerme(sleep_time:int, stop:int = 0, msg:str = False) -> None:
    """dormirá durante @sleep_time + un randint(opcional) 
    
    dormirá durante @sleep_time por defecto, si @stop se especifican entonces 
    dormirá un randint(@sleep_time, @stop), en windows imprime cuanto va a dormir,
    y si @msg se especifica se concatena antes de el msg por defecto.
    """
    wait_time = random.randint(sleep_time, stop) if stop else sleep_time

    default_msg = f"Esperando {wait_time} sgs..."
    msg = f"{msg}. {default_msg}" if msg else default_msg

    if os.name == "nt":#imprime traza (solo en windows)
        print(msg)

    time.sleep(wait_time)


def click_por_xpath(driver, element:str, xpath:str, bilingual_xpath:str = "", sleep_time:int = 3, msg:str = ""):
    """encuentra un elemento del @driver por @xpath, le da click y duerme @sleeptime

    si @msg es dado hace un print con su contenido.

    si el @xpath original no encuentra elemento entonces intentará 
    con @bilingual_xpath, esto para dar soporte a más de un idioma.
    """

    if msg:
        print(msg)

    # 1 intenta dar click
    try:
        driver.find_element(By.XPATH, xpath).click()

    except NoSuchElementException:
        if bilingual_xpath:
            driver.find_element(By.XPATH, bilingual_xpath).click()
        else:
            raise Exception(f"Error, no se pudo localizar el elemento {element}")
        
    except Exception as e:
        print(e)
        driver.close()
        sys.exit(0)
    
    duerme(sleep_time)


def fill_input(driver, texto:str, element:str, xpath:str, bilingual_xpath:str = "", sleep_time:int = 3, msg:str = ""):
    """encuentra un input del @driver por @xpath, limpia, escribe y duerme @sleeptime
    
    si @msg es dado hace un print con su contenido.
    
    encuentra un input del @driver por @xpath, limpia el contenido 
    y escribe @texto, duerme @sleep_time

    si el @xpath original no encuentra elemento entonces intentará 
    con @bilingual_xpath, esto para dar soporte a más de un idioma.
    """

    if msg:
        print(msg)

    # 1 intenta dar click
    try:
        input_txt = driver.find_element(By.XPATH, xpath)
        input_txt.clear()
        duerme(1)
        input_txt.send_keys(texto)

    except NoSuchElementException:
        if bilingual_xpath:
            input_txt = driver.find_element(By.XPATH, bilingual_xpath)
            input_txt.clear()
            duerme(1)
            input_txt.send_keys(texto)
        else:
            raise Exception(f"Error, no se pudo localizar el elemento {element}")
        
    except Exception as e:
        print(e)
        driver.close()
        sys.exit(0)
    
    duerme(sleep_time)

click_por_xpath(driver=driver, element="Acceder", xpath='//span[text()="Acceder"]',  
                sleep_time = r(3,6), msg="Iniciando proceso para iniciar sesión")

fill_input(driver=driver, texto="cristobalgarzalazar", element="Usuario", 
           xpath='//input[@id="wpName1"]', sleep_time=2, msg="Ingresando claves de acceso" )

fill_input(driver=driver, texto="pruebaai27", element="contraseña", 
           xpath='//input[@id="wpPassword1"]', sleep_time=2 )

click_por_xpath(driver=driver, element="Ingresar", xpath='//button[text()="Acceder"]',  
                sleep_time = r(5,9))

try:
    driver.find_element(By.XPATH, '//*[contains(text(), "contraseña que proporcionaste son incorrectos")]')
    raise Exception("Error de acceso")
except NoSuchElementException:
    print("Acceso correcto")
