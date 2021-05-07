def stat(strg):
    times = strg.split(', ')
    seconds = [to_seconds(x) for x in times if to_seconds(x) is not None]
    if len(seconds) > 0:
        return f"Range: {to_hms(_range(seconds))} Average: {to_hms(mean(seconds))} Median: {to_hms(median(seconds))}"
    else:
        return ""


def median(l):
    l.sort()
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    else:
        return (l[len(l) // 2 - 1] + l[len(l) // 2]) // 2


def _range(l):
    return max(l) - min(l)


def mean(l):
    return sum(l) // len(l)


def to_seconds(s):
    if s:
        hms = list(map(int, s.split('|')))
        return hms[0] * 3600 + hms[1] * 60 + hms[2]


def to_hms(sec):
    hours = sec // 3600
    minutes = (sec - hours * 3600) // 60
    seconds = sec - hours * 3600 - minutes * 60
    return f"{hours:02}|{minutes:02}|{seconds:02}"
