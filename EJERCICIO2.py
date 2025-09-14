class calificaciones():
    def __init__(self,calif1,calif2,calif3):
        self.calif1=calif1
        self.calif2=calif2
        self.calif3=calif3
        self.promedio=0
    def calcular_promedio(self):
        self.promedio=float(self.calif1+self.calif2+self.calif3)/3
    def imprimir_promedio(self):
        print("El promedio es: ",self.promedio)
    def agregar_califiaciones(self):
        self.datos.append(self)

datos=[]
while True:
        print("Eliga una opcion")
        print("1.Agregar calificaciones.")
        print("2.Sacar promedio")
        opcion=input("Seleccione el numero de la opcion: ")
        if opcion=="1":
            calif1 = float(input("Ingrese calificación 1: "))
            calif2 = float(input("Ingrese calificación 2: "))
            calif3 = float(input("Ingrese calificación 3: "))
            nuevas_calificaciones=calificaciones(calif1,calif2,calif3)
            datos.append(nuevas_calificaciones)
        else:
            print("Eliga otra opcion")
        if opcion=="2":
            nuevas_calificaciones.calcular_promedio()
            nuevas_calificaciones.imprimir_promedio()
        else:
            print("Eliga otra opcion")