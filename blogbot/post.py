import json


def get_all_posts():
    try:
        with open("posts.json", "r", encoding="utf-8") as f:
            raw_json = json.load(f)
            return list(raw_json)
    except:
        return []


def get_post(slug):
    posts = get_all_posts()

    for post in posts:
        if slug in post["slug"]:
            return post

    return None


def add_post(post):
    posts = get_all_posts()
    posts.insert(0, post)

    with open("posts.json", "w+", encoding="utf-8") as f:
        json.dump(posts, f)
