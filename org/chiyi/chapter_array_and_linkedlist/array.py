#!/usr/bin/python3
# _*_ coding: utf-8 _*_
# @author : chiyi
# @desc : 抓交通肇事犯


# 初始化数组
import random


def random_access(nums: list[int]) -> int:
    """随机访问元素"""
    # 在区间[0, len(nums)-1]中随机抽取一个数字
    random_index = random.randint(0, len(nums) - 1)
    random_num = nums[random_index]
    return random_num


def insert(nums: list[int], num: int, index: int):
    """在数组的索引index处插入元素num"""
    # 把索引index及之后的所有元素向后移动一位
    for i in range(len(nums) - 1, index, -1):
        nums[i] = nums[i - 1]
    # 将num赋值给index处的元素
    nums[index] = num


def remove(nums: list[int], index: int):
    """删除索引index处的元素"""
    # 把索引index之后的所有元素向前移动一位
    for i in range(index, len(nums) - 1):
        nums[i] = nums[i + 1]


def traverse(nums: list[int]):
    """遍历数组"""
    count = 0
    # 通过索引遍历数组
    for i in range(len(nums)):
        count += nums[i]

    # 直接遍历数组元素
    for num in nums:
        count += num

    # 同时遍历数组索引和元素
    for i, num in enumerate(nums):
        count += nums[i]
        count += num


def find(nums: list[int], target: int) -> int:
    """在数组中查找指定元素"""
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1


def extend(nums: list[int], enlarge: int) -> list[int]:
    """扩展数组长度"""
    # 初始化一个扩展长度后的数组
    res = [0] * (len(nums) + enlarge)
    # 将愿数组中的所有元素复制到新数组
    for i in range(len(nums)):
        res[i] = nums[i]
    return res


if __name__ == "__main__":
    # i代表前两位车牌号数字，k代表车牌号
    flag = 0
    for i in range(10):
        if flag:
            break
        for j in range(10):
            if flag:
                break
            # 判断前两位和后两位数字是否相同
            if i != j:
                # 组成4位车牌号码
                k = 1000 * i + 100 * i + 10 * j + j
                # 判断k是否是某个数的平方，是就输出
                for temp in range(31, 100):
                    if temp * temp == k:
                        print("车牌号为：", k)
                        flag = 1
                        break
