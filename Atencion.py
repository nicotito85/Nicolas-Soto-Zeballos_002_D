class Atencion:
    CodigoAtencion = ''
    NombreCliente = ''
    DescripcionAtencion = ''
    PrecioAtencion = 0

    def __init__(self):
        self.CodigoAtencion = 'A-001'
        self.NombreCliente = 'juanin juan jarry'
        self.FechaAtencion = '30-2-2023'
        self.HoraAtencion = '10:00'
        self.DescripcionAtencion = 'toma una cita en la hora'
        self.PrecioAtencion = 20000

    def setCodigoAtencion(self, CodigoAtencion):
        if CodigoAtencion[0:1].isalpha() and CodigoAtencion[2:5].isdigit():
            self.CodigoAtencion = CodigoAtencion
            return True
        else:
            print("formato Codigo incorrecto")
            return False

    def setPrecioAtencion(self, PrecioAtencion):
        if PrecioAtencion() > 20000:
            self.PrecioAtencion = PrecioAtencion
            return True
        else:
            print("precio bajo los 20000")
            return False

    def setNombreCliente(self,NombreCliente):
        if len(NombreCliente)>5 and len(NombreCliente)<46:
            self.NombreCliente = NombreCliente
            return True
        else:
            print("caracteres exceden limite permitido")
            return False
