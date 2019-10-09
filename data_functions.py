import itertools

from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.palettes import Category20
from bokeh.models import Legend


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


def season_chart(df, league, season):

    p = figure(x_axis_type="datetime", plot_height=550,
               plot_width=1100, toolbar_location='above')

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

    p.toolbar.active_drag = None

    legend = Legend(items=legend_it)
    legend.click_policy = "hide"
    p.add_layout(legend, 'left')

    return p
