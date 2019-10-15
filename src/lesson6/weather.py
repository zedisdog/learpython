import requests

appkey = '02a5241a6a742366a9ae00d824788083'
cities = {}

def init():
    response = requests.get('https://way.jd.com/jisuapi/weather1?appkey=' + appkey)
    for city_info in response.json()['result']['result'] :
        cities.update({city_info['city']: city_info['cityid']})

def getWeather(city):
    url = 'https://way.jd.com/jisuapi/weather?cityid={}&appkey={}'.format(cities[city], appkey)
    response = requests.get(url)
    weather = response.json()['result']['result']
    text = '''
    城市：{}
    时间：{}（{}）
    天气：{}
    温度：{}~{}
    '''.format(
        weather['city'], weather['date'], weather['week'],
        weather['weather'], weather['templow'], weather['temphigh']
    )
    print(text)


def getInput():
    city = input('请输入城市\n')

    if city == 'exit':
        exit()

    if city not in cities:
        print('输入的城市错误')
        return False
    else:
        return city


def main():
    init()
    while True:
        city = getInput()
        if not city:
            continue
        getWeather(city)


if __name__ == '__main__':
    main()
