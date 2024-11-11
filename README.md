# Tiempo

Código simple que hace uso de la `Librería` de Google para la lectura de la hora en voz alta.


### Requisitos
- Linux
- Python 3 / pip 3
- gTTS
- VLC
- PulseAudio
- cron

#### Instrucciones:
1. Clonar el repositorio y dirigirse al directorio:
   ```
   git clone https://github.com/GeraMaldonado/.tiempo.git
   cd .tiempo/
   ```
2. Instalar la librería gTTS a través de pip3 _(Recomendación: instalar en un entorno virtual `venv`)_:
   ```
   pip3 install gtts
   ```
3. Instalar VLC, PulseAudio y cron:
   ```
   sudo apt-get install vlc pulseaudio cron
   ```
4. Crear archivo `.sh` con este contenido:
   - _Con librerías en `venv`_
   ```
   #!/bin/bash

   cd "$(dirname "$0")"    # Navegar al directorio del script

   source ./venv/bin/activate    # Activar el entorno virtual

   python3 tiempo.py    # Ejecutar el .py

   cvlc --play-and-close tiempo.mp3    # Reproducir el archivo MP3 sin interfaz gráfica

   deactivate    # Desactivar el entorno virtual

   ```
   - _Con  librerías `globales`_

   ```
   #!/bin/bash

   cd "$(dirname "$0")"    # Navegar al directorio del script

   python3 tiempo.py    # Ejecutar el .py

   cvlc --play-and-close tiempo.mp3    # Reproducir el archivo MP3 sin interfaz gráfica

   ```
   
6. Dar permisos de ejecución al archivo `.sh` y verificar su funcionamiento:
   ```
   sudo chmod +x "archivo".sh
   ./"archivo".sh
   ```
7. Editar cron para que el archivo se ejecute a un intervalo específico:
   - ingresar a modo edicion de cron:
   ```
   crontab -e
   ```
   - al final ingresar la instruccion se puede 
   ```
   0 * * * * DISPLAY=:0  /"direccion"/"de"/.tiempo/tiempo.sh > /"direccion"/"de"/.tiempo/cron.log 2>&1
   ```
   - El `>` es opcional, y redirige la salida del cron a un archivo de log en caso de errores. Puedes omitirlo si no necesitas registro.


La configuración anterior ejecutará el script cada hora. Los asteriscos (`*`) representan diferentes unidades de tiempo: minuto, hora, día del mes, mes y día de la semana. En este caso, `0 * * * *` significa "a los 0 minutos de cada hora". También puedes usar otros valores, como `@reboot`, `@yearly`, `@monthly`, etc., para programar la ejecución en reinicios, por año, mes, semana, etc.

![image](https://github.com/user-attachments/assets/ed862454-fad0-4a13-9e89-7e0bd3ab7f7b)

Este es un código simple, más como un proyecto divertido pequeño y divertido, pero también es muy útil en mi día a día. Espero que te sea útil!
