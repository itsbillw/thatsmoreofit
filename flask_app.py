from flask import Flask, render_template, request

import atexit
import itertools
import pandas as pd
from bokeh.embed import components
from bokeh.palettes import Category20
from apscheduler.schedulers.background import BackgroundScheduler

from data_functions import rebuild_data, parse_season_data, season_chart


# local testing
filename = "static/data/football_data.csv"

# python anywhere local file
# filename = "/home/billw/mysite/static/data/football_data.csv"

df = pd.read_csv(filename, parse_dates=["Date"])
leagues = df["League"].unique().tolist()
seasons = df["Season"].unique().tolist()


scheduler = BackgroundScheduler()
scheduler.add_job(func=rebuild_data, trigger="interval", seconds=300)
scheduler.start()


app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/data', methods=['GET', 'POST'])
def data():

    current_season = request.form.get("season")
    if current_season == None:
        current_season = "2019-20"

    current_league = request.form.get("league")
    if current_league == None:
        current_league = "Premier League"

    season_data = df[(df["Season"] == current_season) &
                     (df["League"] == current_league)]

    if current_league == "Premier League":
        plot = season_chart(season_data, current_league, current_season)
    else:
        plot = season_chart(season_data, current_league, current_season)

    script_chart, div_chart = components(plot)

    return render_template('data.html',
                           script_chart=script_chart,
                           div_chart=div_chart,
                           leagues=leagues,
                           current_league=current_league,
                           seasons=seasons,
                           current_seasons=current_season)


atexit.register(lambda: scheduler.shutdown())

# With debug=True, Flask server will auto-reload
# when there are code changes
if __name__ == '__main__':
    app.run(port=5000, debug=True)
