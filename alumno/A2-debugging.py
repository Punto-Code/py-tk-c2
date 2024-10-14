import tkinter as tk

def saludo_personalizado():
    nombre = entrada.get()  # Obtiene el texto ingresado en el cuadro de texto
    resultado.config(text=f"¡Hola, {nombre}!")  # Cambia el texto de la etiqueta

# Crear la ventana principal
root = tk.Tk()
root.title("Saludo Personalizado")
root.geometry("300x200")

# Crear una etiqueta para ingresar nombre
etiqueta = tk.Label(root, text="Ingresa tu nombre:", font=('Arial', 14))
etiqueta.pack(pady=10)

# Crear un cuadro de texto para que el usuario ingrese su nombre
entrada = tk.Entry(root, font=('Arial', 14), width=20)
entrada.pack(pady=10)

### Crear un botón que llame a la función saludo_personalizado
boton = tk.Button(root, text="Saludar", font=('Arial', 14))
boton.pack(pady=10)

# Crear una etiqueta que mostrará el saludo
resultado = tk.Label(root, text="", font=('Arial', 14))
resultado.pack(pady=10)
