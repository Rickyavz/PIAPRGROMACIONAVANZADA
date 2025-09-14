class Persona:
    def __init__(self):
        self.nombre=input("Ingrese el nombre del empleado ")
        self.sueldo=float(input("Ingrese el sueldo: "))
        self.horas=float(input("Ingrese las horas trabajadas "))
        self.fechadeingreso=input("Ingrese su fecha de Ingreso" )
        self.vacaciones=int(input("Ingrese sus semanas trabajadas "))
    def imprimir(self):
        print("Nombre", self.nombre)
        print("Sueldo", self.sueldo)
        print("Horas", self.horas)
        print("Fecha de ingreso", self.fechadeingreso)
        print("Semanas trabajadas", self.vacaciones)
    def paga_impuestos(self):
        if self.sueldo>3000:
            print("Debe pagar impuestos")
        else:
            print("No paga impuestos")
    def horas_trabajadas(self):
        if self.horas>8:
            print("Trabajo completo")
        else:
            print("Trabajo no completado.")   
    def vacacionespagadas(self):
        if self.vacaciones>300:
            print(" Tiene vacaciones pagadas.")
        else:
            print("No tiene acceso a vacaciones pagadas :(")
persona=Persona()
persona.imprimir()
persona.paga_impuestos()
persona.horas_trabajadas()
persona.vacacionespagadas()
