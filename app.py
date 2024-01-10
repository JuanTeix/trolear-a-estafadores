# Importamos el ModuMódulo

import pywhatkit 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Usamos Un try-except
try:
    num_message = 10000 
  # Enviamos el mensaje
    for i in range(num_message):
        pywhatkit.sendwhatmsg_instantly("+34656498443",  "Mensaje De Prueba" ) 
    print("Mensaje Enviado " + num_message ) 

except: 

  print("No se envio el mensajes, Ocurrio Un Error")