import tkinter as tk
from tkinter import ttk
import numpy as np
from scipy.stats import chisquare


value = [[0, 0, 0, 0]] 

def calcular_media(resultados, m):
    normalizados = np.array(resultados) / m
    return np.mean(normalizados)

def calcular_varianza(resultados, m):
    normalizados = np.array(resultados) / m
    return np.var(normalizados)

def prueba_uniformidad(resultados, m, num_intervalos=10):
    normalizados = np.array(resultados) / m
    frecuencias, _ = np.histogram(normalizados, bins=num_intervalos, range=(0, 1))
    esperado = len(resultados) / num_intervalos
    #aplica la prueba al cuadrado
    chi2, p_valor = chisquare(frecuencias, [esperado] * num_intervalos)
    return chi2, p_valor

def button_callback():
    global value
    value = []  
    
 
    a = int(entry1.get())
    c = int(entry2.get())
    m = int(entry3.get())
    semilla_inicial = int(entry4.get())

   
    semilla_actual = semilla_inicial
    resultados = []
    valores_vistos = set()  # Usamos un conjunto para almacenar los números generados
    iteracion = 0

    while True:
    
        nuevo_numero = (a * semilla_actual + c) % m
        
       
        if nuevo_numero in valores_vistos:
            break
        
        
        valores_vistos.add(nuevo_numero)
        
        # Añadimos los datos de la iteración a `value`
        value.append([iteracion, semilla_actual, nuevo_numero, nuevo_numero / m])
        
        # Agregamos el número a la lista de resultados
        resultados.append(nuevo_numero)
        
        
        semilla_actual = nuevo_numero
        iteracion += 1  



    # Actualizar la tabla con los nuevos datos
    update_treeview()

    # Calcular el periodo de vida
    periodo_vida = len(resultados)

    # Calcular media, varianza y uniformidad
    media = calcular_media(resultados, m)
    varianza = calcular_varianza(resultados, m)
    chi2, p_valor = prueba_uniformidad(resultados, m)

    # Mostrar resultados en el label
    resultados_texto = (
        f"El periodo de vida es: {periodo_vida}\n"
        f"Media: {media:.4f}\n"
        f"Varianza: {varianza:.4f}\n"
        f"Prueba de uniformidad (chi-cuadrado): {chi2:.4f}\n"
        f"p-valor de uniformidad: {p_valor:.4f}"
    )
    label_resultado.configure(text=resultados_texto, fg="darkgreen")
    
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



root = tk.Tk()
root.title("Generadores Congruenciales")
root.geometry("825x460")  
root.configure()

# Crear Frames como contenedores
frame1 = tk.Frame(root, bg="black")
frame2 = tk.Frame(root, bg="black")
frame3 = tk.Frame(root, bg="black")  


frame1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
frame2.grid(row=1, column=0, padx=10, pady=0, sticky="nsew")
frame3.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")  


frame1.grid_columnconfigure(0, weight=1)
frame1.grid_columnconfigure(1, weight=3)  
frame1.grid_columnconfigure(2, weight=1)
frame1.grid_columnconfigure(3, weight=3)  


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


button1 = tk.Button(frame1, text="Procesar", command=button_callback, bg="darkgreen", fg="white")
button1.grid(row=2, column=0, columnspan=4, pady=10, padx=10, sticky="nsew")


frame2.grid_rowconfigure(0, weight=1)
frame2.grid_columnconfigure(0, weight=1)


treeview = ttk.Treeview(frame2, columns=("iteracion", "semilla", "nuevo_numero", "nuevo_numero/m"), show='headings')
treeview.heading("iteracion", text="Iteración")
treeview.heading("semilla", text="Semilla")
treeview.heading("nuevo_numero", text="Número Nuevo")
treeview.heading("nuevo_numero/m", text="Número Nuevo / m")
treeview.pack(expand=True, fill="both", padx=0, pady=0)


frame3.grid_rowconfigure(0, weight=1)
frame3.grid_columnconfigure(0, weight=1)


label_resultado = tk.Label(frame3, text="El periodo de vida es: ", fg="lightgreen", bg="black")
label_resultado.pack(padx=20, pady=20)


root.mainloop()
