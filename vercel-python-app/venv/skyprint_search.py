import search
import skyprint

def generate():    
    searches = search.get_trending_searches(10)

    shirts_to_make = []

    for searchy in searches:
        if len(searchy[0]) < 6:
            shirts_to_make.append(searchy[0])

    skyprint.make_shirts(shirts_to_make)
