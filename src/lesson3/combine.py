import sys


def make_sentence(code):
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


def write_file(str):
    '写文件'
    root = sys.path[0]
    file_name = root + '/text.txt'
    file = open(file_name, 'w+', encoding='UTF-8')
    file.writelines(str)
    file.close()


def check_param(param):
    '检查参数'
    if param == 'exit':
        exit()
    elif not param.isdigit() or len(param) != 4:
        print('输入格式错误，请输入四个数字')
        return False
    else:
        return True


def main():
    while True:
        code = input('输入一个组合\n')
        if not check_param(code):
            continue
        sentence = make_sentence(code)
        print(sentence)
        write_file(sentence)
        print('已保存到文件./text.txt中')


if __name__ == '__main__':
    main()
