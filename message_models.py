from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from datetime import datetime

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + "E:/Moses/College_Life/Year3_2/Software_Development_Workshop_III/Code/practice1/second.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "theSecondPractice"

db = SQLAlchemy(app)  # 实例化数据库

# 管理员
class Admin(db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(64), nullable=False)
    tags = db.relationship("Tag", backref="admin")


# 标签
class Tag(db.Model):
    __tablename__ = "tag"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False)  # 标签名字
    admin_id = db.Column(db.Integer, db.ForeignKey("admin.id"))  # 所属管理员


# 用户
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(64), nullable=False)
    tags = db.relationship("Message", backref="user")  # 反向访问


# 留言条
class Message(db.Model):
    __tablename__ = "message"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(256), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)  # 获得发布留言的时间
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))  # 所属用户
    tags = db.relationship("Tag", secondary="message_to_tag", backref="messages")


# 中间表
class MessageToTag(db.Model):
    __tablename__ = "message_to_tag"
    id = db.Column(db.Integer, primary_key=True)
    message_id = db.Column(db.Integer, db.ForeignKey("message.id"))  # 所属留言条
    tag_id = db.Column(db.Integer, db.ForeignKey("tag.id"))  # 所属tag


if __name__ == "__main__":
    db.create_all()
    # db.drop_all()
