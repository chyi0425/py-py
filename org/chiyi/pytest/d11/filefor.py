import time

def main():
    # read the entire file content at once
    with open('致橡树.txt','r',encoding='utf-8') as f:
        print(f.read())

    # read line by line through a for-in loop
    with open('致橡树.txt',mode='r') as f:
        for line in f:
            print(line,end='')
            time.sleep(0.5)
    print()

    # read files are read into the list by row
    with open('致橡树.txt') as f:
        lines = f.readlines()
    print(lines)

if __name__ == "__main__":
    main()