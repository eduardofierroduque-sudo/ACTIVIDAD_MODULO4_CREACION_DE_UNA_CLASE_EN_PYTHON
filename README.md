HOLA HOLA, AÑADI 2 ARCHIVO .PY EL PRIMERO ES LO SOLICITADO EN EL DOCUMENTO DE ACTIVIDAD, RESOLVIENDO EL CODIGO DE LA SIGUIENTE FORMA:
<img width="2329" height="976" alt="image" src="https://github.com/user-attachments/assets/048b7a7e-a0e0-45cb-9efa-1c9bfc4001da" />
<img width="2335" height="886" alt="image" src="https://github.com/user-attachments/assets/fb103088-091d-4142-bc9c-e992183602c0" />
<img width="2338" height="583" alt="image" src="https://github.com/user-attachments/assets/89bcb923-4ec2-4b5b-a9bd-0c48580225ad" />
DANDO COMO RESULTADO EN LA TERMINAL:
<img width="739" height="463" alt="image" src="https://github.com/user-attachments/assets/cb1bff6a-eb48-4dc9-8c3b-7b69d7fbd9a1" />

PERO NOTE QUE EL RESULTADO DEL LISTADO DE LOS LIBROS QUEDA PERDIDA MAS ALLA DE SOLO DARLA EN .PY ASIQUE DEFINI UN METODO DE __exportar_a_txr__ DENTRO DE LA CLASE __bibilioteca__
<img width="1754" height="940" alt="image" src="https://github.com/user-attachments/assets/67ee7799-922e-4ff5-b2aa-f2162e04fefd" />
<img width="1708" height="854" alt="image" src="https://github.com/user-attachments/assets/40b65441-018a-4601-ac15-ae1ed0997e8d" />
<img width="1757" height="620" alt="image" src="https://github.com/user-attachments/assets/07169597-0010-480b-9f33-1c42e594012d" />
<img width="1750" height="901" alt="image" src="https://github.com/user-attachments/assets/537779de-55aa-477c-8600-2d8a96a965c2" />
<img width="1426" height="604" alt="image" src="https://github.com/user-attachments/assets/ab00d480-8ee2-480c-8db0-2cff23656283" />
<img width="1730" height="895" alt="image" src="https://github.com/user-attachments/assets/9de609d2-439e-4653-b083-468077ec00a6" />

AÑADÍ UN BLOQUE DE CÓDIGO DENTRO DE LA CLASE BIBLIOTECA APROX ENTRE LA LINEA 43 Y 56 
ESTA ES LA LINEA QUE PERMITE LA EXPORTACIÓN:
# --- BLOQUE NUEVO: Método para exportar ---
    def exportar_a_txt(self, nombre_archivo="lista_biblioteca.txt"):
        try:
            with open(nombre_archivo, "w", encoding="utf-8") as archivo:
                archivo.write("REPORTE DE BIBLIOTECA\n")
                archivo.write("="*50 + "\n")
                for libro in self.libros:
                    archivo.write(f"TÍTULO: {libro.get_titulo()}\n")
                    archivo.write(f"AUTOR:  {libro.get_autor()}\n")
                    archivo.write(f"PÁGINAS: {libro.get_paginas()}\n")
                    archivo.write("-" * 30 + "\n")
            print(f"\n✅ Archivo '{nombre_archivo}' generado con éxito.")
        except Exception as e:
            print(f"Error al crear el archivo: {e}")
# Y FINALMENTE EN LA ULTIMA LINEA DEL CODIGO AÑADÍ LA INSTRUCCIÓN PARA GENERAR LA CREACIÓN DEL ARCHIVO

# --- LÍNEA NUEVA: Llamada a la exportación ---
    mi_biblioteca.exportar_a_txt("mis_libros.txt")


        






















