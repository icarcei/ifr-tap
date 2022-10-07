
def insertie(m):
    for i in range(1, len(m)):
        sus = m[i]
        j = i - 1
        while j >= 0 and m[j] > sus:
            m[j+1] = m[j]
            j -= 1
        m[j+1] = sus
    return m


def sortp(v):
    l = []
    nr_pak = 10
    for i in range(nr_pak):
        l.append([])

    for j in v:
        idx = int(nr_pak * j)
        l[idx].append(j)

    for i in range(nr_pak):
        l[i] = insertie(l[i])

    n = 0
    for i in range(nr_pak):
        for j in range(len(l[i])):
            v[n] = l[i][j]
            n += 1
    return v


if __name__ == '__main__':
    v = [0.897, 0.565, 0.656,
         0.1234, 0.665, 0.3434]
    print(f"Sorted Array is: {sortp(v)}")
