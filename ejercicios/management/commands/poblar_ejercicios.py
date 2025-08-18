from django.core.management.base import BaseCommand
from ejercicios.models import Ejercicio, TipoEjercicio
from core.models import Materia,Unidad
from accounts.models import Docente
#  id_materia |              materia               | num_unidad |           unidad
# ------------+------------------------------------+------------+-----------------------------
#           1 | Resolución de problemas en Álgebra |          1 | Ecuaciones lineales
#           1 | Resolución de problemas en Álgebra |          2 | Ecuaciones cuadráticas
#           1 | Resolución de problemas en Álgebra |          3 | Sistema de ecuaciones
#           2 | Funciones y Matrices               |          1 | Funciones reales
#           2 | Funciones y Matrices               |          2 | Composición inversa
#           2 | Funciones y Matrices               |          3 | Álgebra de matrices
#           2 | Funciones y Matrices               |          4 | Determinantes y rango
#           3 | Calculo I                          |          1 | Limites y continuidad
#           3 | Calculo I                          |          2 | Derivadas básicas
#           3 | Calculo I                          |          3 | Aplicaciones de la derivada
#           3 | Calculo I                          |          4 | Integrales indefinidas

class Command(BaseCommand):
    help = "Pobla la base de datos con ejercicios de matrices"

    def handle(self, *args, **options):
        # Asegurar que existan relaciones base
        materia_id = 2
        unidad_id = 3
        docente_id = None
        tipo_ejercicio = 2

        # Lista de ejercicios (simulados, puedes reemplazar con los reales)
        ejercicios_data = [
            {
                "enunciado": "f(x)=5x+4 f=2?",
                "solucion": "14",
                "dificultad": 0.02,
                # "estructura": {"A": [[1,2],[3,4]], "B": [[5,6],[7,8]], "operacion": "suma"},
                "fuente": "prueba1.1",
                "licencia": None
            },

            {
                "enunciado": "f(x)=2x+3 f=5?",
                "solucion": "13",
                "dificultad": 0.03,
                # "estructura": {"M": [[1,2,3],[4,5,6]], "operacion": "transpuesta"},
                "fuente": "prueba1.2",
                "licencia": None
            }
        ]

        for data in ejercicios_data:
            ejercicio, created = Ejercicio.objects.get_or_create(
                materia_id=materia_id,
                unidad_id=unidad_id,
                docente_id=docente_id,
                enunciado=data["enunciado"],
                solucion=data["solucion"],
                dificultad=data["dificultad"],
                fuente=data["fuente"],
                licencia=data["licencia"]
            )

            # Asignar el ManyToMany después
            ejercicio.tipo_ejercicio.set([tipo_ejercicio])
            ejercicio.save()
        # Mensaje de éxito
        if created:
            self.stdout.write(self.style.SUCCESS(f"Ejercicios de matrices creados: {len(ejercicios_data)}"))
        else:
            self.stdout.write(self.style.WARNING("Error al insertar ejercicios."))

        # self.stdout.write(self.style.SUCCESS("Ejercicios insertados correctamente."))