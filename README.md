# 🚚 Sistema de Gestión de Flota de Vehículos

Una empresa de logística necesita un sistema para gestionar su flota de vehículos. Existen tres tipos de vehículos:

- **Camión**: tiene un costo base por kilómetro. Si transporta **carga pesada** (más de 10 toneladas), se aplica un recargo del **15%**.
- **Furgoneta**: tiene un costo base por kilómetro. Si incluye **refrigeración**, se aplica un recargo del **10%**.
- **Camioneta liviana**: tiene un costo base por kilómetro. Si se usa para **reparto express** (entrega en menos de 24 horas), se aplica un recargo del **20%**.

---

## 📄 Archivo `flota.csv`

Cada línea del archivo contiene los siguientes campos separados por comas:

1. **Tipo de vehículo**
   - `1` = Camión
   - `2` = Furgoneta
   - `3` = Camioneta liviana
2. **Patente del vehículo** (cadena)
3. **Nombre del conductor** (cadena)
4. **Costo base por kilómetro** (número entero)
5. **Kilómetros recorridos** (número entero)
6. **Columna extra** (`True` o `False`, según el tipo):
   - Para **camión**: `True` si transporta carga pesada, `False` en caso contrario.
   - Para **furgoneta**: `True` si tiene refrigeración, `False` en caso contrario.
   - Para **camioneta liviana**: `True` si es reparto express, `False` en caso contrario.

---

## 🛠️ Funcionalidades requeridas

1. **Cargar vehículos** desde el archivo `flota.csv`.
2. **Calcular el costo total** de todos los viajes realizados.
3. **Obtener el vehículo** con el viaje más costoso.
4. **Calcular el ingreso total** de la flota (equivalente al costo total).
5. **Contar cuántos camiones** transportan carga pesada.
6. **Contar cuántas furgonetas** tienen refrigeración.
7. **Devolver un diccionario** con la cantidad de vehículos de cada tipo.
