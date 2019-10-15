from flask import Flask, render_template, request

import numpy as np
import pandas as pd
from bokeh.embed import components
from bokeh.layouts import column, row
from bokeh.models.widgets import Select
from bokeh.models import ColumnDataSource, CustomJS

from data_functions import season_chart


# local testing
filename = "data/football_data.parquet"

# python anywhere local file
# filename = "/home/itsbillw/thatsmoreofit/data/football_data.parquet"

df = pd.read_parquet(filename)
leagues = df["League"].unique().tolist()
seasons = df["Season"].unique().tolist()

current_league = leagues[0]
current_season = seasons[-1]

season_data = df[(df["Season"] == current_season) &
                 (df["League"] == current_league)]

teams = season_data["Team"].unique().tolist()

source = ColumnDataSource(season_data)
original_source = ColumnDataSource(df)

league_select = Select(title="Select League", options=leagues, value="Premier League")
season_select = Select(title="Select Season", options=seasons, value="2019-20")

combined_callback_code = """
var data = source.data;
var original_data = original_source.data;
var league = league_select_obj.value;
var season = season_select_obj.value;
for (var key in original_data) {
    data[key] = [];
    for (var i = 0; i < original_data['League'].length; ++i) {
        if (original_data['League'][i] === league &&
            original_data['Season'][i] === season) {
            data[key].push(original_data[key][i]);
        }
    }
}
source.change.emit();
"""

generic_callback = CustomJS(
    args=dict(source=source,
              original_source=original_source,
              league_select_obj=league_select,
              season_select_obj=season_select),
    code=combined_callback_code
)

league_select.callback = generic_callback
season_select.callback = generic_callback

selected_league = league_select.value
selected_season = season_select.value

inputs = row(league_select, season_select)

teams = df[(df["League"] == selected_league)&(df["Season"] == selected_season)]["Team"].unique().tolist()

plot = season_chart(source, selected_league, selected_season, teams)

script_chart, div_chart = components(column(inputs, plot))


app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/data')
def data():

    return render_template('data.html',
                           script_chart=script_chart,
                           div_chart=div_chart)


# With debug=True, Flask server will auto-reload
# when there are code changes
if __name__ == '__main__':
    app.run(port=5000, debug=True)
