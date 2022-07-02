import argparse
import os
from weather_data import weather
from parse import parse_current, parse_astronomy
from cli import print_current, print_astronomy

def current(location: str, use_metric: bool=True):
    result = weather(location)

    if result is not None:
        parsed = parse_current(result, use_metric)
        print_current(parsed, use_metric)
    else:
        print("Error")


def astronomy(location: str, use_icons: bool=True):
    result = weather(location)
    
    if result is not None:
        parsed = parse_astronomy(result)
        print_astronomy(parsed, use_icons)
    else:
        print("Error")


def graph(location: str, use_metric: bool=True):
    os.system("curl v2d.wttr.in/{}{}".format(location, "?m" if use_metric else ""))


def oneline(location: str, use_metric: bool=True):
    result = weather(location)

    if result is not None:
        if not use_metric:
            print("{} °{}".format(result["current_condition"][0]["temp_F"], "F"))
        else:
            print("{} °{}".format(result["current_condition"][0]["temp_C"], "C"))
    else:
        print("Error")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Weather toolkit in the Terminal")
    parser.add_argument("information", choices=["current", "astronomy", "graph"], type=str, help="what information is retrieved")
    parser.add_argument("--imperial", "-f", default=False, action="store_true", help="use fahrenheit")
    parser.add_argument("--icons", "-o", default=True, action="store_false", help="use icons and/or emojis")
    parser.add_argument("--quiet", "-q", default=False, action="store_true", help="returns only the temperature")
    parser.add_argument("location", default="", nargs="?", const=None, type=str, help="the location target of the weather")
    args = parser.parse_args()

    if args.information == "current":
        if args.quiet:
            use_metric = False if args.imperial else True
            oneline(args.location, use_metric) 
        else:
            use_metric = False if args.imperial else True
            current(args.location, use_metric)
    elif args.information == "astronomy":
        astronomy(args.location, args.icons)

    elif args.information == "graph":
        use_metric = False if args.imperial else True
        graph(args.location, use_metric)
