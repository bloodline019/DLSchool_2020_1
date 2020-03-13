# assert B == [5, 6, 15, 29]

def cumsum_and_erase(A, erase=1):
    for i in range(1, len(A)):
        A[i] = A[i] + A[i - 1]
    B = list(filter(lambda x: x != erase, A))
    return B


A = [5, 1, 4, 5, 14]
B = cumsum_and_erase(A, erase=10)
print(B)
