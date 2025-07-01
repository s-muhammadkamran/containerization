import time
import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.RedisError as e:
            if retries == 0:
                raise e
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def welcome():
    count = get_hit_count()
    return "<h1>Welcome to my website! You have visited this page {} times.</h1>".format(count)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)