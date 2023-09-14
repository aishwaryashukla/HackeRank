import pandas as pd
from mftool import Mftool

import pprint
pp = pprint.PrettyPrinter(indent=4)

mf = Mftool()
scheme_codes = mf.get_scheme_codes()

print((scheme_codes))
nav_data = mf.get_scheme_historical_nav_for_dates('120823', '01-01-2023', '30-08-2023')
# pp.pprint(nav_data['data'])
#
def get_best_return(nava_data):
    average_returns = {}
    for d in nava_data:

        day = d['date'][:2]
        # day = row['weekday']

        close_price = float(d['nav'])
        if day in average_returns:
            average_returns[day].append(close_price)
        else:
            average_returns[day] = [close_price]

    # Calculate the mean returns for each day
    for day, prices in average_returns.items():
        average_returns[day] = sum(prices) / len(prices)
        # pp.pprint(f'day = {day} and sum(prices) = {sum(prices)} and len(prices) = {len(prices)} {average_returns[day]} \n')

    # Find the day with the highest average returns
    best_day = min(average_returns, key=average_returns.get)
    pp.pprint(sorted(average_returns.items(),key=lambda x:x[1]))
    pp.pprint(sorted(average_returns.items()))
    return best_day

print(get_best_return(nava_data=nav_data['data']))