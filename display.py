import os


def display_menu(stats):
    os.system("clear")
    operations = {"View all albums:": 1, "Search by genre:": 2, "Search by artist:": 3,
                  "Search by time range:": 4, "Show the shortest album:": 5, "Show the longest album:": 6,
                  "Show your library statistics:": 7, "Add new album": 8, "Edit existing album": 9, "Exit Music Collector": 10}
    len_deli = 106
    sep = "\u2592"
    dash_line = ("\u2592" + "\u2592" * (len_deli+2) + "\u2592")
    print(dash_line)
    print(sep, "\u266a MUSIC COLLECTOR \u266a".center(len_deli), sep)
    print(dash_line)
    print("\u2592", "Select operation by typing the corresponding number".center(len_deli), "\u2592")
    print(dash_line)
    check_decor1 = "\u2592 "
    for key, value in operations.items():
        print(f"{sep} {check_decor1 * 10} {key} {'.' * (76 - len(key))} {str(value):<{2}} {sep*6}")
    print(dash_line)
    stats_names = ["total albums: ", "total time: ", "all artists: ", "all grenres: "]
    stats_string = ""
    for i in range(len(stats_names)):
        stats_string += "\u2592 " + stats_names[i] + str(stats[i]) + " \u2592"
    print("\u2592", stats_string.center(len_deli), "\u2592 ")
    print(dash_line)


def display_choice(choice):
    os.system("clear")
    len_deli = 106
    choice = [[str(x).strip() for x in l] for l in choice]
    dash = "\u2592" + '\u2592' * 108 + "\u2592"
    print(dash)
    print('\u2592{:>3s}\u2592{:^25s}\u2592{:^35s}\u2592{:^10s}\u2592{:^20s}\u2592{:^10s}\u2592'.format("No", "Artist",
          "Album name", "Year", "Genre", "Time"))
    print(dash)
    for i in range(len(choice)):
        print('\u2592{:>3d}\u2592 {:<24s}\u2592 {:<34s}\u2592{:^10s}\u2592{:^20s}\u2592{:^10s}\u2592'.format((i+1), choice[i][0],
              choice[i][1], choice[i][2], choice[i][3], choice[i][4]))
    print(dash)
    print("\u2592", "press 'x' to go back to menu".center(len_deli), "\u2592")
    print(dash)


def display_for_edit(choice):
    os.system("clear")
    len_deli = 106
    choice = [[str(x).strip() for x in l] for l in choice]
    dash = "\u2592" + '\u2592' * 108 + "\u2592"
    print(dash)
    print('\u2592{:>3s}\u2592{:^25s}\u2592{:^35s}\u2592{:^10s}\u2592{:^20s}\u2592{:^10s}\u2592'.format("No", "Artist",
          "Album name", "Year", "Genre", "Time"))
    print(dash)
    print("\u2592", "Type in the number of the album you want to edit.".center(len_deli), "\u2592")
    print(dash)
    for i in range(len(choice)):
        print('\u2592{:>3d}\u2592 {:<24s}\u2592 {:<34s}\u2592{:^10s}\u2592{:^20s}\u2592{:^10s}\u2592'.format((i+1), choice[i][0],
              choice[i][1], choice[i][2], choice[i][3], choice[i][4]))
    print(dash)
    print(dash)


def display_no_data(choice):
    os.system("clear")
    len_deli = 102
    dash = "\u2592" + '\u2592' * 104 + "\u2592"
    print(dash)
    print('\u2592{:^25s}\u2592{:^35s}\u2592{:^10s}\u2592{:^20s}\u2592{:^10s}\u2592'.format("Artist",
          "Album name", "Year", "Genre", "Time"))
    print(dash)
    print("\u2592", choice[1].center(len_deli), "\u2592")
    print(dash)
    print("\u2592", "press 'x' to go back to menu".center(len_deli), "\u2592")
    print(dash)


def display_stats(choice_result):
    os.system("clear")
    digit_stats = choice_result[1:5]
    longest = choice_result[5]
    shortest = choice_result[6]
    oldest = choice_result[7]
    youngest = choice_result[8]
    len_deli = 106
    bullet = "\u2023"
    sep = "\u2592"
    dash = "\u2592" + '\u2592' * 108 + "\u2592"
    print(dash)
    print(sep, "\u266a LIBRARY STATISTICS \u266a".center(len_deli), sep)
    print(dash)
    digit_list = ["Album count: ", "total time: ", "all artists: ", "all grenres: "]
    digit_string = ""
    for i in range(len(digit_list)):
        digit_string += "\u2592 " + digit_list[i] + str(digit_stats[i]) + " \u2592"
    print("\u2592", digit_string.center(len_deli), "\u2592")
    print(dash)
    print(f"{sep} {'The longest album(s):':<{57}}{sep:>{51}}")
    for i in longest:
        print(f"{sep} {bullet} {' - '.join(i):<{57}}{sep:>{49}}")
    print(f"{sep} {' '.center(107)}{sep}")
    print(f"{sep} {'The shortest album(s):':<{57}}{sep:>{51}}")
    for i in shortest:
        print(f"{sep} {bullet} {' - '.join(i):<{57}}{sep:>{49}}")
    print(f"{sep} {' '.center(107)}{sep}")
    print(f"{sep} {'The oldest album(s):':<{57}}{sep:>{51}}")
    for i in oldest:
        print(f"{sep} {bullet} {' - '.join(i):<{57}}{sep:>{49}}")
    print(f"{sep} {' '.center(107)}{sep}")
    print(f"{sep} {'The youngest album(s):':<{57}}{sep:>{51}}")
    for i in youngest:
        print(f"{sep} {bullet} {' - '.join(i):<{57}}{sep:>{49}}")
    print(dash)
    print("\u2592", "press 'x' to go back to menu".center(len_deli), "\u2592")
    print(dash)


def display_middle_stage(set_of_some_things):
    os.system("clear")
    len_deli = 106
    sep = "\u2592"
    dash_line = ("\u2592" + "\u2592" * (len_deli+2) + "\u2592")
    print(dash_line)
    print(sep, "\u266a MUSIC COLLECTOR \u266a".center(len_deli), sep)
    print(dash_line)
    print("\u2592", "Search for one of the following:".center(len_deli), "\u2592")
    print(dash_line)
    for i in range(len(set_of_some_things)):
        print("\u2592", set_of_some_things[i].center(len_deli-5), "\u2592"*6)
    print(dash_line)
    print("\u2592", "press 'x' to go back to menu".center(len_deli), "\u2592")
    print(dash_line)


def display_time_input():
    os.system("clear")
    len_deli = 106
    decor1 = " \u2592"
    decor2 = "\u2592 "
    sep = "\u2592"
    dash_line = ("\u2592" + "\u2592" * (len_deli+2) + "\u2592")
    print(dash_line)
    print(sep, "\u266a MUSIC COLLECTOR \u266a".center(len_deli), sep)
    print(dash_line)
    print("\u2592", "Type in minimum value and enter, then max value and enter".center(len_deli), "\u2592")
    print(dash_line)
    for i in range(3):
        print(decor1*55)
        print(decor2*55)
    print(dash_line)
    

def display_add_album(single_input):
    os.system("clear")
    len_deli = 106
    sep = "\u2592"
    decor1 = " \u2592"
    decor2 = "\u2592 "
    dash_line = ("\u2592" + "\u2592" * (len_deli+2) + "\u2592")
    print(dash_line)
    print(sep, "\u266a MUSIC COLLECTOR \u266a".center(len_deli), sep)
    print(dash_line)
    print("\u2592", single_input.center(len_deli), "\u2592")
    print(dash_line)
    for i in range(3):
        print(decor1*55)
        print(decor2*55)
    print(dash_line)
    

def display_edit_album(single_input, album_to_edit):
    os.system("clear")
    len_deli = 106
    album_string = " - ".join(album_to_edit)
    sep = "\u2592"
    decor1 = " \u2592"
    decor2 = "\u2592 "
    dash_line = ("\u2592" + "\u2592" * (len_deli+2) + "\u2592")
    print(dash_line)
    print(sep, album_string.center(len_deli), sep)
    print(dash_line)
    print("\u2592", single_input.center(len_deli), "\u2592")
    print(dash_line)
    for i in range(3):
        print(decor1*55)
        print(decor2*55)
    print(dash_line)
    