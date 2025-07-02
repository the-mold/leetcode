def reverseWords(self, s: str) -> str:
    s_splitted = s.split(" ")

    res = []
    for i in range(len(s_splitted)-1, -1, -1):
        if s_splitted[i] == "":
            continue
        res.append(s_splitted[i])
    
    return " ".join(res)