def test_get_products(client):
    response = client.get('/products')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_get_product(client):
    product_id = 1
    response = client.get(f'/products/{product_id}')
    assert response.status_code == 200
    assert "name" in response.json

def test_create_product(client, admin_headers):
    new_product = {
        "name": "Chocolate Cake",
        "category": "Dessert",
        "price": 10.50,
        "image_thumbnail": "path/to/thumbnail.jpg",
        "image_mobile": "path/to/mobile.jpg",
        "image_tablet": "path/to/tablet.jpg",
        "image_desktop": "path/to/desktop.jpg"
    }
    response = client.post('/products', json=new_product, headers=admin_headers)
    assert response.status_code == 201
    assert response.json["name"] == "Chocolate Cake"

def test_update_product(client, admin_headers):
    product_id = 1
    update_data = {"price": 12.00}
    response = client.put(f'/products/{product_id}', json=update_data, headers=admin_headers)
    assert response.status_code == 200
    assert response.json["price"] == "12.00"

def test_delete_product(client, admin_headers):
    product_id = 1
    response = client.delete(f'/products/{product_id}', headers=admin_headers)
    assert response.status_code == 200
    assert response.json["message"] == "Product deleted successfully"
