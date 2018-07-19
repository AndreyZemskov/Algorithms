N = 5
votes = {}
for i in range(N):
    name = input()
    if name in votes:
        votes[name] += 1
    else:
        votes[name] = 1

A = list(votes.items())
print(A)