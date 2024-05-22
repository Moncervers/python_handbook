pages = []
for i in range(int(input())):
    pages.append(input())

request = input()
for page in pages:
    if request.lower() in page.lower():
        print(page)
