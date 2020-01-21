def display_menu(stats):
    operations = {"View all albums:": 1, "Search by genre:": 2, "Search by artist:": 3,
                  "Search by time range:": 4, "Show the shortest album:": 5, "Show the longest album:": 6,
                  "Show your library statistics:": 7, "Exit Music Collector": 8}
    len_deli = 102
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
    stats_names = ["total albums: ", "total time: ", "all artists: ", "all grenres: "]
    stats_string = ""
    for i in range(len(stats_names)):
        stats_string += "- " + stats_names[i] + str(stats[i]) + " -"
    print(stats_string)


def display_choice(choice):
    choice = [[x.strip() for x in l] for l in choice]
    dash = "|" + '-' * 104 + "|"
    print(dash)
    print('|{:^25s}|{:^35s}|{:^10s}|{:^20s}|{:^10s}|'.format("Artist", "Album name", "Year", "Genre", "Time"))
    print(dash)
    for i in range(len(choice)):
        print('|{:<25s}|{:<35s}|{:^10s}|{:^20s}|{:^10s}|'.format(choice[i][0], choice[i][1],
              choice[i][2], choice[i][3], choice[i][4]))


def display_stats(stats):
    # stats = [[x.strip() for x in l] for l in stats]
    dash = "|" + '-' * 104 + "|"
    print(dash)
    print('|{:^25s}|{:^35s}|{:^10s}|{:^20s}|{:^10s}|'.format("Artist", "Album name", "Year", "Genre", "Time"))
    print(dash)
    for i in range(len(stats)):
        print('|{:<25s}|{:<35s}|{:^10s}|{:^20s}|{:^10s}|'.format(stats[i][0], stats[i][1],
              stats[i][2], stats[i][3], stats[i][4]))
