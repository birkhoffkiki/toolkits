from multiprocessing import Pool


class EasyProcessing:
    def __init__(self, process_num):
        self.pool = Pool(process_num)

    def apply(self, func, args):
        results = self.pool.map(func, args)
        return results


if __name__ == '__main__':
    def func(x):
        return x^2

    x = list(range(10))
    ep = EasyProcessing(2)
    y = ep.apply(func, x)
    print(y)