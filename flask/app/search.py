import pytrends
from pytrends.request import TrendReq
from urllib.parse import urlparse, parse_qs

def get_trending_searches(top):
    # Initialize pytrends API client
    pytrends = TrendReq()

    top_trending_searches = pytrends.today_searches(pn='US')
    top_trending_searches.head(top)

    output = []

    for top_trending_search in top_trending_searches:
        output.append(format_trend(top_trending_search))

    return output

def format_trend(trend):
    parsed_url = urlparse(trend)
    query_values = parse_qs(parsed_url.query)
    return [query_values[key][0] for key in query_values]