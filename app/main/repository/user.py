import datetime
from app.main.model.user import User
from app.main import db


class UserRepository:
    def get_all_users(self):
        return User.query.filter_by(deleted_at=None).all()

    def get_user_by_id(self, id: int):
        return User.query.filter_by(id=id).filter_by(deleted_at=None).first_or_404()

    def create_user(self, data: User):
        user = User(
            username=data["username"], email=data["email"], password=data["password"]
        )
        user.set_updated_at(datetime.datetime.utcnow())
        user.set_created_at(datetime.datetime.utcnow())
        self.save_changes(user)

    def delete_user_by_id(self, id: int):
        user = self.get_user_by_id(id=id)
        if user is None:
            raise ("user not found")
        user.set_deleted_at(datetime.datetime.utcnow())
        self.save_changes(user)
        return

    def save_changes(self, data: User):
        db.session.add(data)
        db.session.commit()
