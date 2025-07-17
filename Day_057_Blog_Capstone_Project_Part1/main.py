import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    blog_posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template(template_name_or_list="index.html", posts=blog_posts )

@app.route("/post/<int:num>")
def get_post(num):
    posts_for_sale = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template(template_name_or_list="post.html", post_id = num, blog_posts=posts_for_sale)



if __name__ == "__main__":
    app.run(debug=True)
