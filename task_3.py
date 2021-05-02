# Libraries imports
import pandas as pd
import numpy as np

##########################################################
#                   Auxilliary functions                 #
##########################################################

def get_hour(data):
    return data['time'].apply(lambda x : x.split(':')[0])

def task_3_transform(x):
    names = {
        'unique_users': pd.Series.nunique(x['user_id']),
        'peak_hour': x['hour'].value_counts().index[0]
    }
    names['peak_hour_unique_users'] = pd.Series.nunique(x[x['hour'] == names['peak_hour']]['user_id'])

    return pd.Series(names, index=['unique_users', 'peak_hour', 'peak_hour_unique_users'])


##########################################################
#                   Main task function                   #
##########################################################

def execute_task_3(data):
    
    # 1. Set time to hour-only format
    data['hour'] = get_hour(data)

    # 2. Perform transformations
    return data.groupby(['genre']) \
        .apply(task_3_transform) \
        .sort_values(by='unique_users', ascending=False).head(10)


if __name__ == '__main__':

    # Load input data
    started_streams = pd.read_csv('started_streams.csv', sep=';')
    
    # Execute task
    task_3_result = execute_task_3(started_streams)

    # Save output to csv file
    task_3_result.to_csv('results/task_3_results.csv')