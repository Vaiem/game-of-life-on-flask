from flask import Flask
from flask import render_template, redirect, url_for
from model import Game
import random
import time

app = Flask(__name__)
#app.config["game"] = Game(3, 3)
#app.debug = True
#
#

@app.route("/")
def ferst():    
    a = Game(15,15)
    return render_template("index.html" )

@app.route("/game", endpoint='game')
def game():
    mapG = Game().gameMap.tolist()
    return render_template("game.html", gameMap= mapG, count= Game().countGen)

@app.route("/nextGen")
def nextGen():
    Game().gen_next()
    return redirect(url_for('game'))

if __name__ == "__main__":
    app.run(host= "127.0.0.1", port = 8080)