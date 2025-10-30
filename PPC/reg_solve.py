s = open("regexes.txt", 'r').readlines()

for k in range(31):
    st = set()
    for j in range(len(s)):
        s[j] = s[j].strip()
        m = list(s[j].split("]"))
        tmp = m[k].strip("[")
        if (j == 0):
            st = set(list(tmp))
        else:
            st = st.intersection(set(list(tmp)))
    print(list(st)[0], end='')
