import math
hour_for_exam = int(input())
minutes_for_exam = int(input())
hour_we_arrive = int(input())
minutes_we_arrive = int(input())

state = ""
state2 = ""
result = 0
result_hr = 0



ttl_minutes_exam = (hour_for_exam * 60) + minutes_for_exam
ttl_minutes_arrive = (hour_we_arrive * 60) + minutes_we_arrive

if ttl_minutes_arrive > ttl_minutes_exam:
    state = "Late"
    state2 = "after"
    result = abs(ttl_minutes_exam - ttl_minutes_arrive)
elif ttl_minutes_arrive == ttl_minutes_exam or ((ttl_minutes_exam - ttl_minutes_arrive) <= 30):
    state = "On time"
    state2 = "before"
    result = ttl_minutes_exam - ttl_minutes_arrive
elif ((ttl_minutes_exam - ttl_minutes_arrive) > 30):
    state = "Early"
    state2 = "before"
    result = ttl_minutes_exam - ttl_minutes_arrive

if result > 60:
    result_hr = result / 60
    result = result % 60
    print(f'{state} {math.floor(result_hr)}:{result:02d} hours {state2} the start')
elif result == 60:
    result = 1
    print(f'{state} {result} 00 hours {state2} the start')
else:
    print(f'{state} {result} minutes {state2} the start')
