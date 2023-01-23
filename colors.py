colors = [1, 2, 3, 4]

def is_valid(answer):
    return all(color in answer for color in colors)

valid_sum = 0
for a in colors:
    for b in colors:
        for c in colors:
            for d in colors:
                for e in colors:
                    for f in colors:
                        if is_valid(answer=[a, b, c, d, e, f]):
                            valid_sum += 1

print(valid_sum)