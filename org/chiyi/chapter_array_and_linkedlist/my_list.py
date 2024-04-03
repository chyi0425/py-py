class MyList:
    """列表类"""

    def __init__(self):
        """构造方法"""
        self._capacity: int = 10  # 列表容量
        self._arr: list[int] = [0] * self._capacity
        self._size: int = 0
        self._extend_ratio: int = 2

    def size(self) -> int:
        """获取列表长度"""
        return self._size

    def capacity(self) -> int:
        """get list's capacity"""
        return self._capacity

    def get(self, index: int) -> int:
        """access element"""
        # if index out of bound,throw exception
        if index < 0 or index >= self._size:
            raise IndexError("out of bound")
        return self._arr[index]

    def set(self, num: int, index: int):
        """更新元素"""
        if index < 0 or index >= self._size:
            raise IndexError("out of bound")
        self._arr[index] = num

    def add(self, num: int, index: int):
        """insert an element into list by index num"""
        if index < 0 or index >= self._size:
            raise IndexError("out of bound")
