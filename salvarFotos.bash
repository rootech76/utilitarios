#bin/bash

#Mueve las fotos/imagenes  que serán guardadas en Google Fotos a un directorio previamente configurado para tal fin



echo "Iniciando Proceso...."
echo "Moviendo Imagenes de Whatsapp"

mv ./storage/shared/Pictures/Whatsapp/* ./storage/shared/Pictures/GoogleFotos/

echo "Hecho !!"

mv ./storage/shared/Pictures/Telegram/* ./GoogleFotos/

echo "Hecho"

echo "Proceso Finalizado con exito..!!"
