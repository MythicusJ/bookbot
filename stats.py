def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    counts = {}
    for ch in text.lower():
        if ch not in counts: counts[ch] = 0
        counts[ch] += 1
    return counts


def char_counts_sorted(char_dict):
    rows = []
    for ch, n in char_dict.items():
        rows.append({"char": ch, "num": n})
    def by_num(item):
        return item["num"]
    rows.sort(key=by_num, reverse=True)
    return rows
