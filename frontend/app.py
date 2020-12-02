from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def main():
    if request.method == 'GET':
        return render_template('home.html')

@app.route("/api", methods = ['POST'])
def api():
    li = []
    info = dict()
    info["puuid"] = "7uly"
    info["skin_id"]  = "galaxy"
    info["last_round"] = "3"
    info["placement"] = "4"
    info["time_eliminated"] = "23:23"
    info["gold_left"] = "2000"
    li.append(info)
    if request.method == 'POST':
        result = request.form
        print(dict(result))
        return render_template("record.html", result = li)


if __name__ == "__main__":
    app.run()
