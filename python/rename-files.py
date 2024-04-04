import os
import re

# Define el directorio donde están los archivos a renombrar.
path = "/Users/piktonus97m/Downloads/february"

# Compila la expresión regular para identificar el patrón YYYYMMDD.
pattern = re.compile(r'(\d{4})(\d{2})(\d{2})')

# Recorre todos los archivos en el directorio.
for filename in os.listdir(path):
    # Busca el patrón en el nombre del archivo.
    match = pattern.search(filename)
    if match:
        # Crea el nuevo nombre de archivo con el formato YYYY.MM.DD.
        new_filename = pattern.sub(r'\1.\2.\3', filename)
        # Construye las rutas completas de los archivos antiguo y nuevo.
        old_file = os.path.join(path, filename)
        new_file = os.path.join(path, new_filename)
        # Renombra el archivo.
        os.rename(old_file, new_file)
        print(f'Renombrado: {filename} -> {new_filename}')
