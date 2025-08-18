from fastapi import status

def test_create_customer(client):
    response = client.post(
        "/customers",
        json={
            "name": "Jhon Doe",
            "email": "jhon@example.com",
            "age": 33
        },
    )
    assert response.status_code == status.HTTP_201_CREATED


def test_read_customer(client):
    response = client.post(
        "/customers",
        json={
            "name": "Jhon Doe",
            "email": "jhon@example.com",
            "age": 33
        },
    )
    assert response.status_code == status.HTTP_201_CREATED
    customer_id: int = response.json()["id"]
    response_read = client.get(f"/customers/{customer_id}")
    assert response_read.status_code == status.HTTP_200_OK
    assert response_read.json()["name"] == "Jhon Doe"


def test_list_customers(client):
    response = client.post(
        "/customers",
        json={
            "name": "Jhon Doe",
            "email": "jhon@example.com",
            "age": 33
        },
    )
    response = client.get("/customers")
    assert response != None
    assert response != []
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0


def test_update_customer(client):
    # 1. Crear un cliente
    response = client.post(
        "/customers",
        json={
            "name": "Jane Doe",
            "email": "jane@example.com",
            "age": 25,
        },
    )
    assert response.status_code == status.HTTP_201_CREATED
    customer_id = response.json()["id"]

    # 2. Actualizar un campo (PATCH)
    response_patch = client.patch(
        f"/customers/{customer_id}",
        json={"age": 26},
    )
    assert response_patch.status_code == status.HTTP_200_OK
    assert response_patch.json()["age"] == 26

    # 3. Confirmar que realmente se guardó el cambio
    response_read = client.get(f"/customers/{customer_id}")
    assert response_read.status_code == status.HTTP_200_OK
    assert response_read.json()["age"] == 26


def test_delete_customer(client):
    # 1. Crear un cliente
    response = client.post(
        "/customers",
        json={
            "name": "Alice",
            "email": "alice@example.com",
            "age": 28,
        },
    )
    assert response.status_code == status.HTTP_201_CREATED
    customer_id = response.json()["id"]

    # 2. Eliminar el cliente
    response_delete = client.delete(f"/customers/{customer_id}")
    assert response_delete.status_code == status.HTTP_200_OK
    assert response_delete.json()["Detail"] == "ok"

    # 3. Intentar leer el cliente borrado
    response_read = client.get(f"/customers/{customer_id}")
    assert response_read.status_code == status.HTTP_404_NOT_FOUND



