import tkinter as tk
from descripcion import mostrar_contenido  # Importa la función de la ventana de descripción
from nombres import ingresar_nombres

def mostrar_descripcion():
    # Ocultar los elementos de la pantalla principal
    btn_jugar.pack_forget()
    btn_descripcion.pack_forget()
    
    # Llama a la función que muestra el contenido de la descripción
    mostrar_contenido(root,titulo, btn_jugar, btn_descripcion, volver_al_menu)

def volver_al_menu(label_descripcion, btn_volver, titulo, btn_jugar, btn_descripcion):
    # Ocultar la descripción y el botón de volver
    label_descripcion.pack_forget()
    btn_volver.pack_forget()

    root.title("Batallas Cibernéticas")
    
    # Muestra los elementos del menú principal
    titulo.pack()
    btn_jugar.pack(ipadx=60, pady=20, side="top")
    btn_descripcion.pack(ipadx=43)

def ingresar_nombres():
    titulo.pack_forget()
    btn_jugar.pack_forget()
    btn_descripcion.pack_forget()

    ingresar_nombres(root,  volver_al_menu)

    pass

def volver_al_menu_nombres(lbl_nombre_jugador1, entrada_nombre1, lbl_nombre_jugador2, entrada_nombre2, btn_volver):
    # Ocultar la descripción y el botón de volver
    btn_volver.pack_forget()
    lbl_nombre_jugador1.pack_forget()
    entrada_nombre1.pack_forget()
    lbl_nombre_jugador2.pack_forget()
    entrada_nombre2.pack_forget()

    root.title("Batallas Cibernéticas")
    
    # Muestra los elementos del menú principal
    titulo.pack()
    btn_jugar.pack(ipadx=60, pady=20, side="top")
    btn_descripcion.pack(ipadx=43)


root = tk.Tk()
root.title("Batallas Cibérneticas")
root.geometry("700x400")
root.config(bg="#000033")

titulo = tk.Label(root, text="CyberFlex-Conquest", bg="#000033", fg="#00FF00" , font=("Orbitron", 32))
titulo.pack(pady=50)

btn_jugar = tk.Button(root, text="Jugar", relief="raised", command=ingresar_nombres)
btn_jugar.pack(ipadx=60, pady=20, side="top" )

btn_descripcion = tk.Button(root, text="Descripcion", relief="raised", command=mostrar_descripcion)
btn_descripcion.pack(ipadx=43)


root.mainloop()

