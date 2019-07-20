def main():
    try:
        with open('致橡树.txt','r',encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('unable to open the specified file! ')
    except LookupError:
        print('An unknown encoding was specified!')
    except UnicodeDecodeError:
        print('Decoding error when reading a file!')


if __name__ == "__main__":
    main()