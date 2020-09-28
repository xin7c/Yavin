# 传入参数是 [1,2,3,4,5,6,7,8]
# 请补充剩余代码，在控制台输出一个元组：(1,2,3,4)


def query():
    def inner(lst):
        print(tuple(lst[0:4]))
    return inner


first_val = query()

first_val([1, 2, 3, 4, 5, 6, 7, 8])
