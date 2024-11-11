import time
from gtts import gTTS

def tiempo():
    horaActual = time.strftime("%I:%M %p")
    soloHora = int(time.strftime("%I"))
    if( soloHora == 1):
        mensaje = f"Es la {horaActual}"
    else:
        mensaje = f"Son las {horaActual}"
    tts = gTTS(mensaje, lang='es')
    tts.save('tiempo.mp3')

tiempo()
