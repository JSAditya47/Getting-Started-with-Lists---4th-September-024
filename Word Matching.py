print("\033c")

def match_words(words):
    cnt = 0
    lst = []
    
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            cnt = cnt + 1
            lst.append(word)
            
    print("List of Words with First and Last Character Same", lst)
    return cnt
li = ["abc", "cfc", "xyz", "aba", "1221", "nahian", "narfan", "aditya"]
count = match_words(li)
print(f"Number of Words Having First and Last Character Same: {count}")