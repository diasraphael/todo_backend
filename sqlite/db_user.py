from sqlalchemy.orm.session import Session
from sqlalchemy.exc import IntegrityError
from .schemas import UserRequest,UserResponse
from .models import User
from .hash import Hash
from typing import List


def create_user(db:Session, request:UserRequest)-> UserResponse:
  try:
    new_user = User(
      username=request.username,
      email=request.email,
      password=Hash.bcrypt(request.password)
      )
    db.add(new_user)
    db.commit()
    db.refresh(new_user) # this allows to give us an userId
    return UserResponse(user_id=new_user.id, username=new_user.username, email=new_user.email)
  except IntegrityError as e:
    # Handle IntegrityError (UNIQUE constraint violation)
    db.rollback()
    print(f'Error creating user: {e}')
  finally:
    db.close()

def user_to_user_response(user:User):
  return UserResponse(user_id=user.id, username=user.username, email=user.email)

def get_all_users(db:Session)-> List[UserResponse]:
  users = db.query(User).all()
  return [user_to_user_response(user) for user in users]

def login_user(db:Session, request:UserRequest)-> UserResponse:
  try:
      user = db.query(User).filter(User.email == request.email and User.password == Hash.bcrypt(request.password)).first()
      if user:
            return UserResponse(user_id=user.id, username=user.username, email=user.email)
      else:
            return UserResponse(user_id=None, username=None, email=None)  
  except Exception as e:
    db.rollback()
    print(f'Error creating user: {e}')
  finally:
    db.close()