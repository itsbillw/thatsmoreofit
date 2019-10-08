import itertools

import pandas as pd

from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.palettes import Category20
from bokeh.models import Legend


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


def season_chart(df, colors, league):

    p = figure(x_axis_type="datetime", plot_height=550,
               plot_width=1100, toolbar_location='right')

    p.title.text = league
    p.xaxis.axis_label = 'Match Date'
    p.yaxis.axis_label = 'Points'

    legend_it = []

    teams = df.sort_values(["Points"], ascending=False)[
        "Team"].unique().tolist()

    if league == "Premier League":
        for team in teams:
            source = ColumnDataSource(df[df['Team'] == team])
            l = p.line('Date', 'Points', source=source, color=colors[team])
            c = p.circle('Date', 'Points', source=source, color=colors[team])
            legend_it.append((team, [c, l]))
    else:
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