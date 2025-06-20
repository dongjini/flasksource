from flask import Blueprint, redirect, url_for, render_template
from book.forms import UserForm


bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/signup", methoeds=["GET", "POST"])
def signup():
    form = UserForm()
    return render_template("auth/signup.html")
