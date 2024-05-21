req_hours = int(input())
req_minutes = int(input()) + req_hours * 60
estimated_time = int(input())

total_min = req_minutes + estimated_time

result_hours = int(total_min / 60)
result_minutes = total_min - result_hours * 60

if result_hours % 24 < 10 and result_minutes < 10:
    print(f'0{result_hours % 24}:0{result_minutes}')
elif result_hours % 24 > 10 > result_minutes:
    print(f'{result_hours % 24}:0{result_minutes}')
elif result_hours % 24 < 10 < result_minutes:
    print(f'0{result_hours % 24}:{result_minutes}')
else:
    print(f'{result_hours % 24}:{result_minutes}')
