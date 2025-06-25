import json
import requests
import random
import os
import time

def parse_students_json():
    try:
        with open("students.json", "r") as f:
            students = json.load(f)
            for student in students:
                print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
    except FileNotFoundError:
        print("students.json not found.")
    except json.JSONDecodeError:
        print("students.json is not a valid JSON file.")

def get_weather():
    url = "https://api.open-meteo.com/v1/forecast?latitude=41.31&longitude=69.25&current_weather=true"
    try:
        response = requests.get(url)
        data = response.json()
        weather = data.get("current_weather")
        if weather:
            print("Weather in Tashkent:")
            print(f"Temperature: {weather['temperature']}°C")
            print(f"Windspeed: {weather['windspeed']} km/h")
            print(f"Time: {weather['time']}")
        else:
            print("No weather data found.")
    except Exception as e:
        print("Error:", e)

def load_books():
    if not os.path.exists("books.json"):
        return []
    with open("books.json", "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_books(books):
    with open("books.json", "w") as f:
        json.dump(books, f, indent=4)

def add_book(title, author):
    books = load_books()
    books.append({"title": title, "author": author})
    save_books(books)
    print("Book added.")

def update_book(old_title, new_title, new_author):
    books = load_books()
    for book in books:
        if book["title"] == old_title:
            book["title"] = new_title
            book["author"] = new_author
            save_books(books)
            print("Book updated.")
            return
    print("Book not found.")

def delete_book(title):
    books = load_books()
    books = [book for book in books if book["title"] != title]
    save_books(books)
    print("Book deleted.")

def recommend_movie_by_genre(genre):
    sample_movies = {
        "action": ["Mad Max: Fury Road", "Die Hard", "John Wick"],
        "comedy": ["Superbad", "Step Brothers", "The Hangover"],
        "drama": ["Forrest Gump", "The Shawshank Redemption", "Fight Club"],
        "sci-fi": ["Interstellar", "Inception", "The Matrix"],
        "romance": ["The Notebook", "Pride and Prejudice", "La La Land"]
    }

    genre = genre.lower()
    if genre in sample_movies:
        movie = random.choice(sample_movies[genre])
        print(f"Recommended {genre.title()} Movie: {movie}")
    else:
        print("Genre not found. Try: action, comedy, drama, sci-fi, romance.")

def main():
    while True:
        print("\n--- MENU ---")
        print("1. Parse students.json")
        print("2. Get Weather (Tashkent)")
        print("3. Add Book")
        print("4. Update Book")
        print("5. Delete Book")
        print("6. Recommend Movie by Genre")
        print("7. Exit")
        choice = input("Choose an option (1-7): ")

        if choice == "1":
            parse_students_json()
        elif choice == "2":
            get_weather()
        elif choice == "3":
            title = input("Book title: ")
            author = input("Book author: ")
            add_book(title, author)
        elif choice == "4":
            old_title = input("Old title: ")
            new_title = input("New title: ")
            new_author = input("New author: ")
            update_book(old_title, new_title, new_author)
        elif choice == "5":
            title = input("Book title to delete: ")
            delete_book(title)
        elif choice == "6":
            genre = input("Enter movie genre: ")
            recommend_movie_by_genre(genre)
        elif choice == "7":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
