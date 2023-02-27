from flask import Flask
import skyprint_hashtags
import skyprint_search

app = Flask(__name__)

@app.route('/')
def hello_world():
    skyprint_hashtags.generate()
    skyprint_search.generate()
    return 'Success!'

if __name__ == '__main__':
    app.run()