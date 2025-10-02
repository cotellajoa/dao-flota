from flota import Flota


def main():
    flota = Flota("flota.csv")
    print(f"La flota tiene {flota.cantidad_vehiculos()} vehiculos")
    for vehiculo in flota.vehiculos:
        print(f"Patente: {vehiculo.patente}, Costo: {vehiculo.calcular_costo()} ")


if __name__ == "__main__":
    main()
