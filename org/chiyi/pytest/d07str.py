def main():
    str1 = 'hello, world!'
    print(len(str1))
    # 获得字符串首字母大写的拷贝
    print(str1.capitalize())
    # 获得字符串变大写后的拷贝
    print(str1.upper())

    # 从字符串中查找子串所在位置
    print(str1.find('or'))
    print(str1.find('shit'))

    # 与find类似，但找不到会引发异常
    print(str1.index('or'))
#    print(str1.index('shit'))
    print(str1.startswith('He'))
    print(str1.startswith('hel'))
    print(str1.endswith('!'))
    # 将字符串以指定的宽度居中并在两侧填充指定的字符串
    print(str1.center(50,'*'))
    # 将字符串以指定的宽度靠右放置，左侧填充指定的字符串
    print(str1.rjust(50,'*'))
    str2 = 'abc123456'
    # 从字符串取出指定位置的字符(下标运算)
    print(str2[2])
    # 字符串切片(从指定的开始索引到指定的结束索引)
    print(str2[2:5])
    print(str2[2:])
    print(str2[2::2])
    print(str2[::2])
    print(str2[::-1])
    print(str2[-3:-1])

    print(str2.isdigit())
    print(str2.isalpha())
    print(str2.isalnum())

    str3 = '  jackfrued@126.com '
    print(str3)
    print(str3.strip())

if __name__ == '__main__':
    main()