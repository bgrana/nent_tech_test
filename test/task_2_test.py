import numpy as np
import pandas as pd
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import task_2

cols = ['dt', 'time', 'device_name', 'house_number', 'user_id', 'country_code', 'program_title', 'season', 'season_episode', 'genre', 'product_type']

def test_unique_users():
    df = pd.DataFrame([['0', '10:00:00', 'dev1', 1234, '1', 'DE', 'program1', 'S1', 'E1', 'horror', 'svod'], \
        ['0', '10:00:00', 'dev1', 1234, '1', 'DE', 'program1', 'S1', 'E1', 'horror', 'svod'], \
        ['0', '10:00:00', 'dev1', 1234, '2', 'SE', 'program1', 'S1', 'E1', 'horror', 'svod']], columns=cols)
    res = task_2.execute_task_2(df)

    # Number of users should be 2 as 2 users watched 'program1'
    assert res['unique_users'][0] == 2

def test_content_count():
    df = pd.DataFrame([['0', '10:00:00', 'dev1', 1234, '1', 'DE', 'program1', 'S1', 'E1', 'horror', 'svod'], \
        ['0', '10:00:00', 'dev1', 1234, '1', 'DE', 'program1', 'S1', 'E1', 'horror', 'svod'], \
        ['0', '10:00:00', 'dev1', 1234, '2', 'SE', 'program1', 'S1', 'E1', 'horror', 'svod']], columns=cols)
    res = task_2.execute_task_2(df)

    # Content count should be 3 as there are 3 visualizations of 'program1'
    assert res['content_count'][0] == 3

def test_country_code():
    df = pd.DataFrame([['0', '10:00:00', 'dev1', 1234, '1', 'DE', 'program1', 'S1', 'E1', 'horror', 'svod'], \
        ['0', '10:00:00', 'dev1', 1234, '1', 'DE', 'program1', 'S1', 'E1', 'horror', 'svod'], \
        ['0', '10:00:00', 'dev1', 1234, '2', 'SE', 'program1', 'S1', 'E1', 'horror', 'svod']], columns=cols)
    res = task_2.execute_task_2(df)

    # Country code should be 'DE' as it is the most repeated one among viewers of 'program1'
    assert res['country_code'][0] == 'DE'

def test_device_name():
    df = pd.DataFrame([['0', '10:00:00', 'dev1', 1234, '1', 'DE', 'program1', 'S1', 'E1', 'horror', 'svod'], \
        ['0', '10:00:00', 'dev2', 1234, '1', 'DE', 'program1', 'S1', 'E1', 'horror', 'svod'], \
        ['0', '10:00:00', 'dev1', 1234, '2', 'SE', 'program1', 'S1', 'E1', 'horror', 'svod']], columns=cols)
    res = task_2.execute_task_2(df)

    # Device name should be 'dev1' as it is the most repeated one among viewers of 'program1'
    assert res['device_name'][0] == 'dev1'

def test_product_type():
    df = pd.DataFrame([['0', '10:00:00', 'dev1', 1234, '1', 'DE', 'program1', 'S1', 'E1', 'horror', 'svod'], \
        ['0', '10:00:00', 'dev2', 1234, '1', 'DE', 'program1', 'S1', 'E1', 'horror', 'tvod'], \
        ['0', '10:00:00', 'dev1', 1234, '2', 'SE', 'program1', 'S1', 'E1', 'horror', 'svod']], columns=cols)
    res = task_2.execute_task_2(df)

    # Product type should be 'svod' as it is the most repeated one among viewers of 'program1'
    assert res['product_type'][0] == 'svod'

def test_content_ordered_by_unique_users():
    df = pd.DataFrame([['0', '10:00:00', 'dev1', 1234, '1', 'DE', 'program1', 'S1', 'E1', 'horror', 'svod'], \
        ['0', '10:00:00', 'dev2', 1234, '1', 'DE', 'program2', 'S1', 'E1', 'horror', 'svod'], \
        ['0', '10:00:00', 'dev1', 1234, '2', 'SE', 'program2', 'S1', 'E1', 'horror', 'svod']], columns=cols)
    res = task_2.execute_task_2(df)

    # 'program2' should be the most viewed and 'program1' the second most viewed
    assert res.index[0] == 'program2'
    assert res.index[1] == 'program1'

if __name__ == "__main__":
    
    # Tests
    test_unique_users()
    test_content_count()
    test_country_code()
    test_device_name()
    test_product_type()
    test_content_ordered_by_unique_users()
    
    # Print this if everything worked
    print("All Tests Passed")
