# from demo_flask import app
from web_flask import app

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port="3333")
