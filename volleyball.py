import math

year = str(input())
holidays = int(input())
weekends = int(input())

saturdays_sofia = 48 - weekends
saturdays_games_sofia = saturdays_sofia * 3 / 4
holidays_games_sofia = holidays * 2 / 3
sundays_games_home = weekends
ttl_games = saturdays_games_sofia + sundays_games_home + holidays_games_sofia

if year == 'leap':
    ttl_games += ttl_games * 0.15
    print(math.floor(ttl_games))
else:
    print(math.floor(ttl_games))