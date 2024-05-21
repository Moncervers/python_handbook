children = int(input())
sweets = int(input())

print(int((sweets - (sweets % children)) / children))
print(sweets % children)