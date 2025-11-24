import tkinter as tk

# --- Ventana principal ---
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.configure(bg="#e6f0ff")  # color suave azul claro

# --- Variables globales ---
numero_a = 0
numero_b = 0
operacion = "sumar"
resultado = 0
imagen_tk = None

# --- Espacio para la pantalla ---
espacio_util = tk.Frame(ventana, width=300, height=100, bg="#e6f0ff")
espacio_util.grid(row=0, column=0, columnspan=5, pady=10)

# --- Funciones de operaciones ---
def multiplicar(): return numero_a * numero_b
def dividir(): return numero_a / numero_b
def sumar(): return numero_a + numero_b
def restar(): return numero_a - numero_b

def borrar():
    pantalla.config(image=None, text="Error")
    pantalla.image = None

def mostrar_en_pantalla(valor):
    texto_actual = pantalla.cget("text")
    pantalla.config(text=texto_actual + str(valor))

def seleccionar_operacion(simbolo):
    global numero_a, operacion
    numero_a = float(pantalla.cget("text"))
    pantalla.config(text="")
    if simbolo == "*":
        operacion = "multiplicar"
    elif simbolo == "/":
        operacion = "dividir"
    elif simbolo == "+":
        operacion = "sumar"
    else:
        operacion = "restar"

def resultado_final():
    global numero_a, numero_b, resultado, imagen_tk
    numero_b = float(pantalla.cget("text"))
    if operacion == "sumar":
        resultado = sumar()
    elif operacion == "restar":
        resultado = restar()
    elif operacion == "multiplicar":
        resultado = multiplicar()
    elif operacion == "dividir":
        if numero_b == 0:
            pantalla.config(text="Error: ÷0")
            return
        resultado = dividir()
    pantalla.config(text=str(resultado))

# --- Pantalla ---
pantalla = tk.Label(
    espacio_util,
    anchor="e",
    width=18,
    height=2,
    font=("Consolas", 20),
    bg="#d9e6f2",
    fg="#003366",
)
pantalla.pack(fill="both", expand=True)

# --- Botones numéricos ---
botones_pf = [7, 8, 9]
botones_sf = [4, 5, 6]
botones_tf = [1, 2, 3]

# --- Estilos ---
color_num = "#b3d1ff"
color_op = "#6699cc"
color_error = "#ff6666"

# --- Filas de botones ---
for i, numero in enumerate(botones_pf):
    tk.Button(
        ventana,
        text=str(numero),
        font=("Arial", 12, "bold"),
        bg=color_num,
        width=8,
        command=lambda n=numero: mostrar_en_pantalla(n)
    ).grid(row=1, column=i, padx=5, pady=5)

for i, numero in enumerate(botones_sf):
    tk.Button(
        ventana,
        text=str(numero),
        font=("Arial", 12, "bold"),
        bg=color_num,
        width=8,
        command=lambda n=numero: mostrar_en_pantalla(n)
    ).grid(row=2, column=i, padx=5, pady=5)

for i, numero in enumerate(botones_tf):
    tk.Button(
        ventana,
        text=str(numero),
        font=("Arial", 12, "bold"),
        bg=color_num,
        width=8,
        command=lambda n=numero: mostrar_en_pantalla(n)
    ).grid(row=3, column=i, padx=5, pady=5)

# --- Última fila ---
tk.Button(ventana, text="0", font=("Arial", 12, "bold"), bg=color_num, width=8, command=lambda: mostrar_en_pantalla(0)).grid(row=4, column=1, padx=5, pady=5)
tk.Button(ventana, text="=", font=("Arial", 12, "bold"), bg=color_op, fg="white", width=8, command=resultado_final).grid(row=4, column=2, padx=5, pady=5)

# --- Botón "Error" que ocupa toda la columna 4 ---
tk.Button(ventana, text="Eliminar", font=("Arial", 12, "bold"), bg=color_error, fg="white", width=8, height=5, command=borrar).grid(row=1, column=4, rowspan=4, padx=5, pady=5)

# --- Botones de operaciones ubicados en distintas zonas ---
tk.Button(ventana, text="+", font=("Arial", 12, "bold"), bg=color_op, fg="white", width=8, command=lambda: seleccionar_operacion("+")).grid(row=1, column=5, padx=5, pady=5)
tk.Button(ventana, text="-", font=("Arial", 12, "bold"), bg=color_op, fg="white", width=8, command=lambda: seleccionar_operacion("-")).grid(row=2, column=5, padx=5, pady=5)
tk.Button(ventana, text="×", font=("Arial", 12, "bold"), bg=color_op, fg="white", width=8, command=lambda: seleccionar_operacion("*")).grid(row=3, column=5, padx=5, pady=5)
tk.Button(ventana, text="÷", font=("Arial", 12, "bold"), bg=color_op, fg="white", width=8, command=lambda: seleccionar_operacion("/")).grid(row=4, column=5, padx=5, pady=5)

ventana.mainloop()
