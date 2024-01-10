# Importamos el ModuMódulo
import os
from dotenv import load_dotenv
load_dotenv()
import pywhatkit 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Usamos Un try-except
try:
    num_message = os.getenv('NUM_MESSAGE') 
    num_movil = os.getenv('NUM_MOVIL') 
    message = os.getenv('MESSAGE') 
  # Enviamos el mensaje
    for i in range(num_message):
        pywhatkit.sendwhatmsg_instantly( num_movil ,  message ) 
    print("Mensaje Enviado " + num_message ) 

except: 

  print("No se envio el mensajes, Ocurrio Un Error")