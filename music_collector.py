### MUSIC COLLECTOR

def data_import(file_name="text_albums_data.txt"):
    with open(file_name, "r") as f:
        contents = f.readlines()
        lst = [x.strip().split(",") for x in contents]
        #print(lst)
        return lst


def display_menu():
    operations = {"View all albums:": 1, "Search by genre:": 2, "Search by artist:": 3, 
                  "Search by time range:": 4, "Show the shortest album:": 5, "Show the longest album:": 6,
                  "Show your library statistics:": 7}
    length = 70
    len_deli = 67
    sep = "|"
    dash_line = ("|" + "-" * (len_deli+2) + "|")
    print(dash_line)
    #print(f"{sep:<{length}}{title:^{length}}{sep:>{length}}")
    print(sep, "MUSIC COLLECTOR".center(len_deli), sep)
    print(dash_line)
    print("|", "Select operation by typing the corresponding number".center(len_deli), "|")
    print(dash_line)
    for key, value in operations.items():
        # string = key + ":" + str(value)
        print("|", key.ljust(len_deli-2), (str(value)), "|")
    print(dash_line)


def main():
    # user_choice = input()
    albums_list = data_import()
    show_all(albums_list)


def show_all(data):
    for sublist in data:
        print(" - ".join(sublist))


def search_by_genre():
    albums_list = data_import()
    genres = [x[-2] for x in albums_list]
    genres = set(genres)
    print(f"Your library includes following genres: {', '.join(genres)}")
    user_genre = input("Type in the genre you want to search for: ")
    genre_selection = []
    for i in range(len(albums_list)):
        if albums_list[i][-2] == user_genre:
            genre_selection.append(albums_list[i])
    print(genre_selection)

def exit_or_menu():
    pass
    


#data_import()
#display_menu()
search_by_genre()

