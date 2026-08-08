from recuperacion_python_2330263.models import Socio


class GimnasioService:
    """Servicio que administra el registro y operaciones de los socios."""

    def __init__(self):
        self.socios: list[Socio] = []

    def registrar_socio(
        self,
        id_socio: str,
        nombre: str,
        edad: int,
        membresia: str,
        mensualidad: float,
    ) -> Socio:
        """Registra un nuevo socio asegurando ID único y datos válidos."""
        id_limpio = id_socio.strip()
        if not id_limpio:
            raise ValueError("El ID del socio no puede estar vacío.")

        if self.buscar_por_id(id_limpio) is not None:
            raise ValueError(f"Ya existe un socio registrado con el ID '{id_limpio}'.")

        nombre_limpio = nombre.strip()
        if not nombre_limpio:
            raise ValueError("El nombre no puede estar vacío.")

        if edad <= 0:
            raise ValueError("La edad debe ser mayor a cero.")

        membresias_validas = ["Básica", "Premium", "VIP"]
        membresia_cap = membresia.strip().capitalize()
        if membresia_cap not in membresias_validas:
            raise ValueError(
                f"Membresía inválida. Debe ser una de: {', '.join(membresias_validas)}"
            )

        if mensualidad < 0:
            raise ValueError("La mensualidad no puede ser negativa.")

        socio = Socio(
            id_limpio, nombre_limpio, edad, membresia_cap, float(mensualidad)
        )
        self.socios.append(socio)
        return socio

    def obtener_todos(self) -> list[Socio]:
        """Retorna la lista de todos los socios."""
        return self.socios

    def buscar_por_id(self, id_socio: str) -> Socio | None:
        """Busca un socio por su ID único."""
        for socio in self.socios:
            if socio.id_socio == id_socio.strip():
                return socio
        return None

    def actualizar_socio(
        self,
        id_socio: str,
        nombre: str | None = None,
        edad: int | None = None,
        membresia: str | None = None,
        mensualidad: float | None = None,
    ) -> bool:
        """Actualiza los datos de un socio existente."""
        socio = self.buscar_por_id(id_socio)
        if not socio:
            return False

        if nombre is not None:
            nombre_limpio = nombre.strip()
            if not nombre_limpio:
                raise ValueError("El nombre no puede estar vacío.")
            socio.nombre = nombre_limpio

        if edad is not None:
            if edad <= 0:
                raise ValueError("La edad debe ser mayor a cero.")
            socio.edad = edad

        if membresia is not None:
            membresia_cap = membresia.strip().capitalize()
            if membresia_cap not in ["Básica", "Premium", "VIP"]:
                raise ValueError("Membresía inválida.")
            socio.membresia = membresia_cap

        if mensualidad is not None:
            if mensualidad < 0:
                raise ValueError("La mensualidad no puede ser negativa.")
            socio.mensualidad = float(mensualidad)

        return True

    def eliminar_socio(self, id_socio: str) -> bool:
        """Elimina a un socio por su ID."""
        socio = self.buscar_por_id(id_socio)
        if socio:
            self.socios.remove(socio)
            return True
        return False

    # Funciones particulares de la Variante 12
    def calcular_ingreso_mensual_esperado(self) -> float:
        """Calcula la suma total de las mensualidades de todos los socios."""
        return sum(socio.mensualidad for socio in self.socios)

    def filtrar_por_membresia(self, tipo_membresia: str) -> list[Socio]:
        """Filtra y retorna los socios que corresponden a un tipo de membresía."""
        tipo_cap = tipo_membresia.strip().capitalize()
        return [s for s in self.socios if s.membresia == tipo_cap]

    def calcular_edad_promedio(self) -> float:
        """Calcula el promedio de edad de todos los socios registrados."""
        if not self.socios:
            return 0.0
        return sum(socio.edad for socio in self.socios) / len(self.socios)

    def obtener_resumen_general(self) -> dict:
        """Retorna un resumen estadístico del gimnasio."""
        return {
            "total_socios": len(self.socios),
            "ingreso_mensual_esperado": self.calcular_ingreso_mensual_esperado(),
            "edad_promedio": round(self.calcular_edad_promedio(), 2),
        }