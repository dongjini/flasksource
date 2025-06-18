from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")  # == @GetMapping("/")
def index():
    return "Hello!!!"


@app.route("/create", methods=["GET", "POST"])  # == @GetMapping("/create")
def create():
    # return "Create"
    if request.method == "GET":
        return render_template("create.html")
    else:
        name = request.form["name"]  # dictionally 의 key값 가져오는거
        print(f"name {name}")
    return redirect("/")


@app.route("/read/<int:post_id>")  # == @GetMapping("/read/1")
def read(post_id):
    return f"Read {post_id}"
