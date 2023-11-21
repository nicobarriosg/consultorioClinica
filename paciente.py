from doctor import Doctor
from agenda import Agenda

class Paciente(Doctor):
    def __init__(self, Doctor_id, Doctor_nombre, especialidad, agenda, id_Paciente, nombre_Paciente, diagnostico,tratamiento,comunaResi):
        super().__init__(Doctor_id, Doctor_nombre, especialidad, agenda)
        self.id_Paciente    =id_Paciente
        self.nombre_Paciente=nombre_Paciente
        self.diagnostico    = diagnostico
        self.tratamiento    = tratamiento
        self.comunaResi     = comunaResi

    def mostrarPaciente(self):
        return  super().mostrarDoctor()+"\n"+\
                " ----- DATOS DEL PACIENTE ----- "+"\n"+\
                "ID del paciente     : "+str(self.id_Paciente)+"\n"+\
                "Nombre paciente     : "+self.nombre_Paciente+"\n"+\
                "Diagnostico         : "+self.diagnostico+"\n"+\
                "Tratamiento         : "+self.tratamiento+"\n"+\
                "Comuna de residencia: "+self.comunaResi+"\n"+\
                "================================"

    def menu(self):
        print("\n ----- PYTHON CENTER ----- \n")
        print(" ----- Menú de opciones ----- \n")
        print("1. Agregar un nuevo paciente")     
        print("2. Eliminar un paciente existente")   
        print("3. Actualizar datos agenda")   
        print("4. Actualizar datos paciente") 
        print("5. Mostrar datos / por doctor / por fecha")   
        print("6. Mostrar todos los datos disponibles")
        print("7. Finalizar")
        
    def leerOpcion(self):
        while True:
            try:
                opcion=int(input("\nIngresa opción (1 a 7): "))
                if opcion>=1 and opcion<=7:
                    return opcion
                else:
                    print("Opción inválida")
            except:
                print("Debes ingresar sólo números")

    def leerDatos(self,lista):  
        print("--DATOS ALMACENADOS--")
        for q in lista:
            print(q.mostrarPaciente())     

    def buscarId(self, id, lista):
        for item in lista:
            if id == item.id_Paciente:  
                return item
        return None

    def leerId(self):
        while True:
            try:
                id = int(input("\nIngresa ID (Unicamente numeros): "))
                if id > 0:
                    return id
                else:
                    print("El id debe ser mayor 0")
            except:
                print("Debes ingresar sólo números") 
    
    def buscarDoctorId(self, id, lista):
        for item in lista:
            if id == item.Doctor_id:  
                return item
        return None

    def leerDoctorId(self):
        while True:
            try:
                print("\n1.- Juan (Medico General)")
                print("2.- Lucas (Cirujano)")
                print("3.- Yasmin (Cirujano Cardiovascular)")
                print("4.- Raul (Anestesiologo)")
                print("5.- Martina (Alergologo)\n")
                id = int(input("Ingresa ID del doctor (1-5): "))
                if 1 <= id <= 5:
                    return id
                else:
                    print("\nLa opción debe estar entre 1 y 5.")
            except ValueError:
                print("Debes ingresar solo números")


    def buscarfecha(self):
        while True:
            try:
                fecha=int(input("Ingresa Id: "))
                if fecha<=0:
                    return fecha
                else:
                    print("El id debe ser >0")
            except:
                print("Debes ingresar sólo números") 
    
    def buscarfecha(self,id_fecha,lista):
        for f in lista:
            if id_fecha==f.fecha: 
                return f
        return None

    def agregarPaciente(self, lista):
        id = self.leerId()
        q = self.buscarId(id, lista)
        if q is None:
            nombre_paciente = str(input("Ingrese el nombre del paciente: ")).title()
            diagnostico = str(input("Ingrese el diagnóstico del paciente: ")).capitalize()
            tratamiento = str(input("Ingrese el tratamiento del paciente: ")).capitalize()
            comuna_Resi = str(input("Ingrese la comuna de residencia del paciente: ")).title()
            id_doctor = self.leerDoctorId()
            doctor_info = self.docs(id_doctor)
            nombre_doctor, especialidad = doctor_info


            nueva_fecha = input("Ingrese la fecha (Dia/Mes/Año): ")
            nueva_hora = input("Ingrese la hora (Hr:Min): ")
            agenda = Agenda(fecha=nueva_fecha, hora=nueva_hora)
                
            lista.append(Paciente(id_doctor, nombre_doctor, especialidad, agenda, id, nombre_paciente, diagnostico, tratamiento, comuna_Resi))
            print("\nPaciente agregado correctamente.")

        else:
            print("\nID Ya existe, Pertenece a", q.nombre_Paciente)

    def docs(self, id):
        if id == 1:
            return "Juan", "Medico General"
        elif id == 2:
            return "Lucas", "Cirujano"
        elif id == 3:
            return "Yasmin", "Cirujano Cardio"
        elif id == 4:
            return "Raul", "Anestesiologo"
        elif id == 5:
            return "Martina", "Alergologo"
        else:
            return None, None

    def eliminarPaciente(self, lista):
        eliminar_id = int(input("\nIngrese Id del Paciente a Eliminar: "))
        eliminar_paciente = None
        for q in lista:
            if q.id_Paciente == eliminar_id:
                eliminar_paciente = q
                lista.remove(eliminar_paciente)
                print("\nPaciente Eliminado con éxito")
                break

    def actualizarAgenda(self, lista):
        id_paciente = self.leerId()
        paciente = self.buscarId(id_paciente, lista)

        if paciente is None:
            print("No se ha encontrado al paciente con ese ID:", id_paciente)
        else:
            try:
                nueva_fecha = input("\nIngrese la nueva fecha para el paciente en la agenda (Dia/Mes/Año): ")
                nueva_hora = input("Ingrese la nueva hora para el paciente en la agenda: (Hr:Min)")
                paciente.agenda.fecha = nueva_fecha
                paciente.agenda.hora = nueva_hora
                print("\nAgenda actualizada correctamente")
            except Exception as e:
                print("\nError al actualizar la agenda:", str(e))

    def actualizarPaciente(self, lista):
        id_paciente = self.leerId()
        paciente = self.buscarId(id_paciente, lista)
        if paciente is not None:
            print("¿Qué dato desea actualizar?")
            print("1. ID")
            print("2. Nombre")
            print("3. Tratamiento")
            print("4. Diagnóstico")
            print("5. Comuna de residencia")
            opcion = input("Ingrese la opción (1-5): ")
            if opcion == "1":
                nuevo_id = input("Ingrese la nueva ID: ")
                paciente.id_Paciente = nuevo_id
            elif opcion == "2":
                nuevo_nombre = input("Ingrese el nuevo nombre: ").title()
                paciente.nombre_Paciente = nuevo_nombre
            elif opcion == "3":
                nuevo_tratamiento = input("Ingrese el nuevo tratamiento: ").title()
                paciente.tratamiento = nuevo_tratamiento
            elif opcion == "4":
                nuevo_diagnostico = input("Ingrese el nuevo diagnóstico: ").title()
                paciente.diagnostico = nuevo_diagnostico
            elif opcion == "5":
                nueva_comuna = input("Ingrese la nueva comuna de residencia: ").title()
                paciente.comunaResi = nueva_comuna
            print("\nPaciente actualizado correctamente.")
        else:
            print("\nNo se ha encontrado el paciente.")
     
    def buscarDoctor(self,lista):
        id_doctor=self.leerDoctorId()
        doctor=self.buscarDoctorId(id_doctor,lista)
        if doctor:
            print("PACIENTES DEL DOCTOR :",doctor)
            print(doctor.mostrarPaciente())
        else:
            print("----ID DEL DOCTOR NO EXISTE----")

    def buscarAgenda(self,lista,fecha):
        fecha=input("Ingrese la fecha determinada(Dia/Mes/Año): ")
        for f in lista:
            if fecha==f.agenda.fecha:
                print("Pacientes Archivados a  la fecha :  ",fecha)
                print(f.mostrarPaciente())
        else:
            print("No se a encontrado")         

    def menuMostrarDatos(self,lista):
        while True:
            try:
                print("\n========================================")
                opcion = int(input("\nDesea buscar por: \n\n1.Buscar por doctor \n2.Buscar por fecha \n3.Volver al menu \n\nIngrese la opcion (1 a 3): "))
                if opcion >= 1 and opcion <= 3:
                            if opcion == 1:
                                Paciente.buscarDoctor(self,lista)
                            elif opcion == 2:
                                Paciente.buscarAgenda(self,lista,fecha=None)
                            else:
                                print("\n========================================")
                                break
                else:
                    print("\nOpcion fuera de rango. Intente nuevamente")
                    print("\n========================================")
            except:
                print("\nIngrese solo opciones validas")
                print("\n========================================")

