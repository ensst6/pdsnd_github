# Bikeshare.py
A Python script to display and analyze bike sharing data from three cities (New York City, Washington DC, and Chicago)

### Description
The script reads data provided by [Motivate](https://www.motivateco.com/) for
bikeshare use in the first six months of 2017 from New York, Washington, and
Chicago. The user selects which city to analyze. Data can be filtered by month and day. The user can also elect to display detailed or basic data. Finally, the raw data can be viewed five lines at a time.  
The data that are displayed are:
- Most popular month, day, and start hour by number of trips
(top 5 if detail requested; will not be available for month or day if filtered)
- Most popular start & end station by number of trips (top 5 if detail requested)
- Most popular trip (start & end combination) by number of trips (top 5 if
  detail requested)
- Total and mean travel time
- Number of users by user type (Subscriber, Customer, Dependent)
- Number of users by gender (only available for Chicago and New York)
- Earliest, latest, and most common birth year (top 5 if detail requested; only
  available for Chicago and New York)

### Data Files
The bikeshare data for each city are stored in  separate comma-separated variable files:
- Washington, DC:  `washington.csv`
- Chicago: `chicago.csv`
- New York: `new_york_city.csv`

These should be placed in the same directory as the `bikeshare.py` script and
their filenames should not be changed.

### Usage
`> python bikeshare.py`  

Prompts:
1. Enter city name (case-insensitive)
2. Select number of month to filter by (`0` for all)
3. Select number of day to filter by (`0` for all)
4. Choose whether to print detailed reports. This will print the top 5 entries
in each category, rather than just the most popular one. (`Y/N`; case-insensitive)
5. After the analysis runs and the reports display, the user has the option to
display the raw data file five lines at a time. Anything except `no <Enter>`
will display the next five lines.
6. Finally, the user has the option to restart at the beginning. Anything except
`yes <Enter>` stops the program.


### Dependencies
`numpy : 1.18.5`  
`pandas : 1.0.5`  

Developed & tested in `Python 3.8.3`

#### History
Created September 24, 2020

#### License  
[Licensed](license.md) under the [MIT License](https://spdx.org/licenses/MIT.html). Yours to do with what you will.
