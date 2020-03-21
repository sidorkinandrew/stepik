def cumsum_and_erase(A, erase=1):
    cumsum=0
    B = []
    for idx,value in enumerate(A):
        cumsum += value
        if cumsum==erase:
            continue
        B.append(cumsum)
    return B