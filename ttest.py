def add(x, y):
    return x + y

def add_arr(arr:list) -> int:
    sum = 0
    for a in arr:
        sum += a
    return sum

if __name__ == "__main__":
    # print(add(5, 42))
    arr = [10, 20, 30]
    sum = add_arr(arr)
    print(sum)