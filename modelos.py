"""
Sistema RHEA: Registro y monitoreo conceptual de sensores hormonales.

Este módulo contiene las clases del sistema y sus relaciones de herencia
y composición. Los valores utilizados son simulados y no representan
resultados clínicos ni rangos de referencia médicos.
"""

# Catálogo de hormonas y analitos contemplados en el proyecto RHEA.
HORMONAS_RHEA = [
    "FSH",
    "LH",
    "Estradiol",
    "Progesterona",
    "Insulina",
    "Cortisol"
]


# ==========================================================
# CLASE BASE
# ==========================================================

class RegistroRHEA:
    """Representa un registro general de un sensor hormonal."""

    def __init__(
        self,
        codigo,
        hormona_objetivo,
        valor_detectado,
        tipo_muestra,
        activo=True
    ):
        self.codigo = codigo
        self.hormona_objetivo = hormona_objetivo
        self.tipo_muestra = tipo_muestra

        # Encapsulamiento: el valor se almacena como atributo privado.
        self.__valor_detectado = None

        # El setter valida el valor antes de almacenarlo.
        self.valor_detectado = valor_detectado
        self.activo = bool(activo)

    # ======================================================
    # ENCAPSULAMIENTO
    # ======================================================

    @property
    def valor_detectado(self):
        """Getter: permite consultar el valor almacenado."""
        return self.__valor_detectado

    @valor_detectado.setter
    def valor_detectado(self, nuevo_valor):
        """Setter: valida los datos antes de modificarlos."""
        if (
            not isinstance(nuevo_valor, (int, float))
            or isinstance(nuevo_valor, bool)
        ):
            raise TypeError("El valor detectado debe ser un número.")

        if nuevo_valor < 0:
            raise ValueError("El valor detectado no puede ser negativo.")

        self.__valor_detectado = float(nuevo_valor)

    # ======================================================
    # MÉTODOS OPERATIVOS
    # ======================================================

    def activar(self):
        """Activa el registro del sensor."""
        self.activo = True
        return (
            f"El sensor {self.codigo} "
            f"({self.hormona_objetivo}) ha sido activado."
        )

    def desactivar(self):
        """Desactiva el registro del sensor."""
        self.activo = False
        return (
            f"El sensor {self.codigo} "
            f"({self.hormona_objetivo}) ha sido desactivado."
        )

    def actualizar_valor(self, nuevo_valor):
        """Actualiza el valor mediante el setter validado."""
        self.valor_detectado = nuevo_valor
        return (
            f"El sensor {self.codigo} registró un nuevo valor de "
            f"{self.valor_detectado:.2f}."
        )

    def mostrar_informacion(self):
        """Muestra los datos generales del sensor."""
        estado = "Activo" if self.activo else "Inactivo"

        return (
            f"----- Registro RHEA -----\n"
            f"Código: {self.codigo}\n"
            f"Hormona objetivo: {self.hormona_objetivo}\n"
            f"Valor detectado: {self.valor_detectado:.2f}\n"
            f"Tipo de muestra: {self.tipo_muestra}\n"
            f"Estado: {estado}"
        )


# ==========================================================
# SUBCLASE: HERENCIA Y POLIMORFISMO
# ==========================================================

class SensorHormonalAvanzado(RegistroRHEA):
    """
    Representa un sensor avanzado que hereda de RegistroRHEA.
    Añade información sobre la tecnología y la unidad de medición.
    """

    def __init__(
        self,
        codigo,
        hormona_objetivo,
        valor_detectado,
        tipo_muestra,
        tecnologia,
        unidad,
        activo=True
    ):
        # super() reutiliza el constructor de la clase base.
        super().__init__(
            codigo,
            hormona_objetivo,
            valor_detectado,
            tipo_muestra,
            activo
        )

        self.tecnologia = tecnologia
        self.unidad = unidad

    def calibrar(self):
        """Simula una operación conceptual de calibración."""
        return (
            f"Calibración conceptual del sensor {self.codigo} "
            f"mediante {self.tecnologia}. "
            f"Analito: {self.hormona_objetivo}."
        )

    def mostrar_informacion(self):
        """Sobrescribe el método heredado para mostrar más datos."""
        estado = "Activo" if self.activo else "Inactivo"

        return (
            f"----- Sensor RHEA Avanzado -----\n"
            f"Código: {self.codigo}\n"
            f"Hormona objetivo: {self.hormona_objetivo}\n"
            f"Valor detectado: {self.valor_detectado:.2f} "
            f"{self.unidad}\n"
            f"Tipo de muestra: {self.tipo_muestra}\n"
            f"Tecnología: {self.tecnologia}\n"
            f"Estado: {estado}"
        )


# ==========================================================
# CLASE AUXILIAR: COMPOSICIÓN
# ==========================================================

class SistemaMonitoreoRHEA:
    """
    Representa el sistema que administra los registros de sensores.

    COMPOSICIÓN: contiene una lista de objetos RegistroRHEA
    o de sus subclases y utiliza sus métodos de manera delegada.
    """

    def __init__(self, nombre="Sistema de monitoreo RHEA"):
        self.nombre = nombre
        self.sensores = []

    def agregar_sensor(self, sensor):
        """Agrega un objeto sensor a la colección del sistema."""
        if not isinstance(sensor, RegistroRHEA):
            raise TypeError(
                "Solo se pueden agregar objetos de tipo RegistroRHEA."
            )

        if self.buscar_sensor(sensor.codigo) is not None:
            raise ValueError(
                f"Ya existe un sensor con el código {sensor.codigo}."
            )

        self.sensores.append(sensor)
        return f"Sensor {sensor.codigo} agregado al sistema."

    def buscar_sensor(self, codigo):
        """Busca y devuelve un sensor mediante su código."""
        for sensor in self.sensores:
            if sensor.codigo == codigo:
                return sensor
        return None

    def mostrar_sensores(self):
        """Muestra la información de todos los sensores registrados."""
        if not self.sensores:
            return "No hay sensores registrados en el sistema."

        informacion = []
        for sensor in self.sensores:
            # Delegación: se utiliza el método del objeto contenido.
            informacion.append(sensor.mostrar_informacion())

        return "\n\n".join(informacion)

    def actualizar_sensor(self, codigo, nuevo_valor):
        """Localiza un sensor y delega en él la actualización del valor."""
        sensor = self.buscar_sensor(codigo)

        if sensor is None:
            return f"No se encontró el sensor {codigo}."

        return sensor.actualizar_valor(nuevo_valor)

    def activar_sensor(self, codigo):
        """Localiza un sensor y delega en él la activación."""
        sensor = self.buscar_sensor(codigo)

        if sensor is None:
            return f"No se encontró el sensor {codigo}."

        return sensor.activar()

    def desactivar_sensor(self, codigo):
        """Localiza un sensor y delega en él la desactivación."""
        sensor = self.buscar_sensor(codigo)

        if sensor is None:
            return f"No se encontró el sensor {codigo}."

        return sensor.desactivar()

    def cantidad_sensores(self):
        """Devuelve la cantidad de sensores registrados."""
        return len(self.sensores)
