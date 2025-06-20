from flask import Blueprint, redirect, url_for

# Blueprint("펼칭", 실행되는 모듈명가져오기, url_prefix="/")
bp = Blueprint("main", __name__, url_prefix="/")


@bp.route("/")
def index():
    return redirect(url_for("book.list"))
