# Clase 14: Programación Orientada a Objetos - Herencia

## Introducción
La **herencia** es un pilar fundamental de la **Programación Orientada a Objetos (POO)**. Permite que una clase hija herede atributos y métodos de una clase padre, promoviendo la reutilización del código y la creación de jerarquías de clases más estructuradas.

## Conceptos Claves

1. **Clase Padre (Superclase)**: Es la clase base que contiene atributos y métodos comunes.
2. **Clase Hija (Subclase)**: Es la clase que hereda de la superclase y puede ampliar o modificar su comportamiento.
3. **Herencia Simple**: Una subclase hereda de una única superclase.
4. **Herencia Múltiple**: Una subclase hereda de múltiples superclases.
5. **Sobreescritura de Métodos**: Una subclase puede redefinir métodos de la superclase.
6. **Uso de `super()`**: Permite acceder a los métodos de la superclase desde la subclase.

## Representación Visual

### Jerarquía de Clases
![Herencia en POO](./14.0.png)

En la imagen se muestra cómo la clase **Humano** representa la superclase y la clase **Estudiante** es una subclase que hereda de **Humano**.

## Implementación en Código

Ejemplo de implementación en **Python**:

```python
# Definición de la superclase
class Humano:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def hablar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

# Definición de la subclase que hereda de Humano
class Estudiante(Humano):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)  # Llamamos al constructor de la superclase
        self.grado = grado
    
    def estudiar(self):
        print(f"Soy {self.nombre}, tengo {self.edad} años y estudio en {self.grado}.")

# Creación de instancias
persona = Humano("Carlos", 40)
estudiante = Estudiante("Ana", 20, "Universidad")

# Uso de los métodos
persona.hablar()
estudiante.hablar()
estudiante.estudiar()
```

## Explicación del Código
- Se define la clase `Humano` con atributos `nombre` y `edad`, y el método `hablar()`.
- `Estudiante` hereda de `Humano` y añade el atributo `grado` junto con un nuevo método `estudiar()`.
- `super().__init__(nombre, edad)` llama al constructor de la superclase `Humano`.
- Se crean objetos de ambas clases y se llaman sus métodos para demostrar la herencia.

## Beneficios de la Herencia
✔ **Reutilización de código**: Evita la repetición de código en múltiples clases.

✔ **Jerarquía estructurada**: Organiza mejor el código mediante relaciones de clases.

✔ **Extensibilidad**: Facilita la ampliación de funcionalidades sin modificar la superclase.

✔ **Mantenimiento eficiente**: Los cambios en la superclase afectan automáticamente a las subclases.

## Conclusión
La herencia es un mecanismo poderoso en **POO**, ya que permite modelar relaciones entre clases de manera eficiente y reutilizable. Su correcto uso mejora la organización del código y facilita la creación de sistemas escalables.

---

## 👨‍💻 Sobre el Autor

- **👤 Nombre:** Edwin Yoner
- **📧 Contacto:** [✉ edwinyoner@gmail.com](mailto:edwinyoner@gmail.com)
- **🔗 LinkedIn:** [🌐 linkedin.com/in/edwinyoner](https://www.linkedin.com/in/edwinyoner)