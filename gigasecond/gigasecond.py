from datetime import timedelta
def add(moment):
    date = moment + timedelta(seconds = 10**9)
    return date
