import time
import pandas as pd
import numpy as np
import sys

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
              
MONTH_DATA = months = { 0:'All', 1:'January', 2:'February', 3:'March', 
                        4:'April', 5:'May', 6:'June' }
                        
DAY_DATA = { 0:'All', 1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday',
             5:'Friday', 6:'Saturday', 7:'Sunday' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (int) month - integer for month to filter by (Jan = 1 ... Jun = 6), 
                      or 0 to apply no month filter
        (int) day - integer for day of week to filter by (Mon = 1 ... Sun = 7), 
                    or 0 to apply no day filter
        (bool) detailed - whether or not to print detailed reports
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while city not in CITY_DATA.keys():
        city = input('Enter city to retrieve bikeshare data for (Washington, \
New York, Chicago): ').lower()
    
    print('Your city choice was: {}'.format(city.title()))
    
    # get user input for month (all, january, february, ... , june)  
    month = -1
    while month not in MONTH_DATA.keys():
        print('\nEnter number for month to filter by (0 for all): ')
        for i in MONTH_DATA.keys():
            print('{}: {}'.format(i, MONTH_DATA[i]))
        try:
            month = int(input('Your selection: '))
        except ValueError:
            print('Please enter a valid number from the list above')

    print('Your month choice was: {}'.format(MONTH_DATA[month]))


    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = -1
    while day not in DAY_DATA.keys():
        print('\nEnter number for day to filter by (0 for all): ')
        for i in DAY_DATA.keys():
            print('{}: {}'.format(i, DAY_DATA[i]))
        try:
            day = int(input('Your selection: '))
        except ValueError:
            print('Please enter a valid number from the list above')

    print('Your day choice was: {}'.format(DAY_DATA[day]))
    
    detail = ''
    detailed = False
    while detail.upper() not in ('Y', 'N'):
        detail = input('\nprint detailed reports (top 5 entries with data for \
each category)? (Y/N): ')
    
    if detail.upper() == 'Y':
        detailed = True
        print('Detailed reports will be printed')
    else:
        print('Detailed reports will not be printed')
        
    print('-'*40)
    return city, month, day, detailed


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (int) month - integer for month to filter by (Jan = 1 ... Jun = 6), 
                      or 0 to apply no month filter
        (int) day - integer for day of week to filter by (Mon = 1 ... Sun = 7), 
                    or 0 to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    df= pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] =pd.to_datetime(df['Start Time'])
    
    # get month as integer, calendar-indexed (Jan = 1, etc)
    df['month'] = df['Start Time'].dt.month
    
    # get day as name
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 0:
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 0:
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == DAY_DATA[day]]

    print('\nData imported for {}. Filtered by month = {} and day = {}.'.format(
            city.title(), MONTH_DATA[month], DAY_DATA[day]))
    print('-'*40)

    return df


def time_stats(df, month, day, detailed):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    if month == 0:
        popular_month = df['month'].mode()[0]
        print('\nMost popular month : {}'.format(MONTH_DATA[popular_month]))
    # detailed data if requested
        if detailed:
            month_count = df.groupby(['month'])['month'].count()
            month_count = month_count.rename(index = MONTH_DATA)
            print('Top 5:\n', month_count.sort_values(ascending = False)[0:5])
    # skip calculations if filtered
    else:
        print('\nMonth is filtered. Most popular by default is {}.'.format(
              MONTH_DATA[month]))
        if detailed:
            print('Detailed reporting inhibited by filter.')

    # display the most common day of week
    if day == 0:
        popular_day = df['day_of_week'].mode()[0]
        print('\nMost popular day of week : {}'.format(popular_day))
    # detailed data if requested
        if detailed:
            day_count = df.groupby(['day_of_week'])['day_of_week'].count()
            print('Top 5:\n', day_count.sort_values(ascending = False)[0:5])
    # skip calculations if filtered
    else:
        print('\nDay is filtered. Most popular by default is {}.'.format(
              DAY_DATA[day]))
        if detailed:
            print('Detailed reporting inhibited by filter.') 
            
    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('\nMost popular start hour : {}'.format(popular_hour))
    # detailed data if requested
    if detailed:
        hr_count = df.groupby(['hour'])['hour'].count()
        print('Top 5:\n', hr_count.sort_values(ascending = False)[0:5])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df, detailed):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station   
    popular_start = df['Start Station'].mode()[0]
    print('\nMost popular start station : {}'.format(popular_start))
    # detailed data if requested
    if detailed:
        start_count = df.groupby(['Start Station'])['Start Station'].count()
        print('Top 5:\n', start_count.sort_values(ascending = False)[0:5])
    

    # display most commonly used end station
    popular_end = df['End Station'].mode()[0]
    print('\nMost popular end station : {}'.format(popular_end))
    # detailed data if requested
    if detailed:
        end_count = df.groupby(['End Station'])['End Station'].count()
        print('Top 5:\n',end_count.sort_values(ascending = False)[0:5])



    # display most frequent combination of start station and end station as trip
    df['trip'] = df['Start Station']+' - '+df['End Station']
    popular_trip = df['trip'].mode()[0]
    print('\nMost popular trip : {}'.format(popular_trip))   
    # detailed data if requested
    if detailed:
        trip_count = df.groupby(['trip'])['trip'].count()
        print('Top 5:\n',trip_count.sort_values(ascending = False)[0:5])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    tot_travel_time = df['Trip Duration'].sum()
    tot_days = tot_travel_time//(3600*24)
    tot_hrs = (tot_travel_time%(3600*24))//3600
    tot_mins = (tot_travel_time%(3600*24))%3600//60
    tot_secs = (tot_travel_time%(3600*24))%3600%60
    print('\nTotal travel time : {} days {} hrs {} min {} sec'.format(int(tot_days), 
          int(tot_hrs), int(tot_mins),int(tot_secs)))

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    mean_mins = mean_travel_time//60
    mean_secs = mean_travel_time%60
    print('\nMean travel time : {} min {} sec'.format(int(mean_mins), 
          int(mean_secs)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city, detailed):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_count = df.groupby(['User Type'])['User Type'].count()
    print ('\nUsers by type:\n{}'.format(user_count))
    
    # Display counts of gender
    if city != 'washington': 
        gender_count = df.groupby(['Gender'])['Gender'].count()
        print ('\nUsers by gender:\n{}'.format(gender_count))
    # Display earliest, most recent, and most common year of birth
        min_birth = df['Birth Year'].min()
        max_birth = df['Birth Year'].max() 
        popular_birth = df['Birth Year'].mode()[0]    
        print('\nEarliest birth year : {}'.format(int(min_birth)))
        print('Latest birth year : {}'.format(int(max_birth)))
        print('Most common birth year : {}'.format(int(popular_birth)))
    # detailed info, if requested (add code for top 5 birth years)
        if detailed:
    # for some reason, the previous syntax for getting the sorted list wouldn't work
    # error was "index must be monotonic" which year certainly is but...
            birth_ct = df.groupby(['Birth Year'])['Birth Year'].count()
            birth_count = birth_ct.sort_values(ascending = False)
            print('Top 5:\n',birth_count.iloc[0:5])      
    else:
        print('\nGender & birthdate not available for Washington')  
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day, detailed = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day, detailed)
        station_stats(df, detailed)
        trip_duration_stats(df)
        user_stats(df, city, detailed)
        
    # Display raw data 5 rows at a time, if desired
        raw = ' '
        row_count = 0
        while True:       
            raw = input('\nDo you want to see the next five rows of raw data? \
Enter no to cancel or stop; anything else to continue: ')
            if raw.lower() == 'no':
                break
            else:
                print('\nNext five rows of data:\n', df[:][row_count:row_count+5])
                row_count += 5

        restart = input('\nWould you like to restart? Enter yes to keep going, \
anything else to stop.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
