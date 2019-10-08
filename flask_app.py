from flask import Flask, render_template, request

import itertools

from bokeh.embed import components
from bokeh.palettes import Category20

from data_functions import parse_season_data, season_chart


multi_season_leagues = {
    "2018-19": {
        "Premier League": "http://www.football-data.co.uk/mmz4281/1819/E0.csv",
        "La Liga": "http://www.football-data.co.uk/mmz4281/1819/SP1.csv",
        "Serie A": "http://www.football-data.co.uk/mmz4281/1819/I1.csv",
        "Bundesliga": "http://www.football-data.co.uk/mmz4281/1819/D1.csv",
        "Ligue 1": "http://www.football-data.co.uk/mmz4281/1819/F1.csv",
        "Eredivisie": "http://www.football-data.co.uk/mmz4281/1819/N1.csv"
    },
    "2019-20": {
        "Premier League": "http://www.football-data.co.uk/mmz4281/1920/E0.csv",
        "La Liga": "http://www.football-data.co.uk/mmz4281/1920/SP1.csv",
        "Serie A": "http://www.football-data.co.uk/mmz4281/1920/I1.csv",
        "Bundesliga": "http://www.football-data.co.uk/mmz4281/1920/D1.csv",
        "Ligue 1": "http://www.football-data.co.uk/mmz4281/1920/F1.csv",
        "Eredivisie": "http://www.football-data.co.uk/mmz4281/1920/N1.csv"
    }
}


seasons = []
leagues = []
for season in multi_season_leagues:
    seasons.append(season)
    for league in multi_season_leagues[season]:
        if league not in leagues:
            leagues.append(league)


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
             'Watford': '#FBEE23',
             'Cardiff': '#0070B5',
             'Fulham': '#CC0000',
             'Huddersfield': '#0E63AD'}


colors = itertools.cycle(Category20[20])


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

    season_data = parse_season_data(
        multi_season_leagues[current_season][current_league])

    if current_league == "Premier League":
        plot = season_chart(season_data, pl_colors,
                            current_league, current_season)
    else:
        plot = season_chart(season_data, colors,
                            current_league, current_season)

    script_chart, div_chart = components(plot)

    return render_template('data.html',
                           script_chart=script_chart,
                           div_chart=div_chart,
                           leagues=leagues,
                           current_league=current_league,
                           seasons=seasons,
                           current_seasons=current_season)


# With debug=True, Flask server will auto-reload
# when there are code changes
if __name__ == '__main__':
    app.run(port=5000, debug=True)
