from lxml import etree
import requests
for i in range(1087,6000):
    url = 'http://www.dtqcw.net/disease/'+str(i)+'.htm'
    resq = requests.get(url)
    tree = etree.HTML(resq.text)
    fname = tree.xpath("/html/body/div[3]/div/div[1]/div[1]/h1/text()")
    fspan = tree.xpath("/html/body/div[3]/div/div[1]/div[1]/div[1]//span/text()")
    fcontent = tree.xpath("/html/body/div[3]/div/div[1]/div[1]/div[1]//p/text()")
    if len(fname) != 0:
        filename = str(fname[0]) + '.txt'
        file = open('D://data//' + filename, 'w',encoding='utf-8')
        for q in range(0,len(fspan)):
            file.write(fspan[q]+fcontent[q]+'\n')
        file.close()
        print(str(i)+".html爬取完成")






