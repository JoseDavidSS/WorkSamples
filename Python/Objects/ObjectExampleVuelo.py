class Vuelo:
    def __init__ (self, aerolinea, vuelo, fecha , hora, capacidad, cantidad, estado):
        self.aerolinea = aerolinea
        self.vuelo = vuelo
        self.fecha = fecha
        self.hora = hora
        self.capacidad = capacidad
        self.cantidad = cantidad
        self.estado = "O"

    #Métodos get de la clase

    def get_aerolinea (self):
        return str(self.aerolinea)

    def get_vuelo (self):
        return str(self.vuelo)

    def get_fecha (self):
        return str(self.fecha)

    def get_hora (self):
        return str(self.hora)
    
    def get_capacidad (self):
        return self.capacidad

    def get_cantidad (self):
        return self.cantidad

    def get_estado (self):
        return self.estado

    #Métodos set de la clase

    def set_hora (self, hora):
        self.hora = str(hora)

    def set_fecha (self, fecha):
        self.fecha = str(fecha)

    def set_cantidad (self, cantidad):
        self.cantidad += int(cantidad)

    #Método que imprime los valores del objeto

    def mostrar (self):
        print ("aerolínea:", self.get_aerolinea()) #Se agrega los self antes de llamar a los métodos
        print ("número de vuelo:", self.get_vuelo())
        print ("fecha:", self.get_fecha())
        print ("hora:", self.get_hora())
        print ("capacidad:", self.get_capacidad())
        print ("cantidad:", self.get_cantidad())
        print ("estado:", self.get_estado())
        print ("\n")

    #Método que actualiza la hora
        
    def actualiza_hora (self, hora):
        self.set_hora(hora)

    #Método que actualiza la fecha
        
    def actualizar_fecha (self, fecha):
        self.set_fecha (str(fecha))

    #Método que agrega campos
    def reserva (self, cantidad):
        if isinstance (cantidad, int):
            total = cantidad + int(self.get_cantidad())
            if (total >= self.get_capacidad()):
                print ("No hay espacio disponible")
            else:
                self.set_cantidad(cantidad)
        else:
            print ("cantidad debe ser un número entero")

#Definición de instancias

Instancia1 = Vuelo ("Tracopa", 701, "1/1/2018", "14:00", 100, 57, "O")
Instancia2 = Vuelo ("Airlines", 87, "3/5/2018", "20:00", 50, 22, "O")
Instancia3 = Vuelo ("Volar", 9, "5/5/2018", "6:00", 220, 110, "O")
Instancia4 = Vuelo ("Seguritas", 672, "18/7/2018", "8:00", 30, 15, "O")
Instancia5 = Vuelo ("General", 24, "24/12/2018", "15:00", 150, 37, "O")

#Lista de instancias

vuelos = [Instancia1, Instancia2, Instancia3, Instancia4, Instancia5]

#E:lista vuelos (lista de instancias), fecha
#S:aerolinea, número de vuelo y hora
#R:vuelos es lista y fecha es string

def busque (vuelos, fecha):
    if isinstance (vuelos, list) and isinstance (fecha, str):
        largo = len(vuelos)
        for n in range (0, largo):
            if vuelos[n].get_cantidad() < vuelos[n].get_capacidad() and vuelos[n].get_fecha() == fecha:
                print (vuelos[n].get_aerolinea(), vuelos[n].get_vuelo(), vuelos[n].get_hora())
            else:
                return "no hay vuelos disponibles"
    else:
        return "error"
    
#Instancia1 antes de los cambios 
Instancia1.mostrar()

Instancia1.actualiza_hora("4:00")
Instancia1.actualizar_fecha("2/10/2019")
Instancia1.reserva(40)

#Instancia1 después de los cambios
Instancia1.mostrar()

