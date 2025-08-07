def get_index_range(array: list[int], target: int) -> list[int]:
    """Функция возвращает диапазон индексов, где может находиться число
    `target` в отсортированном по возрастанию массиве целых чисел array.

    Использует фазу Экспоненциального расширения для поиска диапазона чисел
    из паттерна Экспоненциальный поиск.

    Временная сложность O(log(m)), где m - номер индекса элемента в массиве,
    или индекса где могло бы располагаться число target, если оно отсутствует.

    Пространственная сложность O(1).

    Args:
        array (list[int]): отсортированный по возрастанию массив целых чисел
        target (int): число, диапазон для которого мы ищем

    Returns:
        list[int]: диапазон индексов, где может находиться число target.
    `target`
    """
    # Этап 1: Экспоненциальное расширение границ
    low = 1
    array_len = len(array)

    while low < array_len and array[low] < target:
        low *= 2

    hight = min(low, array_len - 1)
    low = low // 2

    return [low, hight]


if __name__ == "__main__":
    array_len = int(input())
    array = list(map(int, input().split()))
    target = int(input())

    index_range = get_index_range(array, target)
    print(" ".join(str(idx) for idx in index_range))
