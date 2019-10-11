import pandas as pd


# local testing
filename = "data/football_data.parquet"

# python anywhere local file
# filename = "/home/itsbillw/thatsmoreofit/data/football_data.parquet"

multi_season_leagues = {
    "1993-94": {
        "Premier League": "http://www.football-data.co.uk/mmz4281/9394/E0.csv",
        "La Liga": "http://www.football-data.co.uk/mmz4281/9394/SP1.csv",
        "Serie A": "http://www.football-data.co.uk/mmz4281/9394/I1.csv",
        "Bundesliga": "http://www.football-data.co.uk/mmz4281/9394/D1.csv",
        "Ligue 1": "http://www.football-data.co.uk/mmz4281/9394/F1.csv",
        "Eredivisie": "http://www.football-data.co.uk/mmz4281/9394/N1.csv"
    },
    "1994-95": {
        "Premier League": "http://www.football-data.co.uk/mmz4281/9495/E0.csv",
        "La Liga": "http://www.football-data.co.uk/mmz4281/9495/SP1.csv",
        "Serie A": "http://www.football-data.co.uk/mmz4281/9495/I1.csv",
        "Bundesliga": "http://www.football-data.co.uk/mmz4281/9495/D1.csv",
        "Ligue 1": "http://www.football-data.co.uk/mmz4281/9495/F1.csv",
        "Eredivisie": "http://www.football-data.co.uk/mmz4281/9495/N1.csv"
    },
    "1995-96": {
        "Premier League": "http://www.football-data.co.uk/mmz4281/9596/E0.csv",
        "La Liga": "http://www.football-data.co.uk/mmz4281/9596/SP1.csv",
        "Serie A": "http://www.football-data.co.uk/mmz4281/9596/I1.csv",
        "Bundesliga": "http://www.football-data.co.uk/mmz4281/9596/D1.csv",
        "Ligue 1": "http://www.football-data.co.uk/mmz4281/9596/F1.csv",
        "Eredivisie": "http://www.football-data.co.uk/mmz4281/9596/N1.csv"
    },
    "1996-97": {
        "Premier League": "http://www.football-data.co.uk/mmz4281/9697/E0.csv",
        "La Liga": "http://www.football-data.co.uk/mmz4281/9697/SP1.csv",
        "Serie A": "http://www.football-data.co.uk/mmz4281/9697/I1.csv",
        "Bundesliga": "http://www.football-data.co.uk/mmz4281/9697/D1.csv",
        "Ligue 1": "http://www.football-data.co.uk/mmz4281/9697/F1.csv",
        "Eredivisie": "http://www.football-data.co.uk/mmz4281/9697/N1.csv"
    },
    "1997-98": {
        "Premier League": "http://www.football-data.co.uk/mmz4281/9798/E0.csv",
        "La Liga": "http://www.football-data.co.uk/mmz4281/9798/SP1.csv",
        "Serie A": "http://www.football-data.co.uk/mmz4281/9798/I1.csv",
        "Bundesliga": "http://www.football-data.co.uk/mmz4281/9798/D1.csv",
        "Ligue 1": "http://www.football-data.co.uk/mmz4281/9798/F1.csv",
        "Eredivisie": "http://www.football-data.co.uk/mmz4281/9798/N1.csv"
    },
    "1998-99": {
        "Premier League": "http://www.football-data.co.uk/mmz4281/9899/E0.csv",
        "La Liga": "http://www.football-data.co.uk/mmz4281/9899/SP1.csv",
        "Serie A": "http://www.football-data.co.uk/mmz4281/9899/I1.csv",
        "Bundesliga": "http://www.football-data.co.uk/mmz4281/9899/D1.csv",
        "Ligue 1": "http://www.football-data.co.uk/mmz4281/9899/F1.csv",
        "Eredivisie": "http://www.football-data.co.uk/mmz4281/9899/N1.csv"
    },
    "1999-00": {
        "Premier League": "http://www.football-data.co.uk/mmz4281/9900/E0.csv",
        "La Liga": "http://www.football-data.co.uk/mmz4281/9900/SP1.csv",
        "Serie A": "http://www.football-data.co.uk/mmz4281/9900/I1.csv",
        "Bundesliga": "http://www.football-data.co.uk/mmz4281/9900/D1.csv",
        "Ligue 1": "http://www.football-data.co.uk/mmz4281/9900/F1.csv",
        "Eredivisie": "http://www.football-data.co.uk/mmz4281/9900/N1.csv"
    },
    "2000-01": {
        "Premier League": "http://www.football-data.co.uk/mmz4281/0001/E0.csv",
        "La Liga": "http://www.football-data.co.uk/mmz4281/0001/SP1.csv",
        "Serie A": "http://www.football-data.co.uk/mmz4281/0001/I1.csv",
        "Bundesliga": "http://www.football-data.co.uk/mmz4281/0001/D1.csv",
        "Ligue 1": "http://www.football-data.co.uk/mmz4281/0001/F1.csv",
        "Eredivisie": "http://www.football-data.co.uk/mmz4281/0001/N1.csv"
    },
    "2001-02": {
        "Premier League": "http://www.football-data.co.uk/mmz4281/0102/E0.csv",
        "La Liga": "http://www.football-data.co.uk/mmz4281/0102/SP1.csv",
        "Serie A": "http://www.football-data.co.uk/mmz4281/0102/I1.csv",
        "Bundesliga": "http://www.football-data.co.uk/mmz4281/0102/D1.csv",
        "Ligue 1": "http://www.football-data.co.uk/mmz4281/0102/F1.csv",
        "Eredivisie": "http://www.football-data.co.uk/mmz4281/0102/N1.csv"
    },
    "2002-03": {
        "Premier League": "http://www.football-data.co.uk/mmz4281/0203/E0.csv",
        "La Liga": "http://www.football-data.co.uk/mmz4281/0203/SP1.csv",
        "Serie A": "http://www.football-data.co.uk/mmz4281/0203/I1.csv",
        "Bundesliga": "http://www.football-data.co.uk/mmz4281/0203/D1.csv",
        "Ligue 1": "http://www.football-data.co.uk/mmz4281/0203/F1.csv",
        "Eredivisie": "http://www.football-data.co.uk/mmz4281/0203/N1.csv"
    },
    "2003-04": {
        "Premier League": "http://www.football-data.co.uk/mmz4281/0304/E0.csv",
        "La Liga": "http://www.football-data.co.uk/mmz4281/0304/SP1.csv",
        "Serie A": "http://www.football-data.co.uk/mmz4281/0304/I1.csv",
        "Bundesliga": "http://www.football-data.co.uk/mmz4281/0304/D1.csv",
        "Ligue 1": "http://www.football-data.co.uk/mmz4281/0304/F1.csv",
        "Eredivisie": "http://www.football-data.co.uk/mmz4281/0304/N1.csv"
    },
    "2004-05": {
        "Premier League": "http://www.football-data.co.uk/mmz4281/0405/E0.csv",
        "La Liga": "http://www.football-data.co.uk/mmz4281/0405/SP1.csv",
        "Serie A": "http://www.football-data.co.uk/mmz4281/0405/I1.csv",
        "Bundesliga": "http://www.football-data.co.uk/mmz4281/0405/D1.csv",
        "Ligue 1": "http://www.football-data.co.uk/mmz4281/0405/F1.csv",
        "Eredivisie": "http://www.football-data.co.uk/mmz4281/0405/N1.csv"
    },
    "2005-06": {
        "Premier League": "http://www.football-data.co.uk/mmz4281/0506/E0.csv",
        "La Liga": "http://www.football-data.co.uk/mmz4281/0506/SP1.csv",
        "Serie A": "http://www.football-data.co.uk/mmz4281/0506/I1.csv",
        "Bundesliga": "http://www.football-data.co.uk/mmz4281/0506/D1.csv",
        "Ligue 1": "http://www.football-data.co.uk/mmz4281/0506/F1.csv",
        "Eredivisie": "http://www.football-data.co.uk/mmz4281/0506/N1.csv"
    },
    "2006-07": {
        "Premier League": "http://www.football-data.co.uk/mmz4281/0607/E0.csv",
        "La Liga": "http://www.football-data.co.uk/mmz4281/0607/SP1.csv",
        "Serie A": "http://www.football-data.co.uk/mmz4281/0607/I1.csv",
        "Bundesliga": "http://www.football-data.co.uk/mmz4281/0607/D1.csv",
        "Ligue 1": "http://www.football-data.co.uk/mmz4281/0607/F1.csv",
        "Eredivisie": "http://www.football-data.co.uk/mmz4281/0607/N1.csv"
    },
    "2007-08": {
        "Premier League": "http://www.football-data.co.uk/mmz4281/0708/E0.csv",
        "La Liga": "http://www.football-data.co.uk/mmz4281/0708/SP1.csv",
        "Serie A": "http://www.football-data.co.uk/mmz4281/0708/I1.csv",
        "Bundesliga": "http://www.football-data.co.uk/mmz4281/0708/D1.csv",
        "Ligue 1": "http://www.football-data.co.uk/mmz4281/0708/F1.csv",
        "Eredivisie": "http://www.football-data.co.uk/mmz4281/0708/N1.csv"
    },
    "2008-09": {
        "Premier League": "http://www.football-data.co.uk/mmz4281/0809/E0.csv",
        "La Liga": "http://www.football-data.co.uk/mmz4281/0809/SP1.csv",
        "Serie A": "http://www.football-data.co.uk/mmz4281/0809/I1.csv",
        "Bundesliga": "http://www.football-data.co.uk/mmz4281/0809/D1.csv",
        "Ligue 1": "http://www.football-data.co.uk/mmz4281/0809/F1.csv",
        "Eredivisie": "http://www.football-data.co.uk/mmz4281/0809/N1.csv"
    },
    "2009-10": {
        "Premier League": "http://www.football-data.co.uk/mmz4281/0910/E0.csv",
        "La Liga": "http://www.football-data.co.uk/mmz4281/0910/SP1.csv",
        "Serie A": "http://www.football-data.co.uk/mmz4281/0910/I1.csv",
        "Bundesliga": "http://www.football-data.co.uk/mmz4281/0910/D1.csv",
        "Ligue 1": "http://www.football-data.co.uk/mmz4281/0910/F1.csv",
        "Eredivisie": "http://www.football-data.co.uk/mmz4281/0910/N1.csv"
    },
    "2010-11": {
        "Premier League": "http://www.football-data.co.uk/mmz4281/1011/E0.csv",
        "La Liga": "http://www.football-data.co.uk/mmz4281/1011/SP1.csv",
        "Serie A": "http://www.football-data.co.uk/mmz4281/1011/I1.csv",
        "Bundesliga": "http://www.football-data.co.uk/mmz4281/1011/D1.csv",
        "Ligue 1": "http://www.football-data.co.uk/mmz4281/1011/F1.csv",
        "Eredivisie": "http://www.football-data.co.uk/mmz4281/1011/N1.csv"
    },
    "2011-12": {
        "Premier League": "http://www.football-data.co.uk/mmz4281/1112/E0.csv",
        "La Liga": "http://www.football-data.co.uk/mmz4281/1112/SP1.csv",
        "Serie A": "http://www.football-data.co.uk/mmz4281/1112/I1.csv",
        "Bundesliga": "http://www.football-data.co.uk/mmz4281/1112/D1.csv",
        "Ligue 1": "http://www.football-data.co.uk/mmz4281/1112/F1.csv",
        "Eredivisie": "http://www.football-data.co.uk/mmz4281/1112/N1.csv"
    },
    "2012-13": {
        "Premier League": "http://www.football-data.co.uk/mmz4281/1213/E0.csv",
        "La Liga": "http://www.football-data.co.uk/mmz4281/1213/SP1.csv",
        "Serie A": "http://www.football-data.co.uk/mmz4281/1213/I1.csv",
        "Bundesliga": "http://www.football-data.co.uk/mmz4281/1213/D1.csv",
        "Ligue 1": "http://www.football-data.co.uk/mmz4281/1213/F1.csv",
        "Eredivisie": "http://www.football-data.co.uk/mmz4281/1213/N1.csv"
    },
    "2013-14": {
        "Premier League": "http://www.football-data.co.uk/mmz4281/1314/E0.csv",
        "La Liga": "http://www.football-data.co.uk/mmz4281/1314/SP1.csv",
        "Serie A": "http://www.football-data.co.uk/mmz4281/1314/I1.csv",
        "Bundesliga": "http://www.football-data.co.uk/mmz4281/1314/D1.csv",
        "Ligue 1": "http://www.football-data.co.uk/mmz4281/1314/F1.csv",
        "Eredivisie": "http://www.football-data.co.uk/mmz4281/1314/N1.csv"
    },
    "2014-15": {
        "Premier League": "http://www.football-data.co.uk/mmz4281/1415/E0.csv",
        "La Liga": "http://www.football-data.co.uk/mmz4281/1415/SP1.csv",
        "Serie A": "http://www.football-data.co.uk/mmz4281/1415/I1.csv",
        "Bundesliga": "http://www.football-data.co.uk/mmz4281/1415/D1.csv",
        "Ligue 1": "http://www.football-data.co.uk/mmz4281/1415/F1.csv",
        "Eredivisie": "http://www.football-data.co.uk/mmz4281/1415/N1.csv"
    },
    "2015-16": {
        "Premier League": "http://www.football-data.co.uk/mmz4281/1516/E0.csv",
        "La Liga": "http://www.football-data.co.uk/mmz4281/1516/SP1.csv",
        "Serie A": "http://www.football-data.co.uk/mmz4281/1516/I1.csv",
        "Bundesliga": "http://www.football-data.co.uk/mmz4281/1516/D1.csv",
        "Ligue 1": "http://www.football-data.co.uk/mmz4281/1516/F1.csv",
        "Eredivisie": "http://www.football-data.co.uk/mmz4281/1516/N1.csv"
    },
    "2016-17": {
        "Premier League": "http://www.football-data.co.uk/mmz4281/1617/E0.csv",
        "La Liga": "http://www.football-data.co.uk/mmz4281/1617/SP1.csv",
        "Serie A": "http://www.football-data.co.uk/mmz4281/1617/I1.csv",
        "Bundesliga": "http://www.football-data.co.uk/mmz4281/1617/D1.csv",
        "Ligue 1": "http://www.football-data.co.uk/mmz4281/1617/F1.csv",
        "Eredivisie": "http://www.football-data.co.uk/mmz4281/1617/N1.csv"
    },
    "2017-18": {
        "Premier League": "http://www.football-data.co.uk/mmz4281/1718/E0.csv",
        "La Liga": "http://www.football-data.co.uk/mmz4281/1718/SP1.csv",
        "Serie A": "http://www.football-data.co.uk/mmz4281/1718/I1.csv",
        "Bundesliga": "http://www.football-data.co.uk/mmz4281/1718/D1.csv",
        "Ligue 1": "http://www.football-data.co.uk/mmz4281/1718/F1.csv",
        "Eredivisie": "http://www.football-data.co.uk/mmz4281/1718/N1.csv"
    },
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


def rebuild_current_season_data(file=filename):

    season = "2019-20"
    df = pd.read_parquet(file)
    df = df[df["Season"] != season]
    for league in multi_season_leagues[season]:
        season_data = parse_season_data(
            multi_season_leagues[season][league])
        season_data["Season"] = season
        season_data["League"] = league
        df = df.append(season_data)
    df.to_parquet(file, index=False)


def rebuild_all_season_data(file=filename):

    df = pd.DataFrame()
    for season in multi_season_leagues:
        for league in multi_season_leagues[season]:
            season_data = parse_season_data(
                multi_season_leagues[season][league])
            season_data["Season"] = season
            season_data["League"] = league
            df = df.append(season_data)
    df.to_parquet(file, index=False)


def parse_season_data(filename):

    columns = ['Div', 'Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR']
    source_df = pd.read_csv(filename, usecols=columns,
                            parse_dates=["Date"], dayfirst=True)
    source_df.dropna(how="all", inplace=True)

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


if __name__ == "__main__":
    rebuild_current_season_data()
