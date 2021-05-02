# Libraries imports
import pandas as pd
import numpy as np



##########################################################
#                   Auxilliary functions                 #
##########################################################

def fix_missing_ids(data):
    data.loc[data['profile_id'] == '', 'profile_id'] = pd.NA # Replace empty strings with NA because empty strings are not interpreted as NA values
    data['profile_id'].fillna(data['user_id'], inplace=True)

def filter_sports(data, sports):
    return data[data['sub_genre3'].isin(sports)]

def get_favs(x, category):
    favs = []
    for fav in x[category].unique():
        favs.append({
            'name': fav,
            'viewed_milli_seconds': x[x[category] == fav]['viewed_milli_seconds'].sum()
        })
    favs.sort(key=lambda fav: fav['viewed_milli_seconds'], reverse=True)
    return favs

def get_fav_teams(x):
    fav_teams = {}
    for i in np.arange(len(x)):
        teams = x['product_title'].iloc[i].split(' - ')
        for team in teams:
            if team in fav_teams:
                fav_teams[team]['viewed_milli_seconds'] += x['viewed_milli_seconds'].iloc[i]
            else:
                fav_teams[team] = {'name': team, 'sport': x['sub_genre3'].iloc[i], 'league': x['series_guid'].iloc[i], 'viewed_milli_seconds': x['viewed_milli_seconds'].iloc[i]}

    fav_teams = list(fav_teams.values())
    fav_teams.sort(key=lambda team: team['viewed_milli_seconds'], reverse=True)
    return fav_teams

def task_1_transform(x):
    names = {
        'fav_sports': get_favs(x, 'sub_genre3'),
        'fav_leagues': get_favs(x, 'series_guid'),
        'fav_teams': get_fav_teams(x)
    }
    return pd.Series(names, index=names.keys())


##########################################################
#                   Main task function                   #
##########################################################

def execute_task_1(viewing_data):

    # 1. Use user_id is profile_id is missing
    fix_missing_ids(viewing_data)

    # 2. Get only data from the following sports: ['american football', 'soccer', 'basketball', 'handball', 'ice hockey']
    selected_sports = ['american football', 'soccer', 'basketball', 'handball', 'ice hockey']
    sports_data = filter_sports(viewing_data, selected_sports)

    # 3. Get favorite sports, leagues and teams per profile_id by calling a transformation function defined and explained above
    return sports_data.groupby(['profile_id']).apply(task_1_transform)



if __name__ == '__main__':
    # Load Input data
    viewing_data = pd.read_parquet('ViewingData.snappy.parquet')

    # Execute task
    task_1_result = execute_task_1(viewing_data)

    # Save output to csv file
    task_1_result.to_csv('results/task_1_results.csv')