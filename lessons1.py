import random

if __name__ == '__main__':

    # l = int(input())
    #
    #
    # def rnd():
    #     for i in range(5, 95):
    #         if i % 5 == 0 or i % 7 == 0:
    #             if random.choice((True, False)):
    #                 l.append(i)
    #     random.shuffle(l)
    #     print(*l)
    #
    #
    # rnd()

    n = int(input())
    k = 0
    a = []
    for i in range(n):
        a.append(int(input()))

        for i in range(n):
            if a[i] % 3 == 0:
                k = k + 1
                print(k)