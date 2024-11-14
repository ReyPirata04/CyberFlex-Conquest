import tkinter as tk
from Clases.Jugador import Jugador
from Clases.Robot import Robot

def ingresar_nombres(root, volver_funcion):


    def mostrar():
        j1 = entrada_nombre1.get()
        j2 = entrada_nombre2.get()
        mostrar_jugadores.config(text=f"Jugador 1: {j1}\nJugador 2: {j2}")
        mostrar_jugadores.pack()

    lbl_nombre_jugador1 = tk.Label(root, text="Jugador N1 ingrese su nombre")
    lbl_nombre_jugador1.config(font=("Arial", 14))
    entrada_nombre1 = tk.Entry(root)

    lbl_nombre_jugador2 = tk.Label(root, text="Jugador N2 ingrese su nombre")
    lbl_nombre_jugador2.config(font=("Arial", 14))
    entrada_nombre2 = tk.Entry(root)

    btn_Jugar = tk.Button(root,text="Jugar", command=mostrar)

    mostrar_jugadores = tk.Label(root, text="")


    lbl_nombre_jugador1.pack()
    entrada_nombre1.pack()
    lbl_nombre_jugador2.pack()
    entrada_nombre2.pack()

    btn_Jugar.pack()

    btn_volver = tk.Button(root, text="Volver al Menú", command=lambda: volver_funcion(lbl_nombre_jugador1, entrada_nombre1, lbl_nombre_jugador2, entrada_nombre2, btn_volver))
    btn_volver.pack(pady=10)