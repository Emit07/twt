
def deg_to_arrow(deg: int):
    if deg >= 0 and deg < 23:
        return chr(0xf55c)
    elif deg > 22 and deg < 69:
        return chr(0xf55b)
    elif deg > 68 and deg < 112:
        return chr(0xf553)
    elif deg > 111 and deg < 159:
        return chr(0xf542)
    elif deg > 158 and deg < 202:
        return chr(0xf544)
    elif deg > 201 and deg < 249:
        return chr(0xf541)
    elif deg > 248 and deg < 292:
        return chr(0xf54c)
    elif deg > 291 and deg < 339:
        return chr(0xf55a)
    elif deg > 338 and deg < 361:
        return chr(0xf55c)


def phase_to_emoji(phase: str):
    if phase == "New":
        return "🌑"
    elif phase == "Waxing Crescent":
        return "🌒"
    elif phase == "First Quarter":
        return "🌓"
    elif phase == "Waxing Gibbous":
        return "🌔"
    elif phase == "Full":
        return "🌕"
    elif phase == "Waning Gibbous":
        return "🌖"
    elif phase == "Third Quarter":
        return "🌗"
    elif phase == "Waning Crescent":
        return "🌘"
    else:
        return "🌙"


def average_humidity(hourly: list) -> int:
    tot_humidity = 0
    for hour in hourly:
        tot_humidity += int(hour["humidity"])

    return int(tot_humidity / len(hourly))


def average_percip_chance(hourly: list):
    average_percip = 0

    for hour in hourly:
        average_percip += int(hour["chanceofrain"])

    return int(average_percip / len(hourly))


def compile_percip(hourly: list):
    percip = 0
    for hour in hourly:
        percip += float(hour["precipMM"])

    return percip


