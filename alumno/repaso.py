
import tkinter as tk

# Función para multiplicar el número ingresado por 2
def multiplicar():
    numero = entrada.get()  # Obtener el valor ingresado por el usuario
    try:
        resultado = float(numero) * 2  
        etiqueta_resultado.config(text=f"Resultado: {resultado}")  # Mostrar el resultado
    except ValueError:
        etiqueta_resultado.config(text="Por favor, ingresa un número válido")  

# Crear la ventana principal
root = tk.Tk()
root.title("Multiplicador de Números")
root.geometry("300x200")

# Crear widgets
etiqueta_instrucciones = tk.Label(root, text="Ingresa un número:", font=('Arial', 14))
entrada = tk.Entry(root, font=('Arial', 14), width=10)
boton = tk.Button(root, text="Multiplicar por 2", command=multiplicar, font=('Arial', 14))

# Colocar widgets en la ventana
etiqueta_instrucciones.pack(pady=10)
entrada.pack(pady=10)
boton.pack(pady=10)

# Crear una etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(root, text="", font=('Arial', 14))
etiqueta_resultado.pack(pady=10)

# Iniciar el loop de la ventana
root.mainloop()