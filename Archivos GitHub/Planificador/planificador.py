import tkinter as tk
import calendar
from datetime import datetime, timedelta

# Ventana principal
ventana = tk.Tk()
ventana.title("Planificador de Turnos Simple")
ventana.geometry("750x550")
ventana.config(bg="#F0F0F0")

# Variables básicas
anio = datetime.now().year
mes = datetime.now().month

# Días de trabajo y descanso
dias_trabajo = 4
dias_descanso = 4

# Fecha de inicio del turno
fecha_inicio = datetime(2025, 10, 18)

# Etiqueta de título
titulo = tk.Label(ventana, text="Planificador de Turnos", font=("Arial", 20, "bold"), bg="#F0F0F0")
titulo.pack(pady=10)

# Marco para botones y entrada
marco_config = tk.Frame(ventana, bg="#F0F0F0")
marco_config.pack(pady=5)

tk.Label(marco_config, text="Días de trabajo:", bg="#F0F0F0").grid(row=0, column=0, padx=5)
entrada_trabajo = tk.Entry(marco_config, width=5)
entrada_trabajo.insert(0, str(dias_trabajo))
entrada_trabajo.grid(row=0, column=1, padx=5)

tk.Label(marco_config, text="Días de descanso:", bg="#F0F0F0").grid(row=0, column=2, padx=5)
entrada_descanso = tk.Entry(marco_config, width=5)
entrada_descanso.insert(0, str(dias_descanso))
entrada_descanso.grid(row=0, column=3, padx=5)

tk.Label(marco_config, text="Inicio (YYYY-MM-DD):", bg="#F0F0F0").grid(row=0, column=4, padx=5)
entrada_inicio = tk.Entry(marco_config, width=12)
entrada_inicio.insert(0, fecha_inicio.strftime("%Y-%m-%d"))
entrada_inicio.grid(row=0, column=5, padx=5)

# Marco del calendario
marco_calendario = tk.Frame(ventana, bg="#F0F0F0")
marco_calendario.pack(pady=10)

# Etiqueta para mostrar mes y año
etiqueta_mes = tk.Label(ventana, text="", font=("Arial", 14, "bold"), bg="#F0F0F0")
etiqueta_mes.pack()

# Función para mostrar calendario
def mostrar_calendario():
    for widget in marco_calendario.winfo_children():
        widget.destroy()

    global dias_trabajo, dias_descanso, fecha_inicio
    try:
        dias_trabajo = int(entrada_trabajo.get())
        dias_descanso = int(entrada_descanso.get())
        fecha_inicio = datetime.strptime(entrada_inicio.get(), "%Y-%m-%d")
    except:
        tk.messagebox.showerror("Error", "Revisa los valores ingresados")
        return

    nombre_mes = calendar.month_name[mes]
    etiqueta_mes.config(text=f"{nombre_mes} {anio}")

    # Cabecera de días
    dias_semana = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]
    for i, d in enumerate(dias_semana):
        tk.Label(marco_calendario, text=d, width=10, bg="#D9D9D9", font=("Arial", 10, "bold")).grid(row=0, column=i, padx=2, pady=2)

    # Calcular patrón
    patron = []
    for i in range(dias_trabajo):
        patron.append("T")  # Trabajo
    for i in range(dias_descanso):
        patron.append("D")  # Descanso

    dias = calendar.monthcalendar(anio, mes)

    # Calcular desplazamiento según fecha de inicio
    inicio_mes = datetime(anio, mes, 1)
    diferencia = (inicio_mes - fecha_inicio).days
    inicio_patron = diferencia % len(patron)

    # Mostrar días
    for f, semana in enumerate(dias):
        for c, dia in enumerate(semana):
            if dia == 0:
                tk.Label(marco_calendario, text="", width=10, height=2, bg="#F0F0F0").grid(row=f+1, column=c)
            else:
                tipo = patron[(inicio_patron + dia - 1) % len(patron)]
                if tipo == "T":
                    color = "#A3E4A3"  # verde trabajo
                    texto = f"{dia}\nTrabajo"
                else:
                    color = "#F5A9A9"  # rojo descanso
                    texto = f"{dia}\nDescanso"
                tk.Label(marco_calendario, text=texto, width=10, height=3, bg=color, relief="groove").grid(row=f+1, column=c, padx=2, pady=2)

# Funciones para cambiar mes
def mes_siguiente():
    global mes, anio
    mes += 1
    if mes > 12:
        mes = 1
        anio += 1
    mostrar_calendario()

def mes_anterior():
    global mes, anio
    mes -= 1
    if mes < 1:
        mes = 12
        anio -= 1
    mostrar_calendario()

# Botones de navegación
marco_botones = tk.Frame(ventana, bg="#F0F0F0")
marco_botones.pack(pady=5)
tk.Button(marco_botones, text="◀ Mes anterior", command=mes_anterior, width=15).grid(row=0, column=0, padx=10)
tk.Button(marco_botones, text="Actualizar", command=mostrar_calendario, width=15).grid(row=0, column=1, padx=10)
tk.Button(marco_botones, text="Mes siguiente ▶", command=mes_siguiente, width=15).grid(row=0, column=2, padx=10)

# Leyenda
tk.Label(ventana, text="🟩 Trabajo   🟥 Descanso", font=("Arial", 10), bg="#F0F0F0").pack(pady=5)

# Mostrar calendario inicial
mostrar_calendario()

# Ejecutar programa
ventana.mainloop()

