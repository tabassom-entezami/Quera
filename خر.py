n, m = list(map(int, input().split()))
responses = {}
for _ in range(n):
    q, a = input().split()
    responses[q] = a
question = input()
for word in question.split():
    if word in responses:
        print(responses[word], end=' ')
    print('kachal!', end=' ')
