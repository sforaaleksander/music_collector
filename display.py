import os


def display_menu(stats):
    os.system("clear")
    operations = {"View all albums:": 1, "Search by genre:": 2, "Search by artist:": 3,
                  "Search by time range:": 4, "Show the shortest album:": 5, "Show the longest album:": 6,
                  "Show your library statistics:": 7, "Exit Music Collector": 8}
    len_deli = 102
    sep = "\u2592"
    dash_line = ("\u2592" + "\u2592" * (len_deli+2) + "\u2592")
    print(dash_line)
    # print(f"{sep:<{length}}{title:^{length}}{sep:>{length}}")
    print(sep, "\u266a MUSIC COLLECTOR \u266a".center(len_deli), sep)
    print(dash_line)
    print("\u2592", "Select operation by typing the corresponding number".center(len_deli), "\u2592")
    print(dash_line)
    check_decor1 = "\u2592 "
    # check_decor2 = " \u2592"
    for key, value in operations.items():
        print("\u2592", check_decor1 * 10, key, "." * (73 - len(key)), (str(value)), "\u2592"*6)
    print(dash_line)
    stats_names = ["total albums: ", "total time: ", "all artists: ", "all grenres: "]
    stats_string = ""
    for i in range(len(stats_names)):
        stats_string += "\u2592 " + stats_names[i] + str(stats[i]) + " \u2592"
    print("\u2592", stats_string.center(102), "\u2592 ")
    print(dash_line)


def display_choice(choice):
    os.system("clear")
    len_deli = 102
    choice = [[str(x).strip() for x in l] for l in choice]
    dash = "\u2592" + '\u2592' * 104 + "\u2592"
    print(dash)
    print('\u2592{:^25s}\u2592{:^35s}\u2592{:^10s}\u2592{:^20s}\u2592{:^10s}\u2592'.format("Artist",
          "Album name", "Year", "Genre", "Time"))
    print(dash)
    for i in range(len(choice)):
        print('\u2592{:<25s}\u2592{:<35s}\u2592{:^10s}\u2592{:^20s}\u2592{:^10s}\u2592'.format(choice[i][0],
              choice[i][1], choice[i][2], choice[i][3], choice[i][4]))
    print(dash)
    print("\u2592", "press 'x' to go back to menu".center(len_deli), "\u2592")
    print(dash)


# TO DO:
# def display_stats(stats):
#     os.system("clear")
#     # stats = [[x.strip() for x in l] for l in stats]
#     dash = "\u2592" + '\u2592' * 104 + "\u2592"
#     print(dash)
#     print('\u2592{:^25s}\u2592{:^35s}\u2592{:^10s}\u2592{:^20s}\u2592{:^10s}\u2592'.format("Artist", "Album name",
#           "Year", "Genre", "Time"))
#     print(dash)
#     for i in range(len(stats)):
#         print('\u2592{:<25s}\u2592{:<35s}\u2592{:^10s}\u2592{:^20s}\u2592{:^10s}\u2592'.format(stats[i][0],
#               stats[i][1], stats[i][2], stats[i][3], stats[i][4]))
