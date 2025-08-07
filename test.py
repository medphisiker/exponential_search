from solution import get_index_range


def test():
    # target: 5 (low внутри массива)
    # idx     0 1 2 3 4 5 6 7
    # array:  1 2 3 4 5 6 7 8
    #             l   h

    array = [1, 2, 3, 4, 5, 6, 7, 8]
    target = 5
    right_index_range = [2, 4]
    index_range = get_index_range(array, target)
    assert index_range == right_index_range

    # target: 6 (low выйдет за границы массива)
    # idx     0 1 2 3 4 5 6 7
    # array:  1 2 3 4 5 6 7 8
    #                 l     h

    array = [1, 2, 3, 4, 5, 6, 7, 8]
    target = 6
    right_index_range = [4, 7]
    index_range = get_index_range(array, target)
    assert index_range == right_index_range

    # target: 1 (target на нулевом элементе)
    # idx     0 1 2 3 4 5 6 7
    # array:  1 2 3 4 5 6 7 8
    #         l h

    array = [1, 2, 3, 4, 5, 6, 7, 8]
    target = 1
    right_index_range = [0, 1]
    index_range = get_index_range(array, target)
    assert index_range == right_index_range


if __name__ == "__main__":
    test()
