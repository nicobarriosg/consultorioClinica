class Agenda():
    def __init__(self, fecha, hora):
        self.fecha=fecha
        self.hora=hora

    def mostrarAgenda(self):
        return  "\n ----- DATOS DE LA AGENDA ----- "+"\n"+\
                "Fecha  : "+str(self.fecha)+"\n"+\
                "Hora   : "+str(self.hora)+"\n"
    
   
    