from bs4 import BeautifulSoup
import requests
async def search(tag):
    url=f'https://disboard.org/ko/servers/tag/{tag}'
    r=requests.get(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'})
    # print(f'요청 상태: {r.status_code}\n{r.text}')
    soup=BeautifulSoup(r.text,'html.parser')
    class_name='column is-one-third-desktop is-half-tablet'
    all_length=len(soup.find_all(class_=class_name))
    print(f'총 개수: {all_length}')
    base='https://disboard.org/ko/server/join/'
    result=[]
    for i in soup.find_all(class_=class_name):
        if not '#reviews' in i.find('a').get('href').replace('/ko/server/',''):
            id=i.find('a').get('href').replace('/ko/server/','')
            result.append(base+id)
    return result
'''
░██╗░░░░░░░██╗░█████╗░░██████╗██████╗░███████╗░█████╗░██╗░░░░░░░░██╗░░██╗██╗░░░██╗███████╗
░██║░░██╗░░██║██╔══██╗██╔════╝██╔══██╗██╔════╝██╔══██╗██║░░░░░░░░╚██╗██╔╝╚██╗░██╔╝╚════██║
░╚██╗████╗██╔╝███████║╚█████╗░██████╔╝█████╗░░███████║██║░░░░░░░░░╚███╔╝░░╚████╔╝░░░███╔═╝
░░████╔═████║░██╔══██║░╚═══██╗██╔══██╗██╔══╝░░██╔══██║██║░░░░░░░░░██╔██╗░░░╚██╔╝░░██╔══╝░░
░░╚██╔╝░╚██╔╝░██║░░██║██████╔╝██║░░██║███████╗██║░░██║███████╗██╗██╔╝╚██╗░░░██║░░░███████╗
░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚══════╝╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝'''