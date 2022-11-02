import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    city = input("enter the desired city from new york city, washington and chicago").lower()
    while city not in ["new york city", "chicago", "washington"]:
        city = input("enter the desired city")
        
    

    # TO DO: get user input for month (all, january, february, ... , june)

    month = input("enter the desired month from january to june or else type all").lower()
    while month not in ["january", "february", "march", "april", "may", "june", "all"]:
        month = input("enter the desired month")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    day = input("enter the desired day or else type all").lower()
    while day not in ["all", "monday", "tuesday","wednesday","thursday", "friday", "saturday", "sunday"]:
        day = input("enter the desired day")


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    most_common_month=df['month'].mode()[0]
    print("most common month: ", most_common_month)

    # TO DO: display the most common day of week
    
    most_common_day=df['day_of_week'].mode()[0]
    print("most common day: ", most_common_day)
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour=df['hour'].mode()[0]
    print("most common hour: ", most_common_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station=df['Start Station'].mode()[0]
    print("most common start station: ", most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station=df['End Station'].mode()[0]
    print("most common end station: ", most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_common_end_start_station=df.groupby(['Start Station', 'End Station']).size().idxmax()
    print("most frequent combination of start station and end station trip: ", most_common_end_start_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    sum_time = sum(df["Trip Duration"])/3600
    print("total travel time: ", sum_time)

    # TO DO: display mean travel time
    mean_time = df["Trip Duration"].mean()/3600
    print("avg travel time: ", mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type=df["User Type"].value_counts()
    print(user_type)

    # TO DO: Display counts of gender
    if("Gender" in df.columns):
        user_gender=df["Gender"].value_counts()
        print(user_gender)
       


    # TO DO: Display earliest, most recent, and most common year of birth
    if("Birth Year" in df.columns):
        earliest = df["Birth Year"].min()
        recent = df["Birth Year"].max()
        common = df["Birth Year"].mode()[0]
        print("earliest year", int(earliest))
        print("recent year", int(recent))
        print("most common year", int(common))
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    while (view_data == "yes"):
      print(df.iloc[start_loc:start_loc+5])
      start_loc += 5
      view_data = input("Do you wish to continue?: ").lower()
 

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


