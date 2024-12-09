def test_create_user(client):
    user_data = {
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'securepassword',
        'role': 'admin'
    }

    response = client.post('/users', json=user_data)

    assert response.status_code == 201
    assert response.json['username'] == user_data['username']
    assert response.json['role'] == user_data['role']
    assert 'password' not in response.json  # password should not be serialized

# def test_invalid_user_missing_username(client):
#     response = client.post('/users', json={'email': 'test@example.com', 'password': 'short'})

#     assert response.status_code == 422
#     assert 'username' in response.json

# def test_invalid_user_existing_user(client):
#     client.post(
#         '/users', 
#         json={'username': 'existinguser', 'email': 'test@example.com', 'password': 'password'})

#     response = client.post('/users', json={'username': 'newuser', 'email': 'test@example.com', 'password': 'securepassword'})

#     assert response.status_code == 403
#     assert response.json['error'] == 'Email already exists'
