from flask import Flask, render_template, request

import itertools

from bokeh.embed import components
from bokeh.palettes import Category20

from data_functions import parse_season_data, season_chart

# web resource
# filename = "http://www.football-data.co.uk/mmz4281/1920/E0.csv"

# local testing
# filename = "static/data/football_data.csv"

# python anywhere local file
# filename = "/home/billw/mysite/static/data/football_data.csv"

leagues = {
    "Premier League": "http://www.football-data.co.uk/mmz4281/1920/E0.csv",
    "La Liga": "http://www.football-data.co.uk/mmz4281/1920/SP1.csv",
    "Serie A": "http://www.football-data.co.uk/mmz4281/1920/I1.csv",
    "Bundesliga": "http://www.football-data.co.uk/mmz4281/1920/D1.csv",
    "Ligue 1": "http://www.football-data.co.uk/mmz4281/1920/F1.csv",
    "Eredivisie": "http://www.football-data.co.uk/mmz4281/1920/N1.csv"
}

colors = itertools.cycle(Category20[20])

pl_colors = {'Liverpool': '#D00027',
             'Man City': '#6CABDD',
             'Arsenal': '#EF0107',
             'Chelsea': '#034694',
             'Leicester': '#003090',
             'Crystal Palace': '#1B458F',
             'West Ham': '#7A263A',
             'Burnley': '#6C1D45',
             'Bournemouth': '#DA291C',
             'Tottenham': '#132257',
             'Wolves': '#FDB913',
             'Man United': '#DA291C',
             'Sheffield United': '#EC2227',
             'Brighton': '#0057B8',
             'Newcastle': '#241F20',
             'Aston Villa': '#95BFE5',
             'Everton': '#003399',
             'Southampton': '#D71920',
             'Norwich': '#00A650',
             'Watford': '#FBEE23'}

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/data')
def data():

    current_league = request.args.get("league")
    if current_league == None:
        current_league = "Premier League"

    season_data = parse_season_data(leagues[current_league])

    if current_league == "Premier League":
        plot = season_chart(season_data, pl_colors, current_league)
    else:
        plot = season_chart(season_data, colors, current_league)

    script_chart, div_chart = components(plot)

    return render_template('data.html',
                           script_chart=script_chart,
                           div_chart=div_chart,
                           leagues=leagues,
                           current_league=current_league)


# With debug=True, Flask server will auto-reload
# when there are code changes
if __name__ == '__main__':
    app.run(port=5000, debug=True)
