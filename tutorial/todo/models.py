# Entity

from todo import db
from sqlalchemy import text


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)  # text
    description = db.Column(db.Text(), nullable=False)  # textarea
    created = db.Column(db.DateTime(), nullable=False)
    # default = False (flask app 실행)
    # server_default=text("false") : 테이블 생성 구문에 추가
    completed = db.Column(db.Boolean(), default=False, server_default=text("false"))
    important = db.Column(db.Boolean(), default=False, server_default=text("false"))
