def passed(lst):
    approvedCount = 0
    totalApproved = 0
    for i in lst:
        if (i < 19):
            approvedCount += 1
            totalApproved += i
    if (approvedCount != 0):
        return round(totalApproved / approvedCount)
    else:
        return 'No pass scores registered.'