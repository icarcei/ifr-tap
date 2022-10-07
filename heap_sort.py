

def heapify(arr, N, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < N and arr[largest] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < N and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, N, largest)


def heapsort(s):
    sl = len(s)

    # heapify
    for i in range(int(sl/2)-1, -1, -1):
        heapify(s, sl, i)
    # sort
    for i in range(sl-1, 0, -1):
        s[i], s[0] = s[0], s[i]
        heapify(s, i, 0)


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    heapsort(arr)
    print("Vectorul sortat este:")
    [print(f"{arr[i]} ") for i in range(len(arr))]
