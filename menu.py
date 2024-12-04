#Technewjeans Exercise 9
import os

movies = {
    "Title": ["Portrait of a Lady on Fire"], 
    "Director": ["Céline Sciamma"], 
    "Release date": ["September 18, 2019"], 
    "Genre": ["Historical Drama"], 
    "Language": ["French"]
}

# Main menu function
def show_menu():
    print("\n----- Netflix Movies Recommendations -----")
    print("1. List All Movies")
    print("2. Add a Movie")
    print("3. Update a Movie")
    print("4. Delete a Movie")
    print("5. Search for a Movie")
    print("6. Exit")

# Function to list all movies
def list_all_movies():
    if not movies:
        print("No movies available.")
    else:
        for key in movies:
            print(f"{key}: {movies[key]}")
        
        return " "

   
def add_movie(range_of_dictionary):
    title = input("Enter film title: ")
    director = input("Enter film director: ")
    release_date = input("Enter film release date: ") 
    genre = input("Enter film genre: ")
    language = input("Enter film language: ")

    movies["Title"].append(title)
    movies["Director"].append(director)
    movies["Release date"].append(release_date)
    movies["Genre"].append(genre)
    movies["Language"].append(language)
    print("Film added successfully!\n")
    
def update_movie():
    update_info = input("Enter the list (Title, Director, Release date, Genre, Language) you want to update: ")
    if update_info in movies:
        key_info = int(input("Enter the key index you want to update: "))
        update_value = input (f"Enter the new value for {update_info}: ")
        movies[update_info][key_info] = update_value
    else:
        print("No data record in dictionary")
    
    return " "
    
def delete_movie():
    title_to_delete = input("Enter the title of the movie to delete: ")
    if title_to_delete in movies ["Title"]:
        index = movies["Title"].index(title_to_delete)

        for key in movies:
            movies[key].pop(index)
        print(f"'{title_to_delete}' has been deleted.")

    else:
        print(f"No movie found with the title '{title_to_delete}'.")
    
def search_movie(search_list):
    search_term = input("Enter the movie title to search: ")
    if search_term in movies["Title"]:
        index = movies["Title"].index(search_term)
        print("\nSearch Results:")
        print(f"Title: {movies['Title'][index]}")
        print(f"Director: {movies['Director'][index]}")
        print(f"Release Date: {movies['Release date'][index]}")
        print(f"Genre: {movies['Genre'][index]}")
        print(f"Language: {movies['Language'][index]}")
    else:
        print("No movies found.")
        
# Main program loop
while True:
    os.system('cls')
    print("Student Information Records")
    print("1. List All")
    print("2. Add")
    print("3. Update")
    print("4. Delete")
    print("5. Search")
    print("6. Exit")

    choice = int (input("Enter your choice: "))

    if choice == 6:
        break

    match choice: 
        case 1:
            os.system('cls')
            print(list_all_movies())
            input ("Press enter to back main menu")

        case 2: 
            os.system('cls')
            range_of_dictionary = int(input("How many movie(s) information you want to add: "))
            add_movie(range_of_dictionary)
            input("Press enter to back to main menu")

        case 3:
            os.system('cls')
            print (update_movie())
            input ("Press enter to back main menu")

        case 4:
            os.system('cls')
            print (delete_movie())
            input ("Press enter to back main menu")

        case 5:
            os.system('cls')
            print("Follow the format (Title, Director, Release Date, Genre, Lang) ")
            search_input = input("Enter the list you want to search in the dictionary: ")
            print(search_movie(search_input))
            input("Press enter to continue")

        case 6:
            print ("Invalid choice.")