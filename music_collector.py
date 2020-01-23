import random
from display import display_menu
from display import display_choice
from display import display_stats
from display import display_no_data
from display import display_middle_stage
from display import display_time_input
from display import display_add_album
from display import display_edit_album
from display import display_for_edit
from display import display_recommendation

# MUSIC COLLECTOR


def data_import(file_name="text_albums_data.txt"):
    with open(file_name, "r") as f:
        contents = f.readlines()
        lst = [x.strip().split(",") for x in contents]
        return lst


def gather_user_info(for_what, album_to_edit=None):
    artist = "Type an artist: "
    album = "Type album's name: "
    year = "Type the year: "
    genre = "Type the genre: "
    time = "Type album's length: "
    lst = [artist, album, year, genre, time]
    full_album_info = []
    if for_what == "for_add":
        for i in range(len(lst)):
            display_add_album(lst[i])
            info = input()
            if i == 2:
                while not info.isdigit():
                    info = input()
            if i == 4:
                ls = info.split(":")
                while not ls[0].isdigit() or not ls[1].isdigit() or len(ls) != 2:
                    info = input()
                    ls = info.split(":")
            full_album_info.append(info)
        return full_album_info
    elif for_what == "for_edit":
        for i in range(len(lst)):
            display_edit_album(lst[i], album_to_edit)
            info = input()
            full_album_info.append(info)
        return full_album_info


def update_data(file_name="text_albums_data.txt"):
    with open(file_name, "a") as f:
        f.write(",".join(gather_user_info("for_add")) + "\n")
    main()


def edit_data(file_name="text_albums_data.txt"):
    albums_list = data_import()
    display_for_edit(show_all())
    user_input = input()
    while not user_input.isdigit():
        user_input = input()
    while int(user_input) not in range(len(show_all())+1):
        user_input = input()
    edited_entry = gather_user_info("for_edit", albums_list[int(user_input) - 1])
    albums_list[int(user_input) - 1] = edited_entry
    with open(file_name, "w") as f:
        for e in albums_list:
            f.write(",".join(e) + "\n")
    main()


def menu_choice():
    user_choice = input()
    while not user_choice.isdigit():
        user_choice = input()
    while int(user_choice) not in range(1, 11):
        user_choice = input()
    user_choice = int(user_choice)
    operations = {1: show_all, 2: search_by_genre, 3: search_by_artist,
                  4: search_by_time_range, 5: find_shortest, 6: find_longest,
                  7: show_extended_statistics, 8: update_data, 9: edit_data, 10: exit}
    return operations[int(user_choice)]()


def back_to_menu():
    back = input().lower()
    while back != "x":
        back = input().lower()
    main()


def chceck_choice_result(choice_result):
    if choice_result[0] == "statistics":
        display_stats(choice_result)
    elif choice_result[0] == "no_data":
        display_no_data(choice_result)
    elif choice_result[0] == "recommendation":
        display_recommendation(choice_result)
    else:
        display_choice(choice_result)


def main():

    display_menu(show_statistics())
    chceck_choice_result(menu_choice())
    back_to_menu()


def show_all():
    albums_list = data_import()
    result_lst = []
    for sublist in albums_list:
        result_lst.append(sublist)
    return result_lst


def search_by_genre():
    albums_list = data_import()
    genres = list(set_genres())
    display_middle_stage(genres)
    user_genre = input()
    genres_selection = []
    for i in range(len(albums_list)):
        if (albums_list[i][-2]).lower() == user_genre.lower():
            genres_selection.append(albums_list[i])
    if user_genre == "x" or user_genre == "X":
        main()
    if len(genres_selection) > 0:
        return genres_selection
    return ["no_data", "No data matching your criteria."]


def search_by_artist():
    albums_list = data_import()
    artists = list(set_artists())
    display_middle_stage(artists)
    user_artist = input()
    artist_selection = []
    for i in range(len(albums_list)):
        if (albums_list[i][0]).lower() == user_artist.lower():
            artist_selection.append(albums_list[i])
    if user_artist == "x" or user_artist == "X":
        main()
    if len(artist_selection) > 0:
        list_of_suggestions = recommendation(user_artist.lower())
        result = ["recommendation", artist_selection, list_of_suggestions]
        return result
    return ["no_data", "No data matching your criteria."]


def recommendation(artist):
    albums_list = data_import()
    genre_from_artist = ""
    for i in range(len(albums_list)):
        if artist.lower() == albums_list[i][0].lower():
            genre_from_artist = albums_list[i][-2]
    suggestions = []
    for i in range(len(albums_list)):
        if albums_list[i][-2].lower() == genre_from_artist.lower() and albums_list[i][0].lower() != artist:
            suggestions.append(albums_list[i])
    random.shuffle(suggestions)
    return suggestions[:3]


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
    display_time_input()
    time_min = input()
    while not time_min.isdigit():
        time_min = input()
    time_max = input()
    while not time_max.isdigit():
        time_max = input()
    time_min = int(time_min) * 60
    time_max = int(time_max) * 60
    for e in albums_list:
        if time_min <= e[5] <= time_max:
            result_lst.append(e[:5])
    if len(result_lst) > 0:
        return result_lst
    return ["no_data", "No data matching your criteria."]


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
        artists.add(e[0].strip().upper())
    return artists


def set_genres():
    albums_list = data_import()
    genres = set()
    for e in albums_list:
        genres.add(e[-2].strip().upper())
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
    result_lst = ["statistics", album_count, total_time,
                  total_artists, total_genres, longest, shortest, oldest, youngest]
    return result_lst


main()

# search_by_time_range()

# while not valid:
#     try:
#         # time_min = int(input()) * 60
#         time_min = input()
#         int(time_min)
#         time_min *= 60
#         valid = True
#     except ValueError:
#         time_min = input()
#         int(time_min)
#         time_min *= 60
# valid = False
# while not valid:
#     try:
#         time_max = int(input()) * 60
#         valid = True
#     except ValueError:
#         time_max = int(input()) * 60


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


# def search_by_genre():
#     albums_list = data_import()
#     genres = set_genres()
#     print(f"Your library includes following genres: {', '.join(genres)}")
#     user_genre = input("Type in the genre you want to search for: ").lower()
#     genre_selection = []
#     for i in range(len(albums_list)):
#         if (albums_list[i][-2]).lower() == user_genre:
#             genre_selection.append(albums_list[i])
#     if len(genre_selection) > 0:
#         return genre_selection
#     return ["no_data", "No data matching your criteria."]
