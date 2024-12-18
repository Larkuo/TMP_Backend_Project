from flask import json

def test_get_products(client):
    # Act
    response = client.get('/products')

    # Assert
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_get_product(client):
    # Arrange
    product_id = 1
    new_product = {
        "name": "Chocolate Cake",
        "category": "Dessert",
        "price": 10.50,
        "image_thumbnail": "path/to/thumbnail.jpg",
        "image_mobile": "path/to/mobile.jpg",
        "image_tablet": "path/to/tablet.jpg",
        "image_desktop": "path/to/desktop.jpg"
    }

    # Act
    client.post(
        '/products', 
        data=json.dumps(new_product), 
        headers={'Content-Type': 'application/json'}
    )
    response = client.get(f'/products/{product_id}')

    # Assert
    assert response.status_code == 200
    assert "name" in response.json

def test_create_product(client):
    # Arrange
    new_product = {
        "name": "Chocolate Cake",
        "category": "Dessert",
        "price": 10.50,
        "image_thumbnail": "path/to/thumbnail.jpg",
        "image_mobile": "path/to/mobile.jpg",
        "image_tablet": "path/to/tablet.jpg",
        "image_desktop": "path/to/desktop.jpg"
    }

    # Act
    response = client.post(
        '/products', 
        data=json.dumps(new_product), 
        headers={'Content-Type': 'application/json'}
    )

    # Assert
    assert response.status_code == 201
    assert response.json["name"] == "Chocolate Cake"
    assert response.json["price"] == "10.50"

def test_update_product(client):
    # Arrange
    product_id = 1
    update_data = {"price": 12.00}

    # Act
    create_test_product(client)
    response = client.put(f'/products/{product_id}', json=update_data)

    # Assert
    assert response.status_code == 200
    assert response.json["price"] == "12.00"

def test_delete_product(client):
    # Arrange
    product_id = 1

    # Act
    create_test_product(client)
    response = client.delete(f'/products/{product_id}')

    # Assert
    assert response.status_code == 200
    assert response.json["message"] == "Product deleted successfully"

# helper functions
def create_test_product(client):
    product = {
        "name": "Chocolate Cake",
        "category": "Dessert",
        "price": 10.50,
        "image_thumbnail": "path/to/thumbnail.jpg",
        "image_mobile": "path/to/mobile.jpg",
        "image_tablet": "path/to/tablet.jpg",
        "image_desktop": "path/to/desktop.jpg"
    }

    client.post('/products', data=json.dumps(product), headers={'Content-Type': 'application/json'})