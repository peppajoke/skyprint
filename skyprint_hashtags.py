import skyprint
import hashtag
import persist

def generate():
    print("Starting work...")

    p = persist.Persist("used_hashtags")
    used_hashtags = p.get()
    if used_hashtags is None:
        used_hashtags = []

    hashtags = hashtag.fetch_trending_hashtags(30)

    hashtags = [elem for elem in hashtags if elem not in used_hashtags]

    for hashtagi in hashtags:
        used_hashtags.append(hashtagi)

    p.set(used_hashtags)

    #  t shirt ideas go here
    ideas = hashtags

    skyprint.make_shirts(ideas)

