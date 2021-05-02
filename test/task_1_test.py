import numpy as np
import pandas as pd
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import task_1

cols = ['user_id', 'profile_id', 'sub_genre3', 'series_guid', 'viewed_milli_seconds', 'product_title']

def test_missing_ids_empty_string():
    df = pd.DataFrame([['1', '', 'soccer', '123', 1234, 'team1 - team2']], columns=cols)
    task_1.fix_missing_ids(df)
    assert df[df['profile_id'] == 0]['profile_id'].sum() == 0

def test_missing_ids_na():
    df = pd.DataFrame([['1', pd.NA, 'soccer', '123', 1234, 'team1 - team2']], columns=cols)
    task_1.fix_missing_ids(df)
    assert df[df['profile_id'] == 0]['profile_id'].sum() == 0

def test_selected_sports():
    df = pd.DataFrame([['1', '1', 'soccer', '123', 1234, 'team1 - team2'], ['1', '1', 'basketball', '123', 1234, 'team1 - team2']], columns=cols)
    df = task_1.filter_sports(df, ['soccer'])
    assert df['sub_genre3'].unique() == 'soccer'

def test_get_fav_sports():
    df = pd.DataFrame([['1', '1', 'soccer', 'Premier League', 1, 'team1 - team2'], ['1', '1', 'soccer', 'Premier League', 1, 'team1 - team2'], ['1', '1', 'american football', 'NFL', 1, 'team3 - team4']], columns=cols)
    res = task_1.execute_task_1(df)
    
    # First should be soccer with 2 milliseconds
    assert res.loc[('1', 'fav_sports')][0]['name'] == 'soccer'
    assert res.loc[('1', 'fav_sports')][0]['viewed_milli_seconds'] == 2
    
    # Second should be american football with 1 millisecond
    assert res.loc[('1', 'fav_sports')][1]['name'] == 'american football'
    assert res.loc[('1', 'fav_sports')][1]['viewed_milli_seconds'] == 1

def test_get_fav_leagues():
    df = pd.DataFrame([['1', '1', 'soccer', 'Premier League', 1, 'team1 - team2'], ['1', '1', 'soccer', 'Premier League', 1, 'team1 - team2'], ['1', '1', 'american football', 'NFL', 1, 'team3 - team4']], columns=cols)
    res = task_1.execute_task_1(df)
    
    # First should be Premier League with 2 milliseconds
    assert res.loc[('1', 'fav_leagues')][0]['name'] == 'Premier League'
    assert res.loc[('1', 'fav_leagues')][0]['viewed_milli_seconds'] == 2
    
    # Second should be NFL with 1 millisecond
    assert res.loc[('1', 'fav_leagues')][1]['name'] == 'NFL'
    assert res.loc[('1', 'fav_leagues')][1]['viewed_milli_seconds'] == 1

def test_get_fav_teams():
    df = pd.DataFrame([['1', '1', 'soccer', 'Premier League', 1, 'team1 - team2'], ['1', '1', 'soccer', 'Premier League', 1, 'team1 - team3'], ['1', '1', 'american football', 'NFL', 1, 'team4 - team5']], columns=cols)
    res = task_1.execute_task_1(df)
    
    # There should be 5 different teams and first should be team1 with 2 milliseconds
    assert len(res.loc[('1', 'fav_teams')]) == 5
    assert res.loc[('1', 'fav_teams')][0]['name'] == 'team1'
    assert res.loc[('1', 'fav_teams')][0]['sport'] == 'soccer'
    assert res.loc[('1', 'fav_teams')][0]['league'] == 'Premier League'
    assert res.loc[('1', 'fav_teams')][0]['viewed_milli_seconds'] == 2

def test_fav_sports_leagues_teams_multiple_users():
    df = pd.DataFrame([['1', '1', 'soccer', 'Premier League', 1, 'team1 - team2'], ['1', '1', 'soccer', 'Premier League', 1, 'team1 - team3'], \
        ['1', '1', 'american football', 'NFL', 1, 'team4 - team5'], ['2', '2', 'ice hockey', 'NHL', 1, 'team6 - team7'], \
        ['1', '2', 'ice hockey', 'NHL', 1, 'team6 - team8']], columns=cols)
    res = task_1.execute_task_1(df)
    
    # User profile '1' should have the same results as in previous tests
    assert res.loc[('1', 'fav_sports')][0]['name'] == 'soccer'
    assert res.loc[('1', 'fav_sports')][0]['viewed_milli_seconds'] == 2
    assert res.loc[('1', 'fav_leagues')][0]['name'] == 'Premier League'
    assert res.loc[('1', 'fav_leagues')][0]['viewed_milli_seconds'] == 2
    assert len(res.loc[('1', 'fav_teams')]) == 5
    assert res.loc[('1', 'fav_teams')][0]['name'] == 'team1'
    assert res.loc[('1', 'fav_teams')][0]['sport'] == 'soccer'
    assert res.loc[('1', 'fav_teams')][0]['league'] == 'Premier League'
    assert res.loc[('1', 'fav_teams')][0]['viewed_milli_seconds'] == 2

    # User profile 2 should have 'ice hockey' as favorite and only sport
    assert res.loc[('2', 'fav_sports')][0]['name'] == 'ice hockey'
    assert res.loc[('2', 'fav_sports')][0]['viewed_milli_seconds'] == 2

    # User 2 should have NHL as favorite league with 2 ms
    assert res.loc[('2', 'fav_leagues')][0]['name'] == 'NHL'
    assert res.loc[('2', 'fav_leagues')][0]['viewed_milli_seconds'] == 2

    # User 2 should have team6 as favorite team with 2 ms and a total of 3 favorite teams
    assert len(res.loc[('2', 'fav_teams')]) == 3
    assert res.loc[('2', 'fav_teams')][0]['name'] == 'team6'
    assert res.loc[('2', 'fav_teams')][0]['sport'] == 'ice hockey'
    assert res.loc[('2', 'fav_teams')][0]['league'] == 'NHL'
    assert res.loc[('2', 'fav_teams')][0]['viewed_milli_seconds'] == 2

if __name__ == "__main__":
    
    # Tests
    test_missing_ids_empty_string()
    test_missing_ids_na()
    test_selected_sports()
    test_get_fav_sports()
    test_get_fav_leagues()
    test_get_fav_teams()
    test_fav_sports_leagues_teams_multiple_users()

    # Print this if everything worked
    print("All Tests Passed")
