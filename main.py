from flask import Flask
from flask import render_template, redirect, url_for, request
from model import Game, SizeForm


import random
import time

app = Flask(__name__)
app.secret_key = 'you_need_a_secret_key'

#app.config["game"] = Game(3, 3)
#app.debug = True
#
#

@app.route("/", methods = ['get', 'post'])
def ferst():
    form = SizeForm()
    state = 0
    if form.validate_on_submit():
        a = Game()
        a.x = form.weight.data
        a.y = form.height.data
        a.countGen = 0
        a.gen_start_map()
        state = 1
        
       
    return render_template("index.html", form= form, state = state )

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