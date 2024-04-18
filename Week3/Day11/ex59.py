if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
scores = sorted(arr, reverse = True)
runner_up_score = None
for score in scores:
    if score < max(scores):
        runner_up_score = score
        break
print(score)
