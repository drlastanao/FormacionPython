import pathlib

try:
    file = pathlib.Path("files/one-million.txt")
    print(f"El archivo {file} existe.")
    datos= file.read_text()
    print(f"Los datos del archivo son: {datos}")

    if datos.find("314159") != -1:
        print("El número 314159 se encuentra en el archivo.")
    else:
        print("El número 314159 no se encuentra en el archivo.")

except Exception as e:
    print(f"Ocurrio la siguiente excepción: {e}")
