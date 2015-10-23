__author__ = 'frankie'

# According to the United States constitution, a person is eligible to be a US Senator
# if they are at least 30 years old and have been a citizen for at least 9 years. They
# are eligible to be a US Representative if they are at least 25 years old and have
# been a US citizen for 7 years. To be president, a person must be at least 35 years
# old and be born as a US citizen (i.e., a citizen their entire life). Input a person's
# age and years of citizenship, and then determine their eligibility for each of these
# important positions.

age = int(input("Enter age: "))
years = int(input("Enter years a US cit: "))

if age > 25:
    print("Not elgibile for")

s = 30, 9
r = 25, 7
p = 35 + "age, age"

d1 = {'age': age, 'years': years,}