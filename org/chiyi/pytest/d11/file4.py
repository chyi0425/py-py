def main():
    try:
        with open('mm.jpg','rb') as fs1:
            data = fs1.read()
            print(type(data))
        with open('美眉.jpg','wb') as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print('can not open the specified file.')
    except IOError as e:
        print('An error occurred while reading or writing a file.')
    print('program execution completed.')

if __name__ == "__main__":
    main()