from flask import Blueprint, redirect, url_for

# Blueprint("별칭", 실행되는 모듈명 가져오기, url_prefix="/")
bp = Blueprint("main", __name__, url_prefix="/")


@bp.route("/")
def index():
    # url 지정할 때 사용하는 함수
    # 주소를 지정하진 않고 별칭을 넣음
    return redirect(url_for("todo.list"))
