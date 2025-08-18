import json
from django.core.management.base import BaseCommand
from ejercicios.models import Ejercicio, PasoEjercicio

class Command(BaseCommand):
    help = 'Importar ejercicios desde un archivo JSON'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Ruta del archivo JSON con los ejercicios')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                for item in data:
                    ejercicio = Ejercicio.objects.create(
                        enunciado=item['enunciado'],
                        fuente=item.get('fuente', 'real')
                    )
                    for paso in item.get('pasos', []):
                        PasoEjercicio.objects.create(
                            ejercicio=ejercicio,
                            orden=paso['orden'],
                            contenido=paso['contenido']
                        )
                self.stdout.write(self.style.SUCCESS('Ejercicios importados exitosamente'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error al importar ejercicios: {e}'))