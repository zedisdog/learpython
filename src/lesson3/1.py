from random import choice


def Extract_Stories(code):
    '生成故事'
    time = ["早上", "中午", "半夜"]
    roles = ["小明", "小李", "小白", "小黑"]
    addresses = ["在房上", "在地下", "在电梯里", "在厕所里"]
    events = ["吃饭", "遛狗", "飞翔", "看书"]
    all_text = [time, roles, addresses, events]
    sentence = ''
    for i in range(len(code)):
        # 取模，解决输入的数字超出列表长度报错的问题
        mod = int(code[i]) % len(all_text[i])
        sentence += all_text[i][mod]
    return sentence


def Random_Stories():
    code = ''
    for i in range(4):
        code += str(choice(range(9)))
    return Extract_Stories(code)


while True:
    flag = input("你可以选择随机编故事(r),抽签编故事(e)或者让我退下(l)?(r/e/l)")
    # 随机编故事时：
    if flag == 'r':
        print(Random_Stories())

    # 抽签编故事时：
    elif flag == 'e':
        num = input("请输入四个数字(每个数字取值范围：1~4)")
        print(Extract_Stories(num))
    else:
        print("请输入正确的提示指令")
        continue