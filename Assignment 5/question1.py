def cachedfibonacci(int, dict={}):
    if int in dict:
        return dict[int]
    else:
        if int == 1 or int == 2:
            dict[int] = 1
        else:
            dict[int] = cachedfibonacci(int-1)+cachedfibonacci(int-2)
        return dict[int]
    return dict

if __name__ == "__main__":
    print(cachedfibonacci(100))

#question 1 done - Nov 28th 2020



