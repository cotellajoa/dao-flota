from abc import ABC, abstractmethod


class Flota:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo
        self.vehiculos = []
        if not nombre_archivo.endswith(".csv"):
            raise ValueError("El archivo debe tener la extension .csv")
        if len(nombre_archivo) == 0:
            raise ValueError("El nombre del archivo no puede estar vacio")
        try:
            with open(nombre_archivo, "r") as archivo:
                for linea in archivo:
                    datos = linea.split(",")
                    tipo = int(datos[0])
                    patente = datos[1]
                    nombre = datos[2]
                    costo_base = int(datos[3])
                    km_recorridos = int(datos[4])
                    extra = datos[5].strip() == "True"
                    if tipo == 1:
                        camion = Camion(
                            patente, nombre, costo_base, km_recorridos, extra
                        )
                        self.vehiculos.append(camion)
                    elif tipo == 2:
                        furgoneta = Furgoneta(
                            patente, nombre, costo_base, km_recorridos, extra
                        )
                        self.vehiculos.append(furgoneta)
                    elif tipo == 3:
                        camioneta = CamionetaLiviana(
                            patente, nombre, costo_base, km_recorridos, extra
                        )
                        self.vehiculos.append(camioneta)
                    else:
                        raise ValueError("Tipo de vehiculo no valido")
        except FileNotFoundError:
            raise FileNotFoundError("El archivo no existe")

    def cantidad_vehiculos(self):
        return len(self.vehiculos)

    def cantidad_por_tipo(self):
        cantidades = {"Camion": 0, "Furgoneta": 0, "CamionetaLiviana": 0}
        for vehiculo in self.vehiculos:
            if isinstance(vehiculo, Camion):
                cantidades["Camion"] += 1
            if isinstance(vehiculo, Furgoneta):
                cantidades["Furgoneta"] += 1
            if isinstance(vehiculo, CamionetaLiviana):
                cantidades["CamionetaLiviana"] += 1
        return cantidades

    def costo_total_flota(self) -> int:
        total = 0
        for vehiculo in self.vehiculos:
            total += vehiculo.calcular_costo()
        return total

    def viaje_mas_costoso(self):
        mas_costoso = None
        for vehiculo in self.vehiculos:
            if (
                mas_costoso is None
                or vehiculo.calcular_costo() > mas_costoso.calcular_costo()
            ):
                mas_costoso = vehiculo
        return mas_costoso

    def contar_camiones_carga_pesada(self) -> int:
        count = 0
        for vehiculo in self.vehiculos:
            if isinstance(vehiculo, Camion) and vehiculo.carga_pesada:
                count += 1
        return count

    def contar_furgonetas_refrigeracion(self) -> int:
        count = 0
        for vehiculo in self.vehiculos:
            if isinstance(vehiculo, Furgoneta) and vehiculo.refrigeracion:
                count += 1
        return count


class Vehiculo(ABC):
    def __init__(
        self, patente: str, conductor: str, costo_base: int, km_recorridos: int
    ):
        self.patente = patente
        self.conductor = conductor
        self.costo_base = costo_base
        self.km_recorridos = km_recorridos

    @abstractmethod
    def calcular_costo(self) -> int:
        pass


class Camion(Vehiculo):
    def __init__(
        self,
        patente: str,
        conductor: str,
        costo_base: int,
        km_recorridos: int,
        carga_pesada: bool,
    ):
        super().__init__(patente, conductor, costo_base, km_recorridos)
        self.carga_pesada = carga_pesada
        self.tipo = 1

    def calcular_costo(self) -> int:
        if self.carga_pesada:
            return int(self.costo_base * self.km_recorridos * 1.15)
        return self.costo_base * self.km_recorridos


class Furgoneta(Vehiculo):
    def __init__(
        self,
        patente: str,
        conductor: str,
        costo_base: int,
        km_recorridos: int,
        refrigeracion: bool,
    ):
        super().__init__(patente, conductor, costo_base, km_recorridos)
        self.refrigeracion = refrigeracion
        self.tipo = 2

    def calcular_costo(self) -> int:
        if self.refrigeracion:
            return int(self.costo_base * self.km_recorridos * 1.10)
        return self.costo_base * self.km_recorridos


class CamionetaLiviana(Vehiculo):
    def __init__(
        self,
        patente: str,
        conductor: str,
        costo_base: int,
        km_recorridos: int,
        reparto_express: bool,
    ):
        super().__init__(patente, conductor, costo_base, km_recorridos)
        self.reparto_express = reparto_express
        self.tipo = 3

    def calcular_costo(self) -> int:
        if self.reparto_express:
            return int(self.costo_base * self.km_recorridos * 1.20)
        return self.costo_base * self.km_recorridos
