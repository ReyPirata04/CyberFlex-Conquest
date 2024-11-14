import tkinter as tk

def mostrar_contenido(root, titulo, btn_jugar, btn_descripcion, volver_func):

    root.title("Descripción")
    
    # Crear el contenido de la descripción con saltos de línea
    contenido = """CyberFlex-Conquest es un juego de estrategia 
                donde los jugadores luchan por conquistar 
                territorios cibernéticos."""
    
    # Crear y mostrar el Label con la descripción
    label_descripcion = tk.Label(root, text=contenido, bg="#000033", fg="cyan", wraplength=550, justify="center", font=("Orbitron", 12))
    label_descripcion.pack(pady=20, padx=20)
    
    # Botón para volver al menú principal
    btn_volver = tk.Button(root, text="Volver al Menú", command=lambda: volver_func(label_descripcion, btn_volver, titulo, btn_jugar, btn_descripcion))
    btn_volver.pack(pady=10)

