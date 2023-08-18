import json

def open_post_data():
    with open("blog_posts.json") as open_file:
        return json.load(open_file)

posts = open_post_data()
print(posts[-1])