class Doctor():
    def __init__(self,Doctor_id,Doctor_nombre,especialidad,agenda):
        self.Doctor_id=Doctor_id
        self.Doctor_nombre=Doctor_nombre
        self.especialidad=especialidad
        self.agenda=agenda

    def mostrarDoctor(self):
        return  "\n================================"+\
                "\n ----- DATOS DEL DOCTOR -----"+"\n"+\
                "ID del doctor    : "+str(self.Doctor_id)+"\n"+\
                "Nombre del doctor: "+self.Doctor_nombre+"\n"+\
                "Especialidad     : "+self.especialidad+"\n"+\
                self.agenda.mostrarAgenda() 
                







