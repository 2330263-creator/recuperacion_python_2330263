import pytest
from recuperacion_python_2330263.services import GimnasioService


@pytest.fixture
def servicio():
    s = GimnasioService()
    s.registrar_socio("S01", "Carlos Gómez", 25, "Básica", 500.0)
    s.registrar_socio("S02", "Ana Martínez", 30, "Premium", 800.0)
    return s


# --- 1, 2, 3: Funcionamiento Normal ---
def test_registrar_socio_exito(servicio):
    socio = servicio.registrar_socio("S03", "Luis Reyes", 22, "VIP", 1200.0)
    assert socio.id_socio == "S03"
    assert len(servicio.obtener_todos()) == 3


def test_calcular_ingreso_mensual_esperado(servicio):
    total = servicio.calcular_ingreso_mensual_esperado()
    assert total == 1300.0


def test_filtrar_por_membresia_existente(servicio):
    premium = servicio.filtrar_por_membresia("Premium")
    assert len(premium) == 1
    assert premium[0].nombre == "Ana Martínez"


# --- 4, 5: Casos Límite ---
def test_calcular_edad_promedio_sin_socios():
    servicio_vacio = GimnasioService()
    assert servicio_vacio.calcular_edad_promedio() == 0.0


def test_actualizar_socio_valores_limite(servicio):
    resultado = servicio.actualizar_socio("S01", edad=1)
    assert resultado is True
    assert servicio.buscar_por_id("S01").edad == 1


# --- 6, 7: Datos Incorrectos o Inválidos ---
def test_registrar_socio_id_duplicado(servicio):
    with pytest.raises(
        ValueError, match="Ya existe un socio registrado con el ID 'S01'."
    ):
        servicio.registrar_socio("S01", "Otro Nombre", 40, "Básica", 500.0)


def test_registrar_socio_edad_invalida(servicio):
    with pytest.raises(ValueError, match="La edad debe ser mayor a cero."):
        servicio.registrar_socio("S04", "Pedro", 0, "Básica", 500.0)


def test_registrar_socio_membresia_invalida(servicio):
    with pytest.raises(ValueError, match="Membresía inválida."):
        servicio.registrar_socio("S05", "Maria", 25, "UltraVIP", 500.0)


# --- 8: Búsqueda sin Resultados ---
def test_buscar_socio_inexistente(servicio):
    resultado = servicio.buscar_por_id("S999")
    assert resultado is None