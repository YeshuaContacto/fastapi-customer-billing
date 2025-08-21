# FastAPI
![FastAPI](images/fastapi.png)

## Instalación  
```
pip install -r requirements.txt
```
Ejecutar la aplicación en modo desarrollo.
```
fastapi dev
```
![Run FastAPI](images/run_fastapi.png)

## Estructura de la aplicación
|   .gitignore
|   conftest.py
|   create_multiple_transactions.py
|   db.py
|   db.sqlite3
|   models.py
|   README.md
|   requirements.txt
|
+---.pytest_cache
|   |   .gitignore
|   |   CACHEDIR.TAG
|   |   README.md
|   |
|   \---v
|       \---cache
|               lastfailed
|               nodeids
|
+---app
|   |   main.py
|   |   __init__.py
|   |
|   +---routers
|   |   |   customers.py
|   |   |   invoices.py
|   |   |   plans.py
|   |   |   transactions.py
|   |   |   __init__.py
|   |   |
|   |   \---__pycache__
|   |           customers.cpython-313.pyc
|   |           invoices.cpython-313.pyc
|   |           plans.cpython-313.pyc
|   |           transactions.cpython-313.pyc
|   |           __init__.cpython-313.pyc
|   |
|   +---tests
|   |   |   tests.py
|   |   |   tests_customers.py
|   |   |   __init__.py
|   |   |
|   |   \---__pycache__
|   |           tests_customers.cpython-313-pytest-8.4.1.pyc
|   |           __init__.cpython-313.pyc
|   |
|   \---__pycache__
|           main.cpython-313.pyc
|           tests.cpython-313-pytest-8.4.1.pyc
|           __init__.cpython-313.pyc
|
+---images
|       der.png
|       estructura.png
|       fastapi.png
|       report_tests.png
|       run_fastapi.png
|
\---__pycache__
        conftest.cpython-313-pytest-8.4.1.pyc
        db.cpython-313.pyc
        main.cpython-313.pyc
        models.cpython-313.pyc

## Diagrama de BD
![Diagrama DB](images/der.png)

## Midlewares
Permiten agregar funcionalidades a todos los requests y response de nuestra API


## Template de la comunidad 

La comunidad de FastAPI ha creado un template listo para su uso. Puedes encontrarlo en el siguiente [enlace](https://github.com/fastapi/full-stack-fastapi-template)
```
https://github.com/fastapi/full-stack-fastapi-template
```

## Reporte de pruebas unitarias
```
coverage run --source app/ -m pytest
coverage report
```
![Reporte pruebas unitarias](images/report_tests.png)
