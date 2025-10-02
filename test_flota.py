import pytest
from flota import Flota, Vehiculo, Camion, Furgoneta, CamionetaLiviana


def test_constructor_flota():
    flota = Flota("flota.csv")
    assert flota is not None
    assert flota.cantidad_vehiculos() == 6


def test_archivo_inexistente():
    with pytest.raises(FileNotFoundError):
        Flota("no_existe.csv")


def test_cantidad_por_tipo():
    flota = Flota("flota.csv")
    cantidades = flota.cantidad_por_tipo()
    assert cantidades == {"Camion": 2, "Furgoneta": 2, "CamionetaLiviana": 2}


def test_camion_sin_carga_pesada():
    camion = Camion("ABC123", "Miguel López", 50, 200, False)
    assert camion.calcular_costo() == 10000


def test_camion_con_carga_pesada():
    camion = Camion("XYZ789", "Laura Díaz", 60, 150, True)
    assert camion.calcular_costo() == 10350  # 60*150*1.15 = 10350


def test_furgoneta_con_refrigeracion():
    furgoneta = Furgoneta("DEF456", "Roberto Sánchez", 40, 300, True)
    assert furgoneta.calcular_costo() == 13200  # 40*300*1.10 = 13200


def test_furgoneta_sin_refrigeracion():
    furgoneta = Furgoneta("GHI789", "Sofía Morales", 35, 250, False)
    assert furgoneta.calcular_costo() == 8750


def test_camioneta_express():
    camioneta = CamionetaLiviana("JKL012", "Diego Ruiz", 30, 100, True)
    assert camioneta.calcular_costo() == 3600  # 30*100*1.20 = 3600


def test_camioneta_normal():
    camioneta = CamionetaLiviana("MNO345", "Valeria Castro", 25, 120, False)
    assert camioneta.calcular_costo() == 3000


def test_costo_total_flota():
    flota = Flota("flota.csv")
    total = flota.costo_total_flota()
    assert total == 48900


def test_viaje_mas_costoso():
    flota = Flota("flota.csv")
    viaje_caro = flota.viaje_mas_costoso()
    assert viaje_caro.patente == "DEF456"
    assert viaje_caro.conductor == "Roberto Sánchez"
    assert viaje_caro.calcular_costo() == 13200


def test_contar_camiones_carga_pesada():
    flota = Flota("flota.csv")
    assert flota.contar_camiones_carga_pesada() == 1


def test_contar_furgonetas_refrigeracion():
    flota = Flota("flota.csv")
    assert flota.contar_furgonetas_refrigeracion() == 1


def test_herencia_vehiculos():
    assert issubclass(Camion, Vehiculo)
    assert issubclass(Furgoneta, Vehiculo)
    assert issubclass(CamionetaLiviana, Vehiculo)


def test_composicion_flota_vehiculos():
    flota = Flota("flota.csv")
    assert hasattr(flota, "vehiculos")
    for v in flota.vehiculos:
        assert isinstance(v, Vehiculo)


def test_atributos_camion():
    camion = Camion("ABC123", "Miguel López", 50, 200, False)
    assert camion.tipo == 1
    assert camion.patente == "ABC123"
    assert camion.carga_pesada == False


def test_atributos_furgoneta():
    furgoneta = Furgoneta("DEF456", "Roberto Sánchez", 40, 300, True)
    assert furgoneta.tipo == 2
    assert furgoneta.refrigeracion == True


def test_atributos_camioneta():
    camioneta = CamionetaLiviana("JKL012", "Diego Ruiz", 30, 100, True)
    assert camioneta.tipo == 3
    assert camioneta.reparto_express == True
