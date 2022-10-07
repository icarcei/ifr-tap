from array import array


def sortare_numarare(ar):
    nr_elem = len(ar)
    qout = [0] * nr_elem
    count = [0] * 10
    for i in range(0, nr_elem):
        count[ar[i]] += 1
    for i in range(1, 10):
        count[i] = count[i] + count[i-1]

    i = nr_elem - 1
    while i >= 0:
        qout[count[ar[i]]-1] = ar[i]
        count[ar[i]] = count[ar[i]] - 1
        i -= 1
    for i in range(0, nr_elem):
        ar[i] = qout[i]


if __name__ == '__main__':
    lista = [1, 7, 2, 3, 9, 5, 4]
    sortare_numarare(lista)
    print(f"Stiva sortata este:\n{lista}")
