import search

searches = search.get_trending_searches(10)

for searchy in searches:
    print(searchy)