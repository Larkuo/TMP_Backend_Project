from app.models.user import User
from app.extensions import db

def get_user_by_id(id):
    return db.session.get(User, id=id)

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_user_by_email(email):
    return User.query.filter_by(email=email).first()

def create_new_user(data):    
    new_user = User(
        username=data['username'], 
        email=data['email'],
        is_admin=data['is_admin']
    )
    new_user.set_password(data['password'])

    db.session.add(new_user)
    db.session.commit()

    return new_user

def update_user_by_id(user_id, data):
    user = get_user_by_id(user_id)

    # TODO: Update this to handle password change
    for key, value in data.items():
        setattr(user, key, value)
    
    db.session.commit()
    return user

def delete_user_by_id(user_id):
    user = get_user_by_id(user_id)

    db.session.delete(user)
    db.session.commit()