

def print_current(data: dict, metric: bool):

    #print("{}, {}, {}".format(data["area"], data["region"], data["country"]))
    print("{}, {}".format(data["area"], data["region"]))
    print("Description: \t\033[38;5;226m{}\033[0m".format(data["description"]))
    print("Temperature: \t\033[38;5;40m{}\033[0m °{}".format(data["temperature"], "C" if metric else "F"))
    # TODO format so it is under 80 char
    print("Wind: \t\t{} {} \033[38;5;202m{}\033[0m {}".format(data["winddeg"], data["windpoint"], data["windspeed"], "kt" if metric else "mph"))
    # TODO add precipitation colour
    print("Percipitation: \t{} {}".format(data["precipitation"], "mm" if metric else "in"))
    print("Humidity: \t{}%".format(data["humidity"]))
    print("Visibility: \t{} {}".format(data["visibility"], "km" if metric else "mi"))


def print_astronomy(data: dict, use_icons: bool):
    print("{}, {}".format(data["area"], data["region"]))
    print("Moon Phase: \t\t\033[34m{}\033[0m {}".format(data["phase"], data["phase_emoji"]))
    print("Moon Illumination: \t{}".format(data["illumination"]))
    print("Sun Rise: \t\t\033[33m{}\033[0m".format(data["sunrise"]))
    print("Sun Set: \t\t\033[33m{}\033[0m".format(data["sunset"]))
