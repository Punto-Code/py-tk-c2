# Conversor de Unidades con Tkinter

¡Bienvenidos! En este proyecto crearás una aplicación en Python usando **Tkinter** que convertirá diferentes unidades (metros, gramos, minutos y grados Celsius) a otras unidades correspondientes. El objetivo es que, mediante una serie de desafíos, vayas construyendo la aplicación paso a paso.

## Requisitos

- Conocimientos básicos de Python y Tkinter.
- Tkinter debe estar importado correctamente antes de empezar.

## Demo del Proyecto

[¡Mira la demostración del proyecto aquí!](https://youtu.be/Iil2K-zCpQ0)

[![Ver la demo en YouTube](https://img.youtube.com/vi/Iil2K-zCpQ0/0.jpg)](https://youtu.be/Iil2K-zCpQ0)

  
## Desafíos

### Challenge 1: Crear la interfaz
En este desafío, deberás construir la **interfaz gráfica** para la aplicación. Asegúrate de que contenga los siguientes elementos:

1. Una ventana principal.
2. Una etiqueta que dé instrucciones.
3. Un cuadro de texto donde el usuario pueda ingresar un valor.
4. Botones para realizar cada conversión.
5. Una etiqueta donde se mostrará el resultado.

### Challenge 2: Conversor metros a kilómetros
Ahora, crea la funcionalidad que convierta **metros** a **kilómetros**.

1. Define la función `metros_a_kilometros()`.
2. Usa el valor del cuadro de texto con `get()`.
3. Aplica la fórmula para la conversión: `kms = metros / 1000`.
4. Actualiza la etiqueta de resultado con `config()` para mostrar el valor convertido.

### Challenge 3: Conversor gramos a kilogramos
Crea la funcionalidad para convertir **gramos** a **kilogramos**.

1. Define la función `gramos_a_kilogramos()`.
2. Usa `get()` para obtener el valor ingresado.
3. Aplica la fórmula: `kg = gramos / 1000`.
4. Muestra el resultado usando `config()` en la etiqueta.

### Challenge 4: Conversor minutos a horas
Haz que tu aplicación convierta **minutos** a **horas**.

1. Define la función `minutos_a_horas()`.
2. Obtén el valor del cuadro de texto.
3. Convierte minutos a horas con la fórmula: `horas = minutos / 60`.
4. Actualiza la etiqueta de resultado para mostrar las horas, limitando el valor a dos decimales.

### Challenge 5: Conversor Celsius a Fahrenheit
Por último, implementa la funcionalidad para convertir **Celsius** a **Fahrenheit**.

1. Define la función `celsius_a_fahrenheit()`.
2. Usa `get()` para obtener el valor en Celsius.
3. Aplica la fórmula: `fahrenheit = (celsius * 9/5) + 32`.
4. Muestra el resultado usando `config()` en la etiqueta.

---

### Pistas adicionales:
- Asegúrate de que cada botón esté correctamente vinculado a la función correspondiente mediante el parámetro `command`.
- Utiliza el bloque `try-except` si es necesario para manejar entradas inválidas.

---

¡Buena suerte! Usa tu conocimiento de **Tkinter** y **Python** para completar los desafíos y crear tu conversor de unidades.