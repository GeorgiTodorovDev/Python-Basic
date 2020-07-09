pages_num = int(input())
pages_he_read_for_hr = int(input())
days_he_have_to_read_the_book = int(input())

total_time_for_reading = pages_num / pages_he_read_for_hr
result = total_time_for_reading / days_he_have_to_read_the_book

print(result)