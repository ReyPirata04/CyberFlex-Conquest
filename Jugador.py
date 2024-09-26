class Jugador:
    # Constructor de la clase
    def __init__(self, nombre, robot, puntos):
        self.nombre = nombre
        self.robot = robot
        self.puntos = puntos

    # Constructor de la clase
    def __init__(self, nombre, robot):
        self.nombre = nombre
        self.robot = robot 
    
    # Medoto de instancia
    def elegir(self):
        print(f"Los robots elegidos son: \n {self.robot}")


# Crear una instancia de la clase Jugador
Jugador1 = Jugador("Lucas","Chappie")

# Acceder a los atributos de la instancia
print(f"Nombre del jugador 1: {Jugador1.nombre}")
print(f"Robot elegido: {Jugador1.robot}")

# Llamar a un método de instancia
Jugador1.elegir()