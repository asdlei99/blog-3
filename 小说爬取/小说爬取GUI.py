from tkinter import *
from bs4 import BeautifulSoup
import requests
import time
root = Tk()
root.title('小说爬取')


root.geometry("600x400")  # 使用geometry可以控制root窗口的大小


def login_check(event):  # 使用第二种方法设置事件, 需要响应函数的第一个参数为event
    global root
    url = e1.get()  # entry.get()获取entry框的输入
    all1 = int(e2.get())
    path=e3.get()+".txt"

    next = url.split('/')[-1]
    url0 = url.replace(next, "")
    time0 = time.time()
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36"}
    a = ""
    i = 0

    def replace(content):
        content = content.replace("<br/>\u3000\u3000<br/>\u3000\u3000\xa0\xa0\xa0\xa0", "\r\n")
        content = content.replace("[<div id=\"content\">\r\n\t\t\t\t\xa0\xa0\xa0\xa0", "\r\n")
        content = content.replace("\t\t\t\t<script>chaptererror();</script>\n</div>]", "")
        content = content.replace("<br/>\u3000\u3000", "\r\n")
        content = content.replace("[<div id=\"content\">", "\r\n")
        content = content.replace("\t\t\t\t<script>chaptererror();</script>\n</br></div>]", "")
        return content

    while 1:
        url = url0 + next
        try:
            r = requests.get(url, timeout=10, headers=header)
        except:
            continue
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        demo = r.text
        soup = BeautifulSoup(demo, "html.parser")
        title = str(soup.h1.string)
        a += title
        content = str(soup.select("#content"))
        content = replace(content)
        a += content
        try:
            next = soup.find('a', 'next').attrs['href']
        except:
            break
        i += 1
#        time1 = time.time()
#        b="当前进度:  "+str(round((i * 100 / all1),2))+"% 总花费时间:"+str(round(time1 - time0,2))
#        l1["text"] = b
        if i >= all1:
            break
    b="共爬取了"+str(all1)+"章内容,花时"+str(time1 - time0)+"s"
    l1["text"]=b
    g = open(path, mode='w', encoding='utf-8')
    g.write(a)
    g.close()


Label(root, text='要看的开始章节的网址：').grid(row=0, column=0)  # grid指的是网格化排版, 是我们将来在tkinter中最主要的排版方式
e1 = Entry(root)
e1.grid(row=0, column=1)

Label(root, text='要爬取的章数：').grid(row=1, column=0)
e2 = Entry(root)

e2.grid(row=1, column=1)

Label(root, text='要保存的文件名：').grid(row=2, column=0)
e3 = Entry(root)

e3.grid(row=2, column=1)

b1 = Button(root, text="爬取")
b1.bind('<Button-1>', login_check)
b1.grid(row=3, column=1)

b=""
l1 = Label(root, text=b)
l1.grid(row=4, column=1)
l2 = Label(root, text='')
l2.grid(row=3, column=0)
l3 = Label(root, text="使用说明：我写的爬取小说程序是针对www.qu.la这个网站上的小说")
l3.grid(row=5, column=0)
#l4 = Label(root, text="，请在www.qu.la上找到要爬取的小说的第一面的地址")
#l4.grid(row=5, column=1)



root.mainloop()