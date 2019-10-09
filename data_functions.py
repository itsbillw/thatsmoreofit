import itertools

import pandas as pd

from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.palettes import Category20
from bokeh.models import Legend


# local testing
filename = "static/data/football_data.csv"

# python anywhere local file
# filename = "/home/billw/mysite/static/data/football_data.csv"


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


def rebuild_data():

    df = pd.DataFrame()
    for season in multi_season_leagues:
        for league in multi_season_leagues[season]:
            season_data = parse_season_data(
                multi_season_leagues[season][league])
            season_data["Season"] = season
            season_data["League"] = league
            df = df.append(season_data)
    df.to_csv(filename, index=False)


def parse_season_data(filename):

    columns = ['Div', 'Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR']
    source_df = pd.read_csv(filename, usecols=columns,
                            parse_dates=["Date"], dayfirst=True)

    results = pd.DataFrame()

    teams = source_df["HomeTeam"].sort_values().unique().tolist()

    for team in teams:
        df = source_df[(source_df['HomeTeam'] == team) |
                       (source_df['AwayTeam'] == team)].copy()

        df["Team"] = df.apply(lambda x: team, axis=1)
        df["Opposition"] = df.apply(
            lambda x: x["AwayTeam"] if x["HomeTeam"] == team else x["HomeTeam"], axis=1)
        df['HomeAway'] = df.apply(
            lambda x: "H" if x["HomeTeam"] == team else "A", axis=1)

        df["Result"] = df.apply(lambda x: "W" if (x["FTR"] == "H" and x["HomeTeam"] == team) or
                                (x["FTR"] == "A" and x["AwayTeam"] == team) else
                                ("L" if (x["FTR"] == "A" and x["HomeTeam"] == team) or
                                 (x["FTR"] == "H" and x["AwayTeam"] == team) else "D"), axis=1)
        df["MatchPoints"] = df.apply(lambda x: 3 if x["Result"] == "W" else (
            1 if x["Result"] == "D" else 0), axis=1)
        df["Points"] = df["MatchPoints"].cumsum()

        df["GF"] = df.apply(lambda x: x["FTHG"] if x["HomeTeam"]
                            == team else x["FTAG"], axis=1)
        df["GA"] = df.apply(lambda x: x["FTAG"] if x["HomeTeam"]
                            == team else x["FTHG"], axis=1)
        df["GD"] = df.apply(lambda x: x["GF"] - x["GA"], axis=1)

        df["W"] = df.apply(lambda x: 1 if x["Result"] == "W" else 0, axis=1)
        df["D"] = df.apply(lambda x: 1 if x["Result"] == "D" else 0, axis=1)
        df["L"] = df.apply(lambda x: 1 if x["Result"] == "L" else 0, axis=1)

        df = df.reset_index(drop=True).reset_index()
        df['index'] = df['index'].add(1)
        df = df.rename(columns={"index": "Played"})

        results = results.append(df)

    results = results.reset_index(drop=True)

    return results


def season_chart(df, league, season):

    p = figure(x_axis_type="datetime", plot_height=550,
               plot_width=1100, toolbar_location='right')

    p.title.text = league + " " + season
    p.xaxis.axis_label = 'Match Date'
    p.yaxis.axis_label = 'Points'

    legend_it = []

    teams = df.sort_values(["Points"], ascending=False)[
        "Team"].unique().tolist()

    if league == "Premier League":
        colors = pl_colors
        for team in teams:
            source = ColumnDataSource(df[df['Team'] == team])
            l = p.line('Date', 'Points', source=source, color=colors[team])
            c = p.circle('Date', 'Points', source=source, color=colors[team])
            legend_it.append((team, [c, l]))
    else:
        colors = itertools.cycle(Category20[20])
        for team, color in zip(teams, colors):
            source = ColumnDataSource(df[df['Team'] == team])
            l = p.line('Date', 'Points', source=source, color=color)
            c = p.circle('Date', 'Points', source=source, color=color)
            legend_it.append((team, [c, l]))

    hover = HoverTool(
        tooltips=[
            ('Team', '@Team'),
            ('Opposition', '@Opposition (@HomeAway)'),
            ('Date', '@Date{%F}'),
            ('Result', '@FTHG - @FTAG (@Result)'),
            ('Points', '@Points'),
            ('Match', '@Played of 38')
        ],
        formatters={'Date': 'datetime'}
    )

    p.add_tools(hover)

    legend = Legend(items=legend_it)
    legend.click_policy = "hide"
    p.add_layout(legend, 'left')

    return p
