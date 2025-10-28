def is_distribution_possible(x, y, z, K):
    total = x + y + z + K
    if total % 3 != 0:
        return 0  # Cannot equally distribute
    F = total // 3
    if F >= max(x, y, z):
        return 1
    return 0

# Example usage
x, y, z, K = map(int, input().split())
print(is_distribution_possible(x, y, z, K))
