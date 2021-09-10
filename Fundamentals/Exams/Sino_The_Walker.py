import datetime

start_time = [int(x) for x in input().split(':')]
start_time = datetime.datetime(2021, 7, 1, start_time[0], start_time[1], start_time[2])
added_time = int(input()) * int(input())
start_time += datetime.timedelta(0, added_time)
print(f'Time Arrival: {start_time.time()}')
