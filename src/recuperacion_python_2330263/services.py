from recuperacion_python_2330263.models import Socio


class GimnasioService:
    """Servicio que administra el registro y operaciones de los socios."""

    def __init__(self):
        self.socios: list[Socio] = []

    def _normalizar_membresia(self, membresia: str) -> str:
        membresias_map = {
            "básica": "Básica",
            "basica": "Básica",
            "premium": "Premium",
            "vip": "VIP",
        }
        key = membresia.strip().lower()
        if key not in membresias_map:
            raise ValueError("Membresía inválida. Debe ser una de: Básica, Premium, VIP")
        return membresias_map[key]

    def registrar_socio(
        self,
        id_socio: str,
        nombre: str,
        edad: int,
        membresia: str,
        mensualidad: float,
    ) -> Socio:
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

        membresia_normalizada = self._normalizar_membresia(membresia)

        if mensualidad < 0:
            raise ValueError("La mensualidad no puede ser negativa.")

        socio = Socio(id_limpio, nombre_limpio, edad, membresia_normalizada, mensualidad)
        self.socios.append(socio)
        return socio

    def obtener_todos(self) -> list[Socio]:
        return self.socios

    def buscar_por_id(self, id_socio: str) -> Socio | None:
        id_limpio = id_socio.strip()
        for socio in self.socios:
            if socio.id_socio == id_limpio:
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
            socio.membresia = self._normalizar_membresia(membresia)

        if mensualidad is not None:
            if mensualidad < 0:
                raise ValueError("La mensualidad no puede ser negativa.")
            socio.mensualidad = mensualidad

        return True

    def eliminar_socio(self, id_socio: str) -> bool:
        socio = self.buscar_por_id(id_socio)
        if socio:
            self.socios.remove(socio)
            return True
        return False

    def calcular_ingreso_mensual_esperado(self) -> float:
        return sum(socio.mensualidad for socio in self.socios)

    def filtrar_por_membresia(self, tipo: str) -> list[Socio]:
        try:
            tipo_normalizado = self._normalizar_membresia(tipo)
        except ValueError:
            return []
        return [s for s in self.socios if s.membresia == tipo_normalizado]

    def calcular_edad_promedio(self) -> float:
        if not self.socios:
            return 0.0
        return sum(socio.edad for socio in self.socios) / len(self.socios)

    def obtener_resumen_general(self) -> dict:
        return {
            "total_socios": len(self.socios),
            "ingreso_mensual_esperado": self.calcular_ingreso_mensual_esperado(),
            "edad_promedio": self.calcular_edad_promedio(),
        }