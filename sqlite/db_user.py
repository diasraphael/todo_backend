from sqlalchemy.orm.session import Session
from sqlalchemy.exc import IntegrityError
from .schemas import UserRequest, UserResponse, TaskRequest, TaskResponse
from .models import User, Task
from .hash import Hash
from typing import List


def create_user(db: Session, request: UserRequest) -> UserResponse:
    try:
        new_user = User(
            username=request.username,
            email=request.email,
            password=Hash.bcrypt(request.password),
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)  # this allows to give us an userId
        return UserResponse(
            user_id=new_user.id, username=new_user.username, email=new_user.email
        )
    except IntegrityError as e:
        # Handle IntegrityError (UNIQUE constraint violation)
        db.rollback()
        print(f"Error creating user: {e}")
    finally:
        db.close()


def user_to_user_response(user: User):
    return UserResponse(user_id=user.id, username=user.username, email=user.email)


def get_all_users(db: Session) -> List[UserResponse]:
    users = db.query(User).all()
    return [user_to_user_response(user) for user in users]

def create_task(db: Session, request: TaskRequest)-> TaskResponse:
    try:
        new_task = Task(
            title=request.title,
            user_id=request.user_id,
        )
        db.add(new_task)
        db.commit()
        db.refresh(new_task)  # this allows to give us an taskId
        return TaskResponse(
            user_id=new_task.user_id, title=new_task.title,task_id=new_task.id
        )
    except IntegrityError as e:
        # Handle IntegrityError (UNIQUE constraint violation)
        db.rollback()
        print(f"Error creating user: {e}")
    finally:
        db.close()

def get_task(db:Session, id: int):
    task = db.query(Task).filter(Task.id == id).first()
    return task

def login_user(db: Session, request: UserRequest) -> UserResponse:
    try:
        user = (
            db.query(User)
            .filter(
                User.email == request.email
                and User.password == Hash.bcrypt(request.password)
            )
            .first()
        )
        if user:
            return UserResponse(
                user_id=user.id, username=user.username, email=user.email
            )
        else:
            return UserResponse(user_id=None, username=None, email=None)
    except Exception as e:
        print(f"Error creating user: {e}")
    finally:
        db.close()
