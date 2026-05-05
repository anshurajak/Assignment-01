def min_operations_to_equal(A, K):
    remainder = A[0] % K

    # Check feasibility
    for x in A:
        if x % K != remainder:
            return -1

    # Normalize
    normalized = [(x - remainder) // K for x in A]
    normalized.sort()

    # Median
    median = normalized[len(A)//2]

    # Calculate operations
    operations = sum(abs(x - median) for x in normalized)

    return operations


# Input
N = int(input())
A = list(map(int, input().split()))
K = int(input())

print(min_operations_to_equal(A, K))