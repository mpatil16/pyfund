def tuples_hash(n, integer_list):
    """To accept n numbers, store it in tuple and print hash value of the tuple"""
    t = tuple(integer_list)
    print hash(t)


if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    tuples_hash(n, integer_list)