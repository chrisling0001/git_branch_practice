def add(x:int=0, y:int=0) -> int:
    return x + y

def add_array(arr:list) -> int:
    s = 0
    for a in arr:
        s += a
    return s

if __name__ == "__main__":
    # print(add(5, 42))
    arr = [10, 20, 30]
    sum = add_array(arr)
    print(sum)