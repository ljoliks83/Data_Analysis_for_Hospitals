# hospital with the highest number of patients
highest_patient_number_hospital = hospitals_df.pivot_table(columns='hospital', aggfunc='count').max().index[0]
patients_general = hospitals_df.pivot_table(columns='hospital', aggfunc='count').max().iloc[0]
patients_sports = hospitals_df.pivot_table(columns='hospital', aggfunc='count').max().iloc[2]

# stomach diagnosis in general hospital
stomach_patients_general = round((hospitals_df.loc[(hospitals_df['diagnosis'] == 'stomach') &
                                                  (hospitals_df['hospital'] == 'general')].count().max())
                                / patients_general, 3)

# dislocations patients in sports hospital
disloc_patients_sport = round((hospitals_df.loc[(hospitals_df['diagnosis'] == 'dislocation') &
                                                  (hospitals_df['hospital'] == 'sports')].count().max())
                                / patients_sports, 3)

# difference in median ages for general and sports hospitals
hospitals_ages_df = hospitals_df.pivot_table(index='hospital', values='age', aggfunc='median')
median_ages_diff = abs(int(hospitals_ages_df.loc['general', 'age'] - hospitals_ages_df.loc['sports', 'age']))

# hospital with maximum number of blood tests taken
hospitals_btt_df = hospitals_df.loc[hospitals_df['blood_test'] == 't']
max_btt_count_hospital = hospitals_btt_df.pivot_table(index='hospital', values='blood_test',
                                                      aggfunc='count').idxmax().iloc[0]
max_btt_count_count = hospitals_btt_df.pivot_table(index='hospital', values='blood_test',
                                                   aggfunc='count').max().iloc[0]

# printing the answers
print('The answer to the 1st question is ' + highest_patient_number_hospital)
print('The answer to the 2nd question is ' + str(stomach_patients_general))
print('The answer to the 3rd question is ' + str(disloc_patients_sport))
print('The answer to the 4th question is ' + str(median_ages_diff))
print('The answer to the 5th question is ' + max_btt_count_hospital + ', ' + str(max_btt_count_count) + ' blood tests')
