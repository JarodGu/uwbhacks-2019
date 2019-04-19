from flask import Flask, render_template, send_file, url_for, request, redirect

app = Flask(__name__)

@app.before_request
def before_request():
    if request.url.startswith("http://"):
        url = request.url.replace("http://", "https://", 1)
        code = 301
        return redirect(url, code=code)
    elif "www." in request.url[7:12]:
        url = request.url.replace("www.", "", 1)
        code = 301
        return redirect(url, code=code)

@app.route("/")
def lol():
    return render_template("index.html")

@app.route("/favicon.ico")
def favicon():
    return send_file("static/favicon.ico")

@app.route("/hello/")
@app.route("/hello/<string:whatever>")
def hello(whatever=None):
    return "test routing " + (whatever if whatever != None else "")

if __name__ == "__main__":
    app.run(ssl_context='adhoc')
