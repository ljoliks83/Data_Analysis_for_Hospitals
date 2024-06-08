import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # option from the task
    pd.set_option('display.max_columns', 8)

    # import data
    general_df = pd.read_csv('test/general.csv')
    prenatal_df = pd.read_csv('test/prenatal.csv')
    sports_df = pd.read_csv('test/sports.csv')

    # make all the columns same in the dfs
    prenatal_df = prenatal_df.rename(columns={'HOSPITAL': 'hospital', 'Sex': 'gender'})
    sports_df = sports_df.rename(columns={'Hospital': 'hospital', 'Male/female': 'gender'})

    # concat dfs and drop unneeded column
    hospitals_df = pd.concat([general_df, prenatal_df, sports_df], ignore_index=True)
    hospitals_df.drop(columns='Unnamed: 0', inplace=True)

    # delete empty rows
    hospitals_df.dropna(axis='rows', how='all', inplace=True)

    # correct gender column values
    hospitals_df['gender'] = hospitals_df['gender'].replace({
        'female': 'f', 'woman': 'f',
        'male': 'm', 'man': 'm'
    })

    # remove NaN from gender
    hospitals_df['gender'] = hospitals_df['gender'].fillna('f')

    # set Nan as 0 in tests bmi, diagnosis, blood_test, ecg, ultrasound, mri, xray, children, months
    for col in ['bmi', 'diagnosis', 'blood_test', 'ecg', 'ultrasound', 'mri', 'xray', 'children', 'months']:
        hospitals_df[col] = hospitals_df[col].fillna(0)

    # histogram to show most common age
    age_bins = [0, 15, 35, 55, 70, 80]
    plt.figure(1)
    plt.hist(hospitals_df['age'], bins=age_bins, edgecolor='white')

    # pie chart to show most common diagnosis
    plt.figure(2)
    labels_diag = hospitals_df['diagnosis'].unique()
    plt.pie(hospitals_df['diagnosis'].value_counts(), labels=labels_diag)

    # violin chart to show height distribution
    plt.figure(3)
    plt.violinplot(hospitals_df['height'])

    plt.show()

    answers = ['15-35', 'pregnancy', 'in sports hospital height in inches, in others in meters']

    for i in range(0, 3):
       print(f'The answer to the {i+1}st question: {answers[i]}')
