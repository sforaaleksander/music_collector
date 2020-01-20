# MUSIC COLLECTOR


def data_import(file_name="text_albums_data.txt"):
    with open(file_name, "r") as f:
        contents = f.readlines()
        lst = [x.strip().split(",") for x in contents]
        # print(lst)
        return lst


def display_menu():
    operations = {"View all albums:": 1, "Search by genre:": 2, "Search by artist:": 3, 
                  "Search by time range:": 4, "Show the shortest album:": 5, "Show the longest album:": 6,
                  "Show your library statistics:": 7}
    len_deli = 67
    sep = "|"
    dash_line = ("|" + "-" * (len_deli+2) + "|")
    print(dash_line)
    # print(f"{sep:<{length}}{title:^{length}}{sep:>{length}}")
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


<<<<<<< HEAD
=======
def search_by_artist():
    albums_list = data_import()
    artists = [x[0] for x in albums_list]
    artists = set(artists)
    print(f"Your library includes following artists: {', '.join(artists)}")
    user_artist = input("Type an artist you want to search for: ")
    artist_selection = []
    for i in range(len(albums_list)):
        if albums_list[i][0] == user_artist:
            artist_selection.append(albums_list[i])
    print(artist_selection)


def time_convert():
    albums_list = data_import()
    mod_time_albums_lst = albums_list
    for i in range(len(mod_time_albums_lst)):
        time_string = mod_time_albums_lst[i][-1]
        time_lst = time_string.split(":")
        time_in_seconds = int(time_lst[0]) * 60 + int(time_lst[1])        
        mod_time_albums_lst[i].append(time_in_seconds)
    return mod_time_albums_lst


def search_by_time_range():
    mod_time_albums = time_convert()
    try:
        time_input = int(input("Enter time range in minutes: "))
        time_in_sec = time_input * 60
        for e in mod_time_albums:
            if time_in_sec >= e[5]:
                print(" - ".join(e[:5]))
    except ValueError:
        print("You have to enter only intiger type.")
        search_by_time_range()
        

# print(time_convert())
search_by_time_range()


def exit_or_menu():
    pass


# data_import()
# display_menu()
# search_by_genre()
# search_by_artist()
# search_by_time_range()


>>>>>>> 1987d31f8b2e7560a3ccbfe24927f16dc6004293
def exit_or_menu():
    pass


# convert time to seconds, create copied list of albums
# with appended element 'time_in_seconds' to make sorting easy


def find_shortest():
    mod_time_albums_lst = time_convert()
    lst = sorted(mod_time_albums_lst, key=lambda x: x[-1])[0]
    lst = [str(x) for x in lst]
    string = ", ".join(lst[:-1:])
    return string


def find_longest():
    mod_time_albums_lst = time_convert()
    lst = sorted(mod_time_albums_lst, key=lambda x: x[-1], reverse=True)[0]
    lst = [str(x) for x in lst]
    string = ", ".join(lst[:-1:])
    return string


def find_oldest():
    albums_list = data_import()
    lst = sorted(albums_list, key=lambda x: int(x[-3]))[0]
    lst = [str(x) for x in lst]
    string = ", ".join(lst)
    return string


def find_youngest():
    albums_list = data_import()
    lst = sorted(albums_list, key=lambda x: int(x[-3]), reverse=True)[0]
    lst = [str(x) for x in lst]
    string = ", ".join(lst)
    return string


def set_artists():
    albums_list = data_import()
    artists = set()
    for e in albums_list:
        set.add(e[0])
    return artists


def set_genres():
    albums_list = data_import()
    generes = set()
    for e in albums_list:
        set.add(e[-2])
    return generes


def count_time():
    total_time = 0
    time_string = ""
    mod_time_albums_lst = time_convert()
    for e in mod_time_albums_lst:
        total_time += e[-1]
    if total_time > 3600:
        hours = total_time / 3600
        minutes = total_time  
        seconds = total_time % 3600
    return total_time


def show_statistics():
    albums_list = data_import()
    album_count = 0
    total_time = 0
    total_genres = 0
    total_artists = 0
    longest = find_longest()
    shortest = find_shortest()
    oldest = find_oldest()
    youngest = find_youngest()  


<<<<<<< HEAD
main()
#data_import()
#display_menu()
#search_by_genre()
time_convert()
print("___________________")
show_statistics()
print(count_time())
=======
# main()
# data_import()
# display_menu()
# search_by_genre()
# print(time_convert())
# print("___________________")
# show_statistics()
# print(count_time())
>>>>>>> 1987d31f8b2e7560a3ccbfe24927f16dc6004293
