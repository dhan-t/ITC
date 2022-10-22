# NEEDS TO FIND OUT USER AGE AND MUSIC SUGGESTION FOR THE YEAR OF BIRTH
# takes input of birthdate and age from user

year = int(input("What is your birth year?"))
age = 2022 - year

# processes the year born and adds the results of age to the printed stage

if year >= 1922 and year <= 1949:
    print("Your age is" , age , "Jazz is recommended for you")
elif year >= 1950 and year <= 1959:
    print("Your age is" , age , "Country is recommended for you")
elif year >= 1960 and year <= 1969:
    print("Your age is" , age , "Rock is recommended for you")
elif year >= 1970 and year <= 1979:
    print("Your age is" , age , "Disco is recommended for you")
elif year >= 1980 and year <= 1989:
    print("Your age is" , age , "Pop is recommended for you")
elif year >= 1990 and year <= 1999:
    print("Your age is" , age , "Rock is recommended for you")
elif year >= 2000 and year <= 2009:
    print("Your age is " , age , " R&B is recommended for you")
else:
    print("Your age is" , age , "You can listen to any genre you want")
    
# Original upload date: 09/08/2022
