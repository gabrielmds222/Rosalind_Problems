start = 4119
final = 8643

result = sum(
    [x for x in range(start, final + 1) if x % 2 != 0]
)

print (result)