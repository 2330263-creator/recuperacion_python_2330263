class Socio:
    """Representa a un socio del gimnasio."""

    def __init__(
        self,
        id_socio: str,
        nombre: str,
        edad: int,
        membresia: str,
        mensualidad: float,
    ):
        self.id_socio = id_socio
        self.nombre = nombre
        self.edad = edad
        self.membresia = membresia
        self.mensualidad = mensualidad

    def a_diccionario(self) -> dict:
        """Convierte los datos del socio a un diccionario."""
        return {
            "id_socio": self.id_socio,
            "nombre": self.nombre,
            "edad": self.edad,
            "membresia": self.membresia,
            "mensualidad": self.mensualidad,
        }