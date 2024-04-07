from PIL import Image
import os

# Directorio que contiene las imágenes a optimizar
input_dir = '/home/jorge/Escritorio/imagenes/'

# Directorio de salida para las imágenes optimizadas
output_dir = '/home/jorge/Escritorio/optimizado/'

# Lista de extensiones de archivo de imagen admitidas
allowed_extensions = ('.jpg', '.jpeg', '.png')

# Factor de compresión para JPEG (0 significa sin compresión y 100 es máxima compresión)
jpeg_quality = 70

# Tamaño máximo para las imágenes redimensionadas (en píxeles)
max_width = 900
max_height = 700

# Iterar sobre todos los archivos en el directorio de entrada
for filename in os.listdir(input_dir):
    # Obtener la ruta completa del archivo
    input_path = os.path.join(input_dir, filename)
    
    # Verificar si el archivo es una imagen admitida
    if filename.endswith(allowed_extensions):
        # Abrir la imagen usando Pillow
        with Image.open(input_path) as img:
            # Redimensionar la imagen si es necesario
            img.thumbnail((max_width, max_height))

            
            # Guardar la imagen optimizada en el directorio de salida
            output_path = os.path.join(output_dir, filename)
            img.save(output_path, quality=jpeg_quality if filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg') else None)
            print(f'Imagen optimizada: {output_path}')
    else:
        print(f'Formato de archivo no admitido: {filename}')
