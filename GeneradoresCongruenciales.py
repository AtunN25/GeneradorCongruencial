import tkinter as tk
from tkinter import ttk

# Definir value globalmente
value = [[0, 0, 0, 0]] 

def button_callback():
    global value
    value = []  # Reiniciar `value` en cada llamada a la función

    # Obtener los valores de las entradas
    a = int(entry1.get())
    c = int(entry2.get())
    m = int(entry3.get())
    semilla_inicial = int(entry4.get())

    # Inicializar variables para la generación de números
    semilla_actual = semilla_inicial
    resultados = []
    valores_vistos = set()  # Usamos un conjunto para almacenar los números generados
    iteracion = 0

    while True:
        # Generamos el siguiente número
        nuevo_numero = (a * semilla_actual + c) % m
        
        # Verificamos si el número ya ha sido generado antes
        if nuevo_numero in valores_vistos:
            break
        
        # Agregamos el nuevo número al conjunto y a la lista de resultados
        valores_vistos.add(nuevo_numero)
        
        # Añadimos los datos de la iteración a `value`
        value.append([iteracion, semilla_actual, nuevo_numero, nuevo_numero / m])
        
        # Agregamos el número a la lista de resultados
        resultados.append(nuevo_numero)
        
        # Actualizamos la semilla actual
        semilla_actual = nuevo_numero
        iteracion += 1  # Incrementamos la iteración

    # Actualizar la tabla con los nuevos datos
    update_treeview()

    # Calcular y mostrar el periodo de vida
    periodo_vida = len(resultados)
    print(resultados)
    print(len(resultados))
    label_resultado.configure(text=f"El periodo de vida es: {periodo_vida}", fg="darkgreen")
    
    print(value)

def update_treeview():
    # Eliminar todas las filas existentes
    for row in treeview.get_children():
        treeview.delete(row)
    
    # Insertar nuevas filas en la tabla
    for i, row_data in enumerate(value):
        if i == len(value) - 1:  # Si es la última fila
            treeview.insert("", "end", values=row_data, tags=("highlight",))
        else:
            treeview.insert("", "end", values=row_data)
    
    # Configurar el estilo para la fila resaltada
    treeview.tag_configure("highlight", background="red", foreground="white")

# Crear la ventana principal
root = tk.Tk()
root.title("Ejemplo de Grid con Frame")
root.geometry("865x500")  # Ajusta la altura para el nuevo marco
root.configure(background='#7c1324')

# Crear Frames como contenedores
frame1 = tk.Frame(root, bg="black")
frame2 = tk.Frame(root, bg="darkblue")
frame3 = tk.Frame(root, bg="black")  # Nuevo marco para el resultado

# Colocar los Frames dentro de la cuadrícula y hacer que se expandan
frame1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
frame2.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
frame3.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")  # Añadir el nuevo marco

# Configurar el grid dentro de frame1
frame1.grid_columnconfigure(0, weight=1)
frame1.grid_columnconfigure(1, weight=3)  # Para darle más espacio a las entradas
frame1.grid_columnconfigure(2, weight=1)
frame1.grid_columnconfigure(3, weight=3)  # Para darle más espacio a las entradas

# Primer grupo de etiquetas y entradas
entries = []

label1 = tk.Label(frame1, text="Multiplicador (a):", fg="white", bg="black")
label1.grid(row=0, column=0, padx=5, pady=5, sticky="w")

entry1 = tk.Entry(frame1)
entry1.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
entries.append(entry1)

label2 = tk.Label(frame1, text="Incremento (c):", fg="white", bg="black")
label2.grid(row=1, column=0, padx=5, pady=5, sticky="w")

entry2 = tk.Entry(frame1)
entry2.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
entries.append(entry2)

# Segundo grupo de etiquetas y entradas
label3 = tk.Label(frame1, text="Modulo (m):", fg="white", bg="black")
label3.grid(row=0, column=2, padx=5, pady=5, sticky="w")

entry3 = tk.Entry(frame1)
entry3.grid(row=0, column=3, padx=5, pady=5, sticky="ew")
entries.append(entry3)

label4 = tk.Label(frame1, text="Semilla (x0):", fg="white", bg="black")
label4.grid(row=1, column=2, padx=5, pady=5, sticky="w")

entry4 = tk.Entry(frame1)
entry4.grid(row=1, column=3, padx=5, pady=5, sticky="ew")
entries.append(entry4)

# Crear y ubicar el botón
button1 = tk.Button(frame1, text="Procesar", command=button_callback, bg="darkgreen", fg="white")
button1.grid(row=2, column=0, columnspan=4, pady=10, padx=10, sticky="nsew")

# Configurar el grid dentro de frame2
frame2.grid_rowconfigure(0, weight=1)
frame2.grid_columnconfigure(0, weight=1)

# Crear y ubicar la tabla en frame2
treeview = ttk.Treeview(frame2, columns=("iteracion", "semilla", "nuevo_numero", "nuevo_numero/m"), show='headings')
treeview.heading("iteracion", text="Iteración")
treeview.heading("semilla", text="Semilla")
treeview.heading("nuevo_numero", text="Número Nuevo")
treeview.heading("nuevo_numero/m", text="Número Nuevo / m")
treeview.pack(expand=True, fill="both", padx=20, pady=20)

# Configurar el grid dentro de frame3
frame3.grid_rowconfigure(0, weight=1)
frame3.grid_columnconfigure(0, weight=1)

# Crear y ubicar la etiqueta para mostrar el resultado en frame3
label_resultado = tk.Label(frame3, text="El periodo de vida es: ", fg="darkgreen", bg="black")
label_resultado.pack(padx=20, pady=20)

# Iniciar el bucle principal
root.mainloop()
