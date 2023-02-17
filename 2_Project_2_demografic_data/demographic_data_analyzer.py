import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    # path = r"D:\Dev\freecodecamp-intro-to-pandas\Новая папка\adult.data.csv"
    # df = pd.read_csv(path, na_values=['?'])
    df = pd.read_csv('adult.data.csv', na_values=['?'])

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    mask = df['sex'] == 'Male'
    average_age_men = round(df['age'][mask].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    mask = df['education'] == 'Bachelors'
    total_bach = df['education'][mask].count()
    total = df['education'].count()
    percentage_bachelors = round(total_bach * 100 / total, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    mask1= df['education'] == 'Bachelors'
    mask2= df['education'] == 'Masters'
    mask3= df['education'] == 'Doctorate'
    rich = df['salary'] == '>50K'

    higher_education = round(
        df['education']
        [mask1 | mask2 | mask3].count(), 1)

    lower_education = round(
        df['education']
        [~(mask1 | mask2 | mask3)].count(), 1)

    # percentage with salary >50K
    higher_education_rich = round(
        df['education']
        [(mask1 | mask2 | mask3) & rich].count() * 100 / higher_education, 1)

    lower_education_rich = round(
        df['education']
        [~(mask1 | mask2 | mask3) & rich].count() * 100 / lower_education, 1)   

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = round(df['hours-per-week'].min(), 1)

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    mask = df['hours-per-week'] == df['hours-per-week'].min()
    num_min_workers = df['hours-per-week'][mask].count()

    amt_min_hours_rich = df['hours-per-week'][mask & rich].count()
    rich_percentage = round(amt_min_hours_rich * 100 / num_min_workers, 1)

    # What country has the highest percentage of people that earn >50K?
    rich_amt = df[rich].groupby(['native-country']).size()

    total = df.groupby(['native-country'])['salary'].size()
    mask_percentage = round(rich_amt * 100/ total, 1)
    highest_earning_country_percentage = mask_percentage.sort_values(ascending=False)[0]
    highest_earning_country = mask_percentage.sort_values(ascending=False).index[0]


    # Identify the most popular occupation for those who earn >50K in India.
    mask_india = df['native-country'] == 'India'
    main_mask = df[mask_india & rich]['occupation'].value_counts()
    top_IN_occupation = main_mask.index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
