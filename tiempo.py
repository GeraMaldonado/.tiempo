import time
from gtts import gTTS
from playsound import playsound
#from os import remove

def tiempo():
    horaActual = time.strftime("%I:%M %p")
    soloHora = int(time.strftime("%I"))
    if( soloHora == 1):
        mensaje = f"Es la {horaActual}"
    else:
        mensaje = f"Son las {horaActual}"
    tts = gTTS(mensaje, lang='es')
    tts.save('tiempo.mp3')
    playsound('tiempo.mp3')
#    remove('tiempo.mp3')

tiempo()
