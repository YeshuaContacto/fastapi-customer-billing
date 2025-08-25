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

## 📂 Estructura del proyecto

```bash
.
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── routers
│   │   ├── customers.py
│   │   ├── invoices.py
│   │   ├── plans.py
│   │   └── transactions.py
│   └── tests
│       ├── tests.py
│       └── tests_customers.py
├── db.py
├── models.py
├── create_multiple_transactions.py
├── requirements.txt
└── README.md
|
+---images
|       der.png
|       fastapi.png
|       report_tests.png
|       run_fastapi.png
|
\---__pycache__
        conftest.cpython-313-pytest-8.4.1.pyc
        db.cpython-313.pyc
        main.cpython-313.pyc
        models.cpython-313.pyc
```

## Diagrama de BD
```mermaid
erDiagram
    CUSTOMER {
        int id
        string name
        string description
        string email
        int age
    }
    PLAN {
        int id
        string name
        float price
        string description
    }
    CUSTOMERPLAN {
        int id
        int plan_id
        int customer_id
        string status
    }
    TRANSACTION {
        int id
        float amount
        string description
        int customer_id
    }

    CUSTOMER ||--o{ CUSTOMERPLAN : subscribes
    PLAN ||--o{ CUSTOMERPLAN : offers
    CUSTOMER ||--o{ TRANSACTION : makes


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
