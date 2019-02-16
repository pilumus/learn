import random

def random_market():
    companies = []
    for j in range (0,10):
        report = []
        for i in range (0,6):
            digit = random.randint (-100, 500)
            report.append (digit)
        companies.append(report)
    return companies

def trend(companies):
    """companies - list of reports"""
    main_rise = []
    main_base_rise = []
    for report in companies:
        rise = []
        base_rise = 0
        long = len (report)
        for i in range (long):
            try:
                j = i + 1
                s = report [j] - report [i]
                rise.append (s)
                base_rise = base_rise + s
            except IndexError:
                break
        main_rise.append(rise)
        main_base_rise
    return main_rise, main_base_rise

def moving_average(report):
    """report - list of digits"""
    ma = []
    up = 0
    down = 0
    for i in report:
        up = up + i
        down = down + 1
        seed = up / down
        ma.append (seed)
    return ma
