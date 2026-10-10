import random
import webbrowser

print("ASSISTANT FOR YOUR MOOD ")
name = input("What is your name? ")
print(f"\nHello {name}! ")

print("\nWhat do you want to do?")
print("1 - I want to laugh")
print("2 - I want to cry")
print("3 - I want to get fear")
print("4 - I want to get action")
print("5 - I want to get romantic")

select = input("\nSelect (1/2/3/4/5): ")

laugh_films = [
     "https://www.imdb.com/title/tt0384116/"
]

cry_films = [
    "https://www.imdb.com/title/tt0476735/"
]

fear_films = [
    "https://www.imdb.com/title/tt0054215/"
]

action_films = [
    "https://www.imdb.com/title/tt0266697/"
]

romantic_films = [
    "https://www.imdb.com/title/tt0251127/"
]

if select == "1":
    selected_films = random.choice(laugh_films)
    print("\nExcellent. Let's make you laugh with some funny movies.")
elif select == "2":
    selected_films = random.choice(cry_films)
    print("\nI'm sorry to hear that but lets watch some sad movies to help you cry.")
elif select == "3":
    selected_films = random.choice(fear_films)
    print("\nCool and let's watch some scary movies to get your adrenaline pumping.")
elif select == "4":
    selected_films = random.choice(action_films)
    print("\nGreat! Let's watch some action movies to get your heart racing.")
elif select == "5":
    selected_films = random.choice(romantic_films)
    print("\nSweet! Let's watch some romantic movies to make you feel lovely and cozy.")
else:
    print("\nInvalid selection, but don't worry, I will select a random movie for you.")
    selected_films = "https://www.imdb.com/title/tt0087884/" 

webbrowser.open(selected_films)
