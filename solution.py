def get_index_range(array:list[int], target:int) -> list[int]:
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
    low = 1
    
    while array[low] < target:
        low *= 2
        
        if low > len(array) - 1:
            hight = len(array) - 1
            low = low // 2
            
            return [low, hight]
            
    hight = low
    low = hight // 2
        
    return [low, hight]


if __name__ == "__main__":
    array_len = int(input())
    array = list(map(int, input().split()))
    target = int(input())
    
    index_range = get_index_range(array, target)
    print(" ".join(str(idx) for idx in index_range))
