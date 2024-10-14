import tkinter as tk

# Función para convertir metros a kilómetros
def metros_a_kilometros():
    try:
        metros = float(entrada.get())
        kilometros = metros / 1000
        etiqueta_resultado.config(text=f"{metros} metros = {kilometros} kilómetros")
    except ValueError:
        etiqueta_resultado.config(text="Por favor, ingresa un número válido")

# Función para convertir gramos a kilogramos
def gramos_a_kilogramos():
    try:
        gramos = float(entrada.get())
        kilogramos = gramos / 1000
        etiqueta_resultado.config(text=f"{gramos} gramos = {kilogramos} kilogramos")
    except ValueError:
        etiqueta_resultado.config(text="Por favor, ingresa un número válido")

# Función para convertir minutos a horas
def minutos_a_horas():
    try:
        minutos = float(entrada.get())
        horas = minutos / 60
        etiqueta_resultado.config(text=f"{minutos} minutos = {horas:.2f} horas")
    except ValueError:
        etiqueta_resultado.config(text="Por favor, ingresa un número válido")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Conversor de Unidades")
ventana.geometry("400x300")

# Etiqueta de instrucciones
etiqueta_instrucciones = tk.Label(ventana, text="Ingresa el valor a convertir:", font=('Arial', 14))
etiqueta_instrucciones.pack(pady=10)

# Cuadro de texto para ingresar el valor
entrada = tk.Entry(ventana, font=('Arial', 14), width=10)
entrada.pack(pady=5)

# Botones para cada conversión
boton_metros_km = tk.Button(ventana, text="Metros a Kilómetros", command=metros_a_kilometros, font=('Arial', 14))
boton_metros_km.pack(pady=5)

boton_gramos_kg = tk.Button(ventana, text="Gramos a Kilogramos", command=gramos_a_kilogramos, font=('Arial', 14))
boton_gramos_kg.pack(pady=5)

boton_minutos_horas = tk.Button(ventana, text="Minutos a Horas", command=minutos_a_horas, font=('Arial', 14))
boton_minutos_horas.pack(pady=5)

boton_celsius_fahrenheit = tk.Button(ventana, text="Celsius a Fahrenheit", font=('Arial', 14))
boton_celsius_fahrenheit.pack(pady=5)

# Etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="", font=('Arial', 14))
etiqueta_resultado.pack(pady=10)

# Mantener la ventana abierta
ventana.mainloop()