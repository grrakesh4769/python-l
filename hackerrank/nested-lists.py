names = []
scores = []
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    names.append(name)
    scores.append(score)

rscore = sorted(list(set(scores)), None, None, False)
result = sorted([names[iscore[0]] for iscore in enumerate(scores) if iscore[1] == rscore[1]])
for rname in result:
    print rname
