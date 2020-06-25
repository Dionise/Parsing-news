import urllib.request
import re
import time

sites = ['https://news.yam.md/', 'https://newsmaker.md/', 'https://sputnik.md/archive/', 'https://noi.md/',
         'https://stiri.md/']


def pars():
    f = open('data.txt', 'wb')
    for site in sites:
        try:
            info = urllib.request.urlopen(site)
            html = info.read()
            f.write(html)
        except:
            pass

    f.close()



def process_information_find_specific_key():
    pars()

    f = open('data.txt', 'r', encoding='utf-8')
    strings = re.findall(regex, f.read())
    repeats = strings.count(regex)
    f.close()
    return print('Key> 'f'{regex} was repeated :', f'{repeats}', 'times')



if __name__ == '__main__':
    regex = input(r'Write key -> ')
    x=input('pause time -> ')

    while True:
        process_information_find_specific_key()
        x=time.sleep(2)
