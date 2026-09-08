# QA Project — Urban Grocers: Validación del campo "name" al crear un kit

## Descripción
Este proyecto automatiza la lista de comprobación para el campo `name` en el endpoint
de creación de un kit de productos de la aplicación Urban Grocers, verificando límites
de caracteres, caracteres especiales, espacios, números, ausencia del campo y tipo de dato incorrecto.

## Archivos
- `configuration.py`: URL base y rutas de la API.
- `data.py`: cuerpos de solicitud (usuario y kit) y valores límite de caracteres.
- `sender_stand_request.py`: funciones para enviar solicitudes POST.
- `create_kit_name_kit_test.py`: pruebas automatizadas con Pytest.

## Cómo ejecutar las pruebas
1. Instalar dependencias:# Proyecto Urban Grocers 
2. pip install pytest requests

Ejecutar las pruebas:

pytest create_kit_name_kit_test.py -v


## Resultado esperado
Algunas pruebas marcan `FAILED` porque revelan defectos reales de validación en el backend
(nombre vacío, nombre de 512 caracteres y tipo de dato incorrecto son aceptados con código 201
en vez de 400; y la ausencia del campo `name` devuelve un error 500 en vez de 400).
Este comportamiento es el esperado según la consigna del sprint.
