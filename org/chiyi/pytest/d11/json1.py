import json

def main():
    mydict = {
        'name':'张三',
        'age':38,
        'qq':123456,
        'friends':['李四','王五'],
        'cars':[
            {'brangd':'BYD','max_speed':180},
            {'brangd':'Audi','max_speed':280},
            {'brangd':'Benz','max_speed':320}
        ]
    }
    try:
        with open('data.json','w',encoding='utf-8') as fs:
            json.dump(mydict,fs)
    except IOError as e:
        print(e)
    print('save data completed!')

if __name__ == "__main__":
    main()