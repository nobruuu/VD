import pandas as pd

archivo_csv = 'GoalsandAssists.csv'
data = pd.read_csv(archivo_csv)

ligas_anadir = {
    'Bundesliga': 'Alemania',
    'Ligue 1': 'Francia',
    '3. Liga': 'Alemania',
    '2. Bundesliga': 'Alemania',
    'Regionalliga Südwest': 'Alemania',
    'Serie A': 'Italia',
    'Ligue 2': 'Francia',
    'LaLiga': 'España',
    'Championnat National': 'Francia',
    'NOFV-Oberliga Nord': 'Alemania',
    'LaLiga2': 'España',
    'France': 'Francia',
    'Serie C - A': 'Italia',
    'Oberliga Niederrhein': 'Alemania',
    'Serie C - B': 'Italia',
    'National 3 - Grp. C': 'Francia',
    'Serie B': 'Alemania',
    'National 2 - Grp. A': 'Francia',
    'National 2 - Grp. C': 'Francia',
    'Oberliga Westfalen': 'Alemania',
    'Serie C - C': 'Italia',
    'Spain': 'España',
    'Premier League': 'Inglaterra',
    'Primera Federación - Gr. I': 'España',
    'Championship': 'Inglaterra',
    'League Two': 'Inglaterra',
    'Segunda Federación - Gr. I': 'España',
    'League One': 'Inglaterra',
    'Serie D - B': 'Italia',
    'Liga Portugal': 'Portugal',
    'Primera Federación - Gr. II': 'España',
    'Regionalliga Nordost': 'Alemania',
    'Liga Sabseg': 'Portugal',
    'Italy': 'Italia',
    'Portugal': 'Portugal',
    'Liga 3': 'España',
    'Serie D - E': 'Italia',
    'Serie D - I': 'Italia',
}

data['League Country'] = data['League Name'].map(ligas_anadir)
player_goals = data.groupby('Name')['Goals'].sum().reset_index()
player_goals_sorted = player_goals.sort_values(by='Goals', ascending=False)
top_scorers = player_goals_sorted.head(150)
top_scorers_info = data[data['Name'].isin(top_scorers['Name'])]
top_scorers_info = top_scorers_info[['Name', 'Club Name', 'League Name', 'League Country']]
top_scorers_info = top_scorers_info.drop_duplicates(subset='Name')
country_counts = top_scorers_info['League Country'].value_counts()
print(country_counts)