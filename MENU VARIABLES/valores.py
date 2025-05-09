import os  # Para trabajar con archivos, rutas y abrir el archivo

# Función para verificar si un número es primo
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Función para ingresar un número primo válido
def ingresar_primo():
    while True:
        try:
            numero = int(input("Ingrese un número entero positivo primo: "))
            if numero > 0 and es_primo(numero):
                print(f"✔ {numero} es un número primo válido.")
                return numero
            else:
                print("✖ El número no es primo o no es positivo.")
        except ValueError:
            print("✖ Entrada inválida. Debes ingresar un número entero.")

# Función para ingresar una cadena de texto
def ingresar_cadena():
    cadena = input("Ingrese una cadena de caracteres: ")
    print(f"✔ Cadena ingresada: '{cadena}'")
    return cadena

# Función para ingresar un valor vacío o con espacios
def ingresar_vacio_o_espacios():
    cadena = input("Ingrese un valor (puede estar vacío o solo contener espacios): ")
    if cadena.strip() == "":
        print("✔ El valor está vacío o solo tiene espacios.")
    else:
        print("✖ El valor contiene caracteres visibles.")
    return cadena

# Función para ingresar un número decimal
def ingresar_decimal():
    while True:
        try:
            decimal = float(input("Ingrese un número decimal: "))
            print(f"✔ Número decimal ingresado: {decimal}")
            return decimal
        except ValueError:
            print("✖ Entrada inválida. Debes ingresar un número decimal.")

# Función para guardar las variables en un archivo dentro de la carpeta "MENU VARIABLES"
def guardar_en_archivo(var1, var2, var3, var4):
    try:
        # Crear la carpeta si no existe
        carpeta = "MENU VARIABLES"
        os.makedirs(carpeta, exist_ok=True)

        # Ruta completa del archivo
        nombre_archivo = "valores_guardados.txt"
        ruta_completa = os.path.join(carpeta, nombre_archivo)

        # Guardar los valores en el archivo
        with open(ruta_completa, "w", encoding="utf-8") as archivo:
            archivo.write("=== VALORES INGRESADOS ===\n")
            archivo.write(f"var1 (Número primo): {var1}\n")
            archivo.write(f"var2 (Cadena de texto): {repr(var2)}\n")
            archivo.write(f"var3 (Vacío o espacios): {repr(var3)}\n")
            archivo.write(f"var4 (Número decimal): {var4}\n")

        # Mostrar ruta absoluta del archivo
        ruta_absoluta = os.path.abspath(ruta_completa)
        print(f"\n✔ Archivo guardado exitosamente en:\n{ruta_absoluta}")

        # Abrir automáticamente el archivo (solo en Windows)
        os.startfile(ruta_absoluta)

    except Exception as e:
        print(f"✖ Error al guardar o abrir el archivo: {e}")

# Función principal con menú
def main():
    var1 = None
    var2 = None
    var3 = None
    var4 = None

    while True:
        print("\n===== MENÚ DE OPCIONES =====")
        print("1. Ingresar número primo")
        print("2. Ingresar cadena de texto")
        print("3. Ingresar valor vacío o con espacios")
        print("4. Ingresar número decimal")
        print("5. Mostrar variables ingresadas")
        print("6. Salir y guardar en archivo")

        opcion = input("Seleccione una opción (1-6): ")

        if opcion == "1":
            var1 = ingresar_primo()
        elif opcion == "2":
            var2 = ingresar_cadena()
        elif opcion == "3":
            var3 = ingresar_vacio_o_espacios()
        elif opcion == "4":
            var4 = ingresar_decimal()
        elif opcion == "5":
            print("\n=== VALORES INGRESADOS ===")
            print(f"var1 (Número primo): {var1}")
            print(f"var2 (Cadena de texto): {repr(var2)}")
            print(f"var3 (Vacío o espacios): {repr(var3)}")
            print(f"var4 (Número decimal): {var4}")
        elif opcion == "6":
            print("\nSaliendo del programa. Estos son los valores finales:")
            print(f"var1 (Número primo): {var1}")
            print(f"var2 (Cadena de texto): {repr(var2)}")
            print(f"var3 (Vacío o espacios): {repr(var3)}")
            print(f"var4 (Número decimal): {var4}")
            guardar_en_archivo(var1, var2, var3, var4)
            print("¡Hasta luego!")
            break
        else:
            print("✖ Opción no válida. Intente de nuevo.")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
