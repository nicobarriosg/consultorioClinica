from paciente import Paciente
from agenda import Agenda
from doctor import Doctor

lista = []
p = Paciente(1,"Juan","Medico General", Agenda("13/10/2023","15:30"),1,"Pedro Martinez","Dolor de cabeza","Paracetamol","Maipu")
lista.append(p)

p = Paciente(2,"Lucas","Cirujano",Agenda("17/02/2023","15:00"),2,"Gabriela Campos","Fiebre","Ibuprofeno","Puente Alto")
lista.append(p)

p = Paciente(3,"Yasmin","Cirujano Cardiovascular",Agenda("10/03/2023","17:00"),3,"Nicolar Barrios","Dolor de garganta","antiinflamatorio","Santiago Centro")
lista.append(p)

p = Paciente(4,"Raul","Anestesiologo",Agenda("31/01/2023","18:00"),2,"Juan Cortes","Alergias","Descongestionantes","Las Rejas")
lista.append(p)

p = Paciente(5,"Martina","Alergologo",Agenda("18/05/2023","11:00"),2,"Liam Rodriguez","Gripe","Antivirales","Ñuñoa")
lista.append(p)

while True:
    p.menu()
    opcion = p.leerOpcion()
    if opcion == 1:
        p.agregarPaciente(lista)
    elif opcion == 2:
        p.eliminarPaciente(lista)
    elif opcion == 3:
        p.actualizarAgenda(lista)
    elif opcion == 4:
        p.actualizarPaciente(lista)
    elif opcion == 5:
        p.menuMostrarDatos(lista)
    elif opcion == 6:
        p.leerDatos(lista)
    else:
        print("\nNos vemos la proxima!")
        break

# Nicolás Barrios
# Lucas Gonzalez