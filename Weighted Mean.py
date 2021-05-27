n = int(input().strip())

vals = list(map(int, input().rstrip().split()))

weights = list(map(int, input().rstrip().split()))
print(round(sum([vals[x]*weights[x] for x in range(len(vals))]) / sum(weights), 1))

