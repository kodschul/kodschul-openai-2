from flask import Flask, render_template, request, jsonify
import post

app = Flask(__name__)


@app.route("/")
def posts():
    return render_template("blog.html",  posts=post.get_all_posts())


@app.route("/<slug>")
def get_post():
    return render_template("blog_post.html")


app.run(debug=True)
