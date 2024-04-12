from sqlalchemy.orm.session import Session
from sqlalchemy.exc import IntegrityError
from .schemas import UserRequest, UserResponse
from .models import User
from sqlite.hash import Hash
from sqlalchemy.orm import joinedload


def create(db: Session, request: UserRequest) -> UserResponse:
    try:
        new_user = User(
            username=request.username,
            email=request.email,
            password=Hash.bcrypt(request.password),
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)  # this allows to give us an userId

        """ # Explicitly load tasks for the new_user
        db.refresh(new_user)
        db.expunge(new_user)
        new_user_with_tasks = (
            db.query(User).options(joinedload(User.tasks)).get(new_user.id)
        )
 """
        return UserResponse.from_orm(new_user)
    # return new_user
    except IntegrityError as e:
        # Handle IntegrityError (UNIQUE constraint violation)
        db.rollback()
        print(f"Error creating user: {e}")
    finally:
        db.close()


def login(db: Session, request: UserRequest) -> UserResponse:
    try:
        user = (
            db.query(User)
            .filter(
                User.email == request.email
                and User.password == Hash.bcrypt(request.password)
            )
            .first()
        )
        db.refresh(user)
        """ db.expunge(user)
        new_user_with_tasks = (
            db.query(User).options(joinedload(User.tasks)).get(user.id)
        ) """

        return UserResponse.from_orm(user)
    # return user
    except Exception as e:
        print(f"Error creating user: {e}")
    finally:
        db.close()
