import tkinter as tk

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
boton_metros_km = tk.Button(ventana, text="Metros a Kilómetros", font=('Arial', 14))
boton_metros_km.pack(pady=5)

boton_gramos_kg = tk.Button(ventana, text="Gramos a Kilogramos", font=('Arial', 14))
boton_gramos_kg.pack(pady=5)

boton_minutos_horas = tk.Button(ventana, text="Minutos a Horas", font=('Arial', 14))
boton_minutos_horas.pack(pady=5)

boton_celsius_fahrenheit = tk.Button(ventana, text="Celsius a Fahrenheit", font=('Arial', 14))
boton_celsius_fahrenheit.pack(pady=5)

# Etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="", font=('Arial', 14))
etiqueta_resultado.pack(pady=10)

# Mantener la ventana abierta
ventana.mainloop()
