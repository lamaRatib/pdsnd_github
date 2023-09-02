import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city= input('Would u like to see data for Chicago, New York or Washington?\n').title()
        if city=='Chicago' or city=='New York' or city=='Washington':
            city=city.lower()
            break;
        else:
            print('wrong answer, pls choose one of the cities: Chicago, New York or Washington:')
            
            
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        filtering= input('Would u like to filter data by month, day, both or not at all? type none for no filter.\n')
        if filtering=='month' or filtering=='day' or filtering=='both' or filtering=='none':
            break     
        else:
            print('wrong answer, pls choose one of the options:')
            
    if filtering=='month' or filtering=='both':
        while True:
            month=input('Which month? January, February, March, April, May, June?\n')
            if month=='January' or month=='February' or month=='March' or month=='April' or month=='May' or month=='June':
                break
            else:
                print('wrong answer, pls choose one of the options:')
        if filtering=='month':
            day='all' 
                

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    if filtering=='day'or filtering=='both':
        while True:
            day=input('Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday?\n')
            if day=='Monday' or day=='Tuesday' or day=='Wednesday' or day=='Thursday' or day=='Friday' or day=='Saturday' or day=='Sunday':
                break
            else:
                print('wrong answer, pls choose one of the options:')
        if filtering=='day': 
            month='all'
                    
    if filtering=='none':
        month='all'
        day='all'
       
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month=month.lower()
        month = months.index(month) + 1
 
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    commonMonth = df['month'].mode()[0]
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    print('Most common Month:', months[commonMonth-1])

    # TO DO: display the most common day of week
    commonDay = df['day_of_week'].mode()[0]
    print('Most common Day:', commonDay)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    commonHour = df['hour'].mode()[0]
    print('Most common Start Hour:', commonHour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    commonSS = df['Start Station'].mode()[0]
    print('Most commonly used start station:', commonSS)

    # TO DO: display most commonly used end station
    commonES = df['End Station'].mode()[0]
    print('Most commonly used end station:', commonES)

    # TO DO: display most frequent combination of start station and end station trip
    frequentcombo= df.groupby(['Start Station', 'End Station']).size().idxmax()
    print('Most frequent combination of start station and end station:', frequentcombo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    totalTravelTime=df['Trip Duration'].sum()
    print('Total travel time in sec: ',totalTravelTime)

    # TO DO: display mean travel time
    meanTravelTime=df['Trip Duration'].mean()
    print('Mean travel time in sec: ',meanTravelTime)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    userCounts = df['User Type'].value_counts()
    print('User Type Counts:',dict(userCounts))

    # TO DO: Display counts of gender
    if 'Gender' in df:
        genderCounts = df['Gender'].value_counts()
        print('\nGender Counts:',dict(genderCounts))
    else:
        print('\nGender is not available in the dataset')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest = df['Birth Year'].min()
        mostRecent= df['Birth Year'].max()
        mostCommon= df['Birth Year'].mode()[0]
        print('\nEarliest Birth Year:', int(earliest))
        print('Most Recent Birth Year:', int(mostRecent))
        print('Most Common Birth Year:', int(mostCommon))
    else:
        print('\nBirth year is not available in the dataset')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    view_data=input('\nWould u like display 5 rows of data?(yes/no)\n').lower()
    start_loc=0
    while view_data =='yes':
        print( df.iloc[start_loc:start_loc + 5])
        start_loc+=5
        view_data=input('\nWould u like display the next 5 rows of data?(yes/no)\n').lower()
        
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
