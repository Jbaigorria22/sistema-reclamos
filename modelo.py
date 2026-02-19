class Reclamo:

    def __init__(self, numero_servicio, nombre, barrio, descripcion, fecha, estado="Pendiente"):
        self.numero_servicio = numero_servicio
        self.nombre = nombre
        self.barrio = barrio
        self.descripcion = descripcion
        self.fecha = fecha
        self.estado = estado

    def marcar_como_resuelto(self):
        if self.estado == "Resuelto":
            return False
        self.estado = "Resuelto"
        return True

    def to_dict(self):
        return {
            "numero_servicio": self.numero_servicio,
            "nombre": self.nombre,
            "barrio": self.barrio,
            "descripcion": self.descripcion,
            "fecha": self.fecha,
            "estado": self.estado
        }

    @staticmethod
    def from_dict(data):
        return Reclamo(
            data["numero_servicio"],
            data["nombre"],
            data["barrio"],
            data["descripcion"],
            data["fecha"],
            data["estado"]
        )
