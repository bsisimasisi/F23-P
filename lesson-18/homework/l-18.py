import pandas as pd

df = pd.read_csv("C:\Users\abduv\F23-P\lesson-18\homework\stackoverflow_qa.csv")
df['creationdate'] = pd.to_datetime(df['creationdate'])

before_2014 = df[df['creationdate'] < '2014-01-01']
print(before_2014)

score_above_50 = df[df['score'] > 50]
print(score_above_50)

score_between_50_100 = df[(df['score'] >= 50) & (df['score'] <= 100)]
print(score_between_50_100)

answered_by_scott = df[df['ans_name'] == 'Scott Boston']
print(answered_by_scott)

five_users = ['Unutbu', 'Scott Boston', 'Mike Pennington', 'unutbu', 'Demitri']
answered_by_5 = df[df['ans_name'].isin(five_users)]
print(answered_by_5)

filtered = df[
    (df['creationdate'] >= '2014-03-01') & 
    (df['creationdate'] <= '2014-10-31') & 
    (df['ans_name'].str.lower() == 'unutbu') & 
    (df['score'] < 5)
]
print(filtered)

score_or_views = df[(df['score'].between(5, 10)) | (df['viewcount'] > 10000)]
print(score_or_views)

not_by_scott = df[df['ans_name'] != 'Scott Boston']
print(not_by_scott)

titanic_df = pd.read_csv("C:\Users\abduv\F23-P\lesson-18\homework\titanic.csv")

female_class1_20_30 = titanic_df[
    (titanic_df['Sex'] == 'female') &
    (titanic_df['Pclass'] == 1) &
    (titanic_df['Age'].between(20, 30))
]
print(female_class1_20_30)

fare_over_100 = titanic_df[titanic_df['Fare'] > 100]
print(fare_over_100)

survived_alone = titanic_df[
    (titanic_df['Survived'] == 1) &
    (titanic_df['SibSp'] == 0) &
    (titanic_df['Parch'] == 0)
]
print(survived_alone)

embarked_c_fare_50 = titanic_df[
    (titanic_df['Embarked'] == 'C') &
    (titanic_df['Fare'] > 50)
]
print(embarked_c_fare_50)

with_family = titanic_df[
    (titanic_df['SibSp'] > 0) & (titanic_df['Parch'] > 0)
]
print(with_family)

kids_not_survived = titanic_df[
    (titanic_df['Age'] <= 15) & (titanic_df['Survived'] == 0)
]
print(kids_not_survived)

cabin_and_fare_200 = titanic_df[
    titanic_df['Cabin'].notna() & (titanic_df['Fare'] > 200)
]
print(cabin_and_fare_200)

odd_passenger_ids = titanic_df[titanic_df['PassengerId'] % 2 != 0]
print(odd_passenger_ids)

ticket_counts = titanic_df['Ticket'].value_counts()
unique_tickets = ticket_counts[ticket_counts == 1].index
unique_ticket_df = titanic_df[titanic_df['Ticket'].isin(unique_tickets)]
print(unique_ticket_df)

miss_class1 = titanic_df[
    (titanic_df['Sex'] == 'female') &
    (titanic_df['Name'].str.contains('Miss')) &
    (titanic_df['Pclass'] == 1)
]
print(miss_class1)
