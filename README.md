# NENT Tech test

For this Tech test I had to develop 3 tasks related to data transformation. I have tried to get the task execution stable enough by also developing a small suite of unit tests for each task.

## Dependencies

For this tech test I have used Python 3.7 and Pandas for the data manipulation. The test was developed in a Python virtual environment created and managed with `pipenv`, a python library for virtual environment management. This means that the only requirements needed in you computer to run this project are `Python 3.7` and `pipenv==2020.11.15`.

Inside the virtual environment are the actual dependencies of the project. Here is a list of all of them obtained via the command `pipenv run pip freeze`:

```
numpy==1.20.2
pandas==1.2.4
pyarrow==4.0.0
python-dateutil==2.8.1
pytz==2021.1
six==1.15.0
```

In order to install these dependencies in the virtual environment the following command must be run before executing any code:

```
pipenv run pip install -r requirements.txt
```

## Execution instructions

In order to execute any code in this project one must only run the command:

```
pipenv run python file_to_execute.py
```

## Task 1

For this task I had to get the favorite sports, leagues and teams of each user in the dataset `ViewingData.snappy.parquet`. Apart from this, some other things must be taken into consideration like the user not having a `profile_id` in the dataset, in which case I should use the `user_id`.

The expected output of this task has the following structure:

```
[profile_id: string (nullable = true),
favSports: array ( struct (name: string, viewedMilliseconds: long),
favLeagues: array ( struct (name: string, viewedMilliseconds: long),
favTeams: array ( struct (name: string, viewedMilliseconds: long, seriesGuid: string, sport: string)]
```

My approach to this task was to group all rows in the dataset by their `profile_id` and then perform the necessary operations to get the favorite sports, leagues and teams based on the time they have spent watching their content.

The final output of this task is saved in a csv file with 4 columns:

- `profile_id`: The ID of the user in the platform.

- `fav_sports`: a Python list with each sport the user has watched ordered by the total time spent watching it. Each sport is saved in the structure of a Python dictionary with attributes: `name` and `viewed_milli_seconds`.

- `fav_leagues`: a Python list with each league the user has watched ordered by the total time spent watching it. Each league is saved in the structure of a Python dictionary with attributes: `name` and `viewed_milli_seconds`.

- `fav_teams`: a Python list with each league the user has watched ordered by the total time spent watching it. Each league is saved in the structure of a Python dictionary with attributes: `name`, `sport`, `league` and `viewed_milli_seconds`. Each team in this list is considered individually, which means that for every match shown in the dataset the names of the teams were extracted and the viewed time of the match was added.

## Task 2

The second task consisted in counting the number of watches each individual program from the dataset `started_streams.csv` gets, as well as the number of unique users that watch each program and in which device, country and product type.

The expected output of this task has the following structure:

```
[program_title,device_name,country_code,product_type,unique_users,content_count]
```

For this task, my approach was once again to group the rows of the dataset by `program_title` and then use aggregation functions to count the number of views and the number of unique users.

As for the country, product type and device I made the assumption that the task wanted me to pick the most common of each of them for that specific `program_title` as the task specification document did not explicitly say how to select those fields.

## Task 3

In this last task the objective was to get the top 10 most watched genres in the dataset `started_streams.csv` as well as which hour got the maximum watches for each of them.

The expected output of this task has the following structure:

```
[genre,unique_users,peak_hour(24 hours patterns means 00 to 23), peak_hour_unique_users]
```

The first thing I did for this task was to extract the `hour` from the column `time` to a new column in order to make the following operations more convenient to implement.

Then, I once again grouped the rows in the dataset by `genre` and counted the number of unique users, calculated the `peak_hour` (most common hour for that genre) and the number of unique users that were watching at that `peak_hour`.

# Tests

Tests can be found in the `test/` folder of the project in 3 different files, one for each task:

```
task_1_test.py
task_2_test.py
task_3_test.py
```

Test can be run with:

```
pipenv run python task_X_test.py
```
