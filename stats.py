def count_words(content:str):
    return len(content.split())

def count_char(content:str):
    counted_chars = {}
    lower_content = content.lower()
    for char in lower_content:
        if char not in counted_chars:
            counted_chars[char] = 1
        else:
            counted_chars[char] += 1
    return counted_chars

def sort_on(items):
    return items["count"]

def sort_counted_chars(counted_chars:dict):
    # restructure dict into list
    # [{"char": "a", "count": 7}]
    char_stats = []
    
    for i in counted_chars:
        entry = {
            "char": i,
            "count": counted_chars[i]
        }
        char_stats.append(entry)
    
    char_stats.sort(reverse=True, key=sort_on)
    return char_stats
