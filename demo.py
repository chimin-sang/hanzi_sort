from hanzi_sort import pinyin_order
from hanzi_sort import bihua_order

if __name__ == "__main__":
    alist = '许玉昆 家位于 二七区蜜 蜂张派 出所 附近 1只鸟 禬禳 梓潼庙 廜㢝'.split()
    print(sorted(alist, key=pinyin_order))
    print(sorted(alist, key=bihua_order))