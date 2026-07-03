import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    total_bachelors = len(df[df['education'] == "Bachelors"])
    total = len(df)
    percentage_bachelors = round((total_bachelors / total) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = round((len(df[(df['education'] == "Bachelors") | (df['education'] == "Masters") | (df['education'] == "Doctorate")]) / len(df)) * 100, 1)
    lower_education = round((len(df[(df['education'] != "Bachelors") & (df['education'] != "Masters") & (df['education'] != "Doctorate")]) / len(df)) * 100, 1)

    # percentage with salary >50K
    higher_education_rich = round((len(df[((df['education'] == "Bachelors") | (df['education'] == "Masters") | (df['education'] == "Doctorate")) & (df['salary'] == ">50K")]) / len(df[(df['education'] == "Bachelors") | (df['education'] == "Masters") | (df['education'] == "Doctorate")])) * 100, 1)
    lower_education_rich = round((len(df[((df['education'] != "Bachelors") & (df['education'] != "Masters") & (df['education'] != "Doctorate")) & (df['salary'] == ">50K")]) / len(df[(df['education'] != "Bachelors") & (df['education'] != "Masters") & (df['education'] != "Doctorate")])) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = len(df[df['hours-per-week'] == df['hours-per-week'].min()])

    rich_percentage = (len(df[(df['hours-per-week'] == df['hours-per-week'].min()) & (df['salary'] == '>50K')]) / len(df[df['hours-per-week'] == df['hours-per-week'].min()])) * 100

    # What country has the highest percentage of people that earn >50K?
    country_rich_counts = pd.DataFrame(df.groupby(['native-country'])['salary'].value_counts())
    country_rich_counts = country_rich_counts.loc[(slice(None), '>50K'), :]
    country_counts = pd.DataFrame(df.groupby(['native-country'])['salary'].count())
    country_mix_counts = country_counts.merge(country_rich_counts, on='native-country')
    country_mix_counts = country_mix_counts.rename(columns={'salary': 'total-count', 'count': 'rich-count'})
    country_mix_counts['rich-percentage'] = ((country_mix_counts['rich-count'] / country_mix_counts['total-count']) * 100).round(1)
    country_mix_counts = country_mix_counts.sort_values('rich-percentage', ascending=False)
    country_mix_counts = country_mix_counts.reset_index()[['native-country', 'total-count', 'rich-count', 'rich-percentage']]

    highest_earning_country = country_mix_counts.iloc[0]['native-country']
    highest_earning_country_percentage = country_mix_counts.iloc[0]['rich-percentage']

    # Identify the most popular occupation for those who earn >50K in India.
    occupation_india = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts()
    top_IN_occupation = occupation_india.keys()[0]

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
