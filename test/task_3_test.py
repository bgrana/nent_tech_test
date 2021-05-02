import numpy as np
import pandas as pd
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import task_3

cols = ['dt', 'time', 'device_name', 'house_number', 'user_id', 'country_code', 'program_title', 'season', 'season_episode', 'genre', 'product_type']

def test_get_hour():
    df = pd.DataFrame([['0', '10:00:00', 'dev1', 1234, '1', 'DE', 'program1', 'S1', 'E1', 'horror', 'svod'], \
        ['0', '11:00:00', 'dev2', 1234, '1', 'DE', 'program2', 'S1', 'E1', 'horror', 'svod'], \
        ['0', '12:00:00', 'dev1', 1234, '2', 'SE', 'program2', 'S1', 'E1', 'horror', 'svod']], columns=cols)
    res = task_3.get_hour(df)

    # Hours should be 10,11,12
    assert list(res) == ['10','11','12']

def test_unique_users():
    df = pd.DataFrame([['0', '10:00:00', 'dev1', 1234, '1', 'DE', 'program1', 'S1', 'E1', 'horror', 'svod'], \
        ['0', '11:00:00', 'dev2', 1234, '1', 'DE', 'program2', 'S1', 'E1', 'horror', 'svod'], \
        ['0', '12:00:00', 'dev1', 1234, '2', 'SE', 'program2', 'S1', 'E1', 'horror', 'svod']], columns=cols)
    res = task_3.execute_task_3(df)

    # There should be 2 unique users of the genre 'horror'
    assert res['unique_users'][0] == 2

def test_peak_hour():
    df = pd.DataFrame([['0', '10:00:00', 'dev1', 1234, '1', 'DE', 'program1', 'S1', 'E1', 'horror', 'svod'], \
        ['0', '11:00:00', 'dev2', 1234, '1', 'DE', 'program2', 'S1', 'E1', 'horror', 'svod'], \
        ['0', '11:00:00', 'dev1', 1234, '2', 'SE', 'program2', 'S1', 'E1', 'horror', 'svod']], columns=cols)
    res = task_3.execute_task_3(df)

    # Peak hour should be 11 for the genre horror
    assert res['peak_hour'][0] == '11'

def test_peak_hour_unique_users():
    df = pd.DataFrame([['0', '10:00:00', 'dev1', 1234, '2', 'DE', 'program1', 'S1', 'E1', 'horror', 'svod'], \
        ['0', '11:00:00', 'dev2', 1234, '1', 'DE', 'program2', 'S1', 'E1', 'horror', 'svod'], \
        ['0', '11:00:00', 'dev1', 1234, '1', 'SE', 'program2', 'S1', 'E1', 'horror', 'svod']], columns=cols)
    res = task_3.execute_task_3(df)

    # There should be 1 unique users at peak hour (11) for genre 'horror
    assert res['peak_hour_unique_users'][0] == 1

if __name__ == "__main__":
    
    # Tests
    test_get_hour()
    test_unique_users()
    test_peak_hour()
    test_peak_hour_unique_users()
    
    # Print this if everything worked
    print("All Tests Passed")
