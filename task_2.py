# Libraries imports
import pandas as pd
import numpy as np


##########################################################
#                   Main task function                   #
##########################################################

def execute_task_2(data):

    # 1. Perform transformations
    return data.groupby(['program_title']) \
        .agg(unique_users=('user_id', pd.Series.nunique), \
            content_count=('user_id', 'count'), \
            device_name=('device_name', lambda x: x.value_counts().index[0]), \
            country_code=('country_code', lambda x: x.value_counts().index[0]), \
            product_type=('product_type', lambda x: x.value_counts().index[0])) \
        .sort_values(by='unique_users', ascending=False)


if __name__ == '__main__':

    # Load input data
    started_streams = pd.read_csv('started_streams.csv', sep=';')
    
    # Execute task
    task_2_result = execute_task_2(started_streams)

    # Save output to csv file
    task_2_result.to_csv('results/task_2_results.csv')