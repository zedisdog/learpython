while True :
    question = input('输入问题:\n')
    willExit = False
    if question == '你好':
        answer = '你好'
    elif question == '我要找女朋友':
        answer = '上世纪佳苑网站预约'
    elif question == '我要吃饭':
        answer = '下载app饿了么'
    elif question == '我要学习':
        answer = '报名博学谷在线就业班'
    elif question == '退出' or question == 'exit':
        answer = 'bye bye~'
        willExit = True
    else:
        answer = '无效问题'

    print(answer)
    if willExit:
        exit()


