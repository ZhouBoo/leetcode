def merge_sort(collection):
    """Pure implementation of the merge sort algorithm in Python

    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending

    Examples:
    >>> merge_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    >>> merge_sort([])
    []

    >>> merge_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    def merge(left, right):
        result = []
        
        while left and right:
            lf = left if left[0] <= right[0] else right
            result.append((left if left[0] <= right[0] else right).pop(0))
        return result + left + right

        if len(collection) <= 1:
            return collection
        
        mid = len(collection) // 2

        return merge(merge_sort(collection[:mid]), merge_sort(collection[mid:]))