#!/usr/bin/python3
# _*_ coding: utf-8 _*_
# @author : chiyi
# @desc : 百钱百鸡

if __name__ == "__main__":
    # cock表示公鸡数量，hen表示母鸡数量，chicken表示小鸡数量
    # 外层循环控制公鸡数量取值范围0-20
    cock = 0
    while cock <= 20:
        # 内层循环控制母鸡数量取值范围0-33
        hen = 0
        while hen <= 33:
            # 内层循环控制小鸡数量取值范围为0-100
            # chicken = 0
            # while chicken <= 100:
            #     # 条件控制
            #     if (5 * cock + 3 * hen + chicken / 3.0 == 100) and (cock + hen + chicken == 100):
            #         print("cock=%2d,hen=%2d,chicken=%2d\n" % (cock, hen, chicken))
            #     chicken += 1
            # 算法优化，当公鸡和母鸡数量确定后，小鸡数量是固定的
            chicken = 100 - cock - hen
            if (5 * cock + 3 * hen + chicken / 3.0 == 100) and (cock + hen + chicken == 100):
                print("cock=%2d,hen=%2d,chicken=%2d\n" % (cock, hen, chicken))
            hen += 1
        cock += 1
