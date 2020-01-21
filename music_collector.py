from display import display_menu
from display import display_choice

# MUSIC COLLECTOR


def data_import(file_name="text_albums_data.txt"):
    with open(file_name, "r") as f:
        contents = f.readlines()
        lst = [x.strip().split(",") for x in contents]
        return lst


def menu_choice():
    user_choice = input()
    operations = {1: show_all, 2: search_by_genre, 3: search_by_artist,
                  4: search_by_time_range, 5: find_shortest, 6: find_longest, 7: show_extended_statistics,
                  8: exit}
    if int(user_choice) in operations.keys():
        return operations[int(user_choice)]()


def main():
    display_menu(show_statistics())
    display_choice(menu_choice())
    # show_all()


def show_all():
    albums_list = data_import()
    for sublist in albums_list:
        print(" - ".join(sublist))


def search_by_genre():
    albums_list = data_import()
    genres = set_genres()
    print(f"Your library includes following genres: {', '.join(genres)}")
    user_genre = input("Type in the genre you want to search for: ").lower()
    genre_selection = []
    for i in range(len(albums_list)):
        if (albums_list[i][-2]).lower() == user_genre:
            genre_selection.append(albums_list[i])
    return genre_selection


def search_by_artist():
    albums_list = data_import()
    artists = set_artists()
    print(f"Your library includes following artists: {', '.join(artists)}")
    user_artist = input("Type an artist you want to search for: ").lower()
    artist_selection = []
    for i in range(len(albums_list)):
        if (albums_list[i][0]).lower() == user_artist:
            artist_selection.append(albums_list[i])
    return artist_selection


def time_convert():
    albums_list = data_import()
    for i in range(len(albums_list)):
        time_string = albums_list[i][-1]
        time_lst = time_string.split(":")
        time_in_seconds = int(time_lst[0]) * 60 + int(time_lst[1])
        albums_list[i].append(time_in_seconds)
    return albums_list


def search_by_time_range():
    albums_list = time_convert()
    result_lst = []
    try:
        time_input = int(input("Enter time range in minutes: "))
        time_in_sec = time_input * 60
        for e in albums_list:
            if time_in_sec >= e[5]:
                result_lst.append(e[:5])
    except ValueError:
        print("You have to enter only intiger type.")
        search_by_time_range()
    return result_lst


def check_for_equal_entries(source, match, i):
    result_lst = []
    for e in source:
        if e[i] == match[i]:
            result_lst.append(e[:5])
    return result_lst


def find_shortest():
    albums_list = time_convert()
    lst = sorted(albums_list, key=lambda x: x[-1])[0]
    return check_for_equal_entries(albums_list, lst, -1)


def find_longest():
    albums_list = time_convert()
    lst = sorted(albums_list, key=lambda x: x[-1], reverse=True)[0]
    return check_for_equal_entries(albums_list, lst, -1)


def find_oldest():
    albums_list = data_import()
    lst = sorted(albums_list, key=lambda x: int(x[-3]))[0]
    return check_for_equal_entries(albums_list, lst, 0)


def find_youngest():
    albums_list = data_import()
    lst = sorted(albums_list, key=lambda x: int(x[-3]), reverse=True)[0]
    return check_for_equal_entries(albums_list, lst, 0)


def set_artists():
    albums_list = data_import()
    artists = set()
    for e in albums_list:
        artists.add(e[0])
    return artists


def set_genres():
    albums_list = data_import()
    genres = set()
    for e in albums_list:
        genres.add(e[-2])
    return genres


def set_album_names():
    albums_list = data_import()
    set_album_names = set()
    for e in albums_list:
        set_album_names.add(e[0])
    return set_album_names


def count_time():
    total_time = 0
    albums_list = time_convert()
    for e in albums_list:
        total_time += e[-1]
    if total_time > 3600:
        hours = round(total_time / 3600)
        minutes = round(total_time % 3600 / 60)
        seconds = round(total_time % 3600 % 60)
    if len(str(seconds)) == 1:
        seconds = (str(seconds)).zfill(2)
    time_string = f"{hours}:{minutes}:{seconds}"
    return time_string


def show_statistics():
    album_count = len(set_album_names())
    total_time = count_time()
    total_genres = len(set_genres())
    total_artists = len(set_artists())
    result_lst = [album_count, total_time, total_artists, total_genres]
    return result_lst


def show_extended_statistics():
    album_count = len(set_album_names())
    total_time = count_time()
    total_genres = len(set_genres())
    total_artists = len(set_artists())
    longest = find_longest()
    shortest = find_shortest()
    oldest = find_oldest()
    youngest = find_youngest()
    result_lst = [album_count, total_time, total_artists, total_genres, longest, shortest, oldest, youngest]
    result_lst = [str(x) for x in result_lst]
    return result_lst


main()


# def find(what):
#     if what == "shortest":
#         i = -1
#         rev = False
#     if what == "longest":
#         i = -1
#         rev = True
#     if what == "oldest":
#         i = -4
#         rev = False
#     if what == "youngest":
#         i = -4
#         rev = True
#     source = time_convert()
#     result = sorted(source, key=lambda x: int(x[i]), reverse=rev)[0]
#     result_lst = []
#     for e in source:
#         if e[i] == result[i]:
#             result_lst.append(", ".join(e[:5]))
#     string = "; ".join(result_lst[:5])
#     return string


# def search_by_(what):
#     albums_list = data_import()
#     if what == "artist":
#         set_of_what = set_artists()
#     if what == "genre":
#         set_of_what = set_genres()
#     print(f"Your library includes following {what}s: {', '.join(set_of_what)}")
#     user_what = input(f"Type the {what} you want to search for: ")
#     what_selection = []
#     if what == "artist":
#         w = 0
#     if what == "genre":
#         w = -2
#     for i in range(len(albums_list)):
#         if albums_list[i][w] == user_what:
#             what_selection.append(albums_list[i])
#     what_string = ""
#     for sublist in what_selection:
#         what_string += " ".join(sublist) + "\n"
#     return what_string
