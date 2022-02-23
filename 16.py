def is_possible(teams, T, k):
    sum = 0
    for i in range(len(teams)):
        sum += min(T, teams[i])

    return (sum >= (T * k))

def countOfTeams(teams_list, N, K):
    lb = 0
    ub = 10000000000000
    while (lb <= ub):
        mid = lb + (ub - lb) // 2
        if (is_possible(teams_list, mid, K)):
            if (is_possible(teams_list, mid + 1, K) == False):
                return mid

            else:
                lb = mid + 1
        else:
            ub = mid - 1
    return 0

for i in range(int(input())):
    N, K = map(int, input().split())
    arr = [int(i) for i in input().split()]
    print(countOfTeams(arr, N, K))
