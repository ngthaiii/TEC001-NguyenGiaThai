import re
def find_top5():
    text = input("Enter a text:").lower()
    words = re.findall(r"\b\w+\b", text)
    regular = {}
    for word in words:
        if word in regular:
            regular[word] += 1
        else:
            regular[word] = 1
    sort_regular = sorted(regular.items(), key=lambda x: x[1], reverse=True)
    top5 = dict(sort_regular[:5])
    total = len(words)
    sum_top5 = sum(top5.values())
    if total == 0:
        proportion = 0
    else:
        proportion = (sum_top5 / total) *100
    print(f"Top 5 frequent words:", top5)
    print(f"Total number of words: {total}.")
    print(f"Proportion of 5 most common words: {sum_top5} / {total}= {proportion:.2f}%.")
find_top5()