"""
Archivo principal del sistema RHEA.

Contiene las importaciones, la creación de objetos y las pruebas
de herencia, polimorfismo, encapsulamiento y composición.
"""

from modelos import (
    HORMONAS_RHEA,
    RegistroRHEA,
    SensorHormonalAvanzado,
    SistemaMonitoreoRHEA
)


if __name__ == "__main__":

    print("=" * 45)
    print(" SISTEMA DE MONITOREO HORMONAL RHEA")
    print("=" * 45)

    print("\nAnalitos contemplados en el proyecto:")
    for hormona in HORMONAS_RHEA:
        print(f"- {hormona}")

    print(
        "\nNota: los valores son simulados y no tienen uso clínico.\n"
    )

    # ------------------------------------------------------
    # 1. INSTANCIACIÓN DE OBJETOS
    # ------------------------------------------------------

    sensor_base = RegistroRHEA(
        "RHEA-BASE-001",
        "FSH",
        5.4,
        "Muestra hormonal",
        True
    )

    sensor1 = SensorHormonalAvanzado(
        "RHEA-001",
        "FSH",
        5.4,
        "Muestra hormonal",
        "Microfluídica y biosensor",
        "mUI/mL"
    )

    sensor2 = SensorHormonalAvanzado(
        "RHEA-002",
        "LH",
        7.2,
        "Muestra hormonal",
        "Microfluídica y biosensor",
        "mUI/mL"
    )

    sensor3 = SensorHormonalAvanzado(
        "RHEA-003",
        "Estradiol",
        82.6,
        "Muestra hormonal",
        "Biosensor electroquímico",
        "pg/mL"
    )

    sensor4 = SensorHormonalAvanzado(
        "RHEA-004",
        "Progesterona",
        1.8,
        "Muestra hormonal",
        "Biosensor electroquímico",
        "ng/mL"
    )

    sensor5 = SensorHormonalAvanzado(
        "RHEA-005",
        "Insulina",
        8.1,
        "Muestra hormonal",
        "Biosensor electroquímico",
        "uUI/mL"
    )

    sensor6 = SensorHormonalAvanzado(
        "RHEA-006",
        "Cortisol",
        12.3,
        "Muestra hormonal",
        "Biosensor electroquímico",
        "ug/dL"
    )

    # ------------------------------------------------------
    # 2. COMPOSICIÓN: CREACIÓN DEL SISTEMA CONTENEDOR
    # ------------------------------------------------------

    sistema = SistemaMonitoreoRHEA()

    print("REGISTRO DE SENSORES")
    print(sistema.agregar_sensor(sensor_base))

    for sensor in [
        sensor1,
        sensor2,
        sensor3,
        sensor4,
        sensor5,
        sensor6
    ]:
        print(sistema.agregar_sensor(sensor))

    print(
        f"\nCantidad total de sensores: "
        f"{sistema.cantidad_sensores()}"
    )

    # ------------------------------------------------------
    # 3. HERENCIA Y POLIMORFISMO
    # ------------------------------------------------------

    print("\n" + "=" * 45)
    print(" INFORMACIÓN DE LOS SENSORES")
    print("=" * 45)

    # El mismo método se ejecuta de manera diferente
    # según el tipo de objeto almacenado.
    print(sistema.mostrar_sensores())

    # ------------------------------------------------------
    # 4. MÉTODOS OPERATIVOS Y DELEGACIÓN
    # ------------------------------------------------------

    print("\n" + "=" * 45)
    print(" PRUEBAS DE FUNCIONAMIENTO")
    print("=" * 45)

    print(sistema.activar_sensor("RHEA-BASE-001"))
    print(sistema.buscar_sensor("RHEA-001").calibrar())
    print(sistema.desactivar_sensor("RHEA-002"))
    print(sistema.actualizar_sensor("RHEA-003", 84.0))

    # ------------------------------------------------------
    # 5. ENCAPSULAMIENTO Y VALIDACIÓN
    # ------------------------------------------------------

    print("\n" + "=" * 45)
    print(" PRUEBA DE ENCAPSULAMIENTO")
    print("=" * 45)

    try:
        sensor1.valor_detectado = -2
    except ValueError as error:
        print(f"Validación correcta: {error}")

    print(
        f"Valor consultado de {sensor1.codigo}: "
        f"{sensor1.valor_detectado:.2f} {sensor1.unidad}"
    )

    # ------------------------------------------------------
    # 6. INDEPENDENCIA ENTRE INSTANCIAS
    # ------------------------------------------------------

    print("\n" + "=" * 45)
    print(" INDEPENDENCIA ENTRE INSTANCIAS")
    print("=" * 45)

    sistema.actualizar_sensor("RHEA-001", 6.1)

    for codigo in ["RHEA-001", "RHEA-002", "RHEA-003"]:
        sensor = sistema.buscar_sensor(codigo)
        print(
            f"Valor de {codigo}: "
            f"{sensor.valor_detectado:.2f} {sensor.unidad}"
        )

    print("\n" + "=" * 45)
    print(" PRUEBA DE COMPOSICIÓN")
    print("=" * 45)

    print(
        "El sistema contiene objetos sensores y puede utilizar "
        "sus métodos mediante la clase contenedora."
    )
    print(f"Sensores administrados: {sistema.cantidad_sensores()}")

    print("\nPruebas terminadas correctamente.")
    print("Los valores utilizados son simulados y no clínicos.")
