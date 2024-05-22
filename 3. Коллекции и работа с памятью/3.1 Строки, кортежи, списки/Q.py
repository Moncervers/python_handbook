phrase = ''.join(input().lower().split())
if phrase == phrase[::-1]:
    print('YES')
else:
    print('NO')