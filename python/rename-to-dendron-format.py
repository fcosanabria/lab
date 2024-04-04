import os

# Define el directorio donde están los archivos a renombrar.
path = "/Users/piktonus97m/Downloads/Cursos/"

# Define el prefijo que quieres añadir a cada archivo.
prefijo = "universidad.uned.cursos."

# Recorre todos los archivos en el directorio especificado.
for filename in os.listdir(path):
    # Elimina los espacios en blanco, convierte a minúsculas y añade el prefijo.
    new_filename = prefijo + filename.replace(" ", "-").lower()
    
    # Construye las rutas completas de los archivos antiguo y nuevo.
    old_file = os.path.join(path, filename)
    new_file = os.path.join(path, new_filename)
    
    # Renombra el archivo.
    os.rename(old_file, new_file)
    print(f'Renombrado: {filename} -> {new_filename}')
