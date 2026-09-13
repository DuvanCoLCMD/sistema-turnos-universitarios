class ColaTurnos:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.datos = [None] * capacidad
        self.frente = 0
        self.final = 0
        self.cantidad = 0

    def esta_vacia(self):
        return self.cantidad == 0

    def esta_llena(self):
        return self.cantidad == self.capacidad

    def agregar_turno(self, estudiante):
        if self.esta_llena():
            print("No se puede agregar el turno. La cola está llena.")
            return False

        self.datos[self.final] = estudiante
        self.final += 1
        self.cantidad += 1

        print(f"Turno agregado: {estudiante}")
        return True

    def atender_turno(self):
        if self.esta_vacia():
            print("No hay estudiantes para atender. La cola está vacía.")
            return None

        estudiante = self.datos[self.frente]

        for i in range(self.frente, self.final - 1):
            self.datos[i] = self.datos[i + 1]   

        self.datos[self.final - 1] = None
        self.final -= 1
        self.cantidad -= 1

        print(f"Estudiante atendido: {estudiante}")
        return estudiante

    def siguiente_turno(self):
        if self.esta_vacia():
            print("No hay estudiantes esperando.")
            return None

        return self.datos[self.frente]

    def mostrar_cola(self):
        if self.esta_vacia():
            print("La cola está vacía.")
            return

        print("\nEstudiantes en espera:")

        for i in range(self.frente, self.final):
            print(f"{i + 1}. {self.datos[i]}")


# Programa principal

cola = ColaTurnos(5)

print("===== SISTEMA DE TURNOS UNIVERSITARIOS =====")

print("\n--- Registro de estudiantes ---")

cola.agregar_turno("Andres Castor")
cola.agregar_turno("Angela Gómez")
cola.agregar_turno("Carlos Rodríguez")

cola.mostrar_cola()

print("\n--- Siguiente estudiante ---")

print("Siguiente turno:", cola.siguiente_turno())

print("\n--- Atención de estudiantes ---")

cola.atender_turno()
cola.atender_turno()

cola.mostrar_cola()

print("\n--- Caso límite: intentar atender una cola vacía ---")

cola.atender_turno()
cola.atender_turno()

print("\n--- Caso límite: llenar la cola ---")

cola.agregar_turno("Ana López")
cola.agregar_turno("Pedro Martínez")
cola.agregar_turno("Laura Torres")
cola.agregar_turno("Andrés Díaz")
cola.agregar_turno("Sofía Ramírez")

cola.mostrar_cola()

print("\n--- Intentar agregar un estudiante con la cola llena ---")

cola.agregar_turno("Daniel Castro")