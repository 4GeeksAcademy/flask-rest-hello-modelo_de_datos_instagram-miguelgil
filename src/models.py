from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    firstname: Mapped[str] = mapped_column(String(120), nullable=False)
    lastname: Mapped[str] = mapped_column(String(120), nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email
        }


class Follower(db.Model):
    __tablename__ = 'follower'

    user_from_id: Mapped[int] = mapped_column(ForeignKey('user.id'), primary_key=True)
    user_to_id: Mapped[int] = mapped_column(ForeignKey('user.id'), primary_key=True)


class Post(db.Model):
    __tablename__ = 'post'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)


class Comment(db.Model):
    __tablename__ = 'comment'

    id: Mapped[int] = mapped_column(primary_key=True)
    comment_text: Mapped[str] = mapped_column(String(255), nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)
    post_id: Mapped[int] = mapped_column(ForeignKey('post.id'), nullable=False)


class Media(db.Model):
    __tablename__ = 'media'

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(Enum('image', 'video', name='media_types'), nullable=False)
    url: Mapped[str] = mapped_column(String(255), nullable=False)
    post_id: Mapped[int] = mapped_column(ForeignKey('post.id'), nullable=False)