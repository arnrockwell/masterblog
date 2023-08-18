from flask import Flask, request, render_template, redirect, url_for
import json

app = Flask(__name__)
post_data = "blog_posts.json"


def open_post_data(file_name):
    # Open the JSON file containing the blog posts
    with open(file_name, "r") as open_file:
        return json.load(open_file)

def fetch_post_by_id(post_id):
    # Gets the blog post data by id
    # Returns None if no post exists
    posts = open_post_data(post_data)
    found = None
    for post in posts:
        if post["id"] == post_id:
            found = post
            break

    return found


@app.route("/")
def index():
    posts = open_post_data(post_data)
    return render_template("index.html", posts=posts)


@app.route("/add", methods=["GET", "POST"])
def add():
    # Takes the info submitted from the form & creates a new blog post
    # Redirect back to home page
    if request.method == "POST":
        author = request.form.get("author")
        title = request.form.get("title")
        content = request.form.get("content")

        posts = open_post_data(post_data)

        if not posts:
            post_id = 1
        else:
            last_post = posts[-1]
            post_id = int(last_post["id"] + 1)

        new_post = {"id": post_id, "author": author, "title": title,
                    "content": content}
        
        posts.append(new_post)

        with open(post_data, "w") as update_file:
            json.dump(posts, update_file, indent=4)

        return redirect(url_for("index"))

    return render_template("add.html")


@app.route("/update/<int:post_id>", methods=["GET", "POST"])
def update(post_id):
    # Fetch the blog posts from the JSON file
    post = fetch_post_by_id(post_id)
    if post is None:
        # Post not found
        return "Post not Found", 404

    if request.method == "POST":
        # Update the post in the JSON file
        # Redirect back to home page
        author = request.form.get("author")
        title = request.form.get("title")
        content = request.form.get("content")

        post["author"] = author
        post["title"] = title
        post["content"] = content

        # Find post in data by id
        # Delete old post, add new version
        # Sort data by id
        posts = open_post_data(post_data)
        for item in posts:
            if item["id"] == post_id:
                idx = posts.index(item)
                del posts[idx]
                break
        posts.append(post)
        updated_data = sorted(posts, key=lambda i: i["id"])

        with open(post_data, "w") as update_file:
            json.dump(updated_data, update_file, indent=4)

        return redirect(url_for("index"))

    # Else, it's GET request
    # So display the update.html page
    return render_template("update.html", post=post)


@app.route("/delete/<int:post_id>")
def delete(post_id):
    # Find the blog post with the given id and removes it from the list
    # Redirect back to home page
    posts = open_post_data(post_data)
    for post in posts:
        if post["id"] == post_id:
            idx = posts.index(post)
            del posts[idx]
            break

    with open(post_data, "w") as update_file:
        json.dump(posts, update_file, indent=4)

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run("0.0.0.0")