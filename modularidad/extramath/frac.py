def gcd(a: int, b: int) -> int:
    """Calculate common divisor through Euclid's algorithm"""
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """Least common multiple Euclid's algorithm"""
    return a * b // gcd(a, b)
