from flask import Flask
import datetime

app = Flask(__name__)

@app.route("/")
def hello():
  now = datetime.datetime.now()
  return "Hello from flask! {0}".format(now)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True, port=80)
