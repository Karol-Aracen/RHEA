Sistema RHEA: Registro y monitoreo conceptual de sensores hormonales.

Descripción: RHEA es un sistema conceptual desarrollado en Python mediante programación orientada a objetos. Permite registrar sensores hormonales, consultar y actualizar valores simulados, activar y desactivar sensores y visualizar información de los analitos.

Analitos contemplados
  FSH
  LH
  Estradiol
  Progesterona
  Insulina
  Cortisol

Conceptos de programación orientada a objetos:
  Encapsulamiento: protección del atributo valor_detectado mediante una propiedad y validaciones.
  Herencia: SensorHormonalAvanzado hereda de RegistroRHEA.
  Polimorfismo: sobrescritura del método mostrar_informacion().
  Composición: SistemaMonitoreoRHEA contiene una colección de objetos sensores y delega operaciones en ellos.
  Modularización: separación de las clases y las pruebas en modelos.py y main.py.

Estructura:
  modelos.py: definición de clases y métodos.
  main.py: importaciones, instanciación y pruebas del sistema.
  diagrama_UML.png: representación de la estructura de clases.
Consideraciones

Los valores utilizados son simulados y no representan resultados clínicos ni rangos de referencia médicos.
