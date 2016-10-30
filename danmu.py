# encoding:utf-8
from lxml import etree
import re
import requests


def get_danmu(av=6849182):
    url = "http://www.bilibili.com/video/av" + av
    page = requests.get(url)
    match = re.search(r'cid=(\d+)', page.text.encode('utf-8'))
    if match:
        cid = match.group(1)
    else:
        print("Cannot find danmu!")
        return
    xml_path = "http://comment.bilibili.tv/{0}.xml".format(cid)

    danmu = requests.get(xml_path)
    doc = etree.fromstring(danmu.text.encode('utf-8'))
    root = doc
    ret = []
    for i in root:
        ret.append(i.text)
    return ret

if __name__ == '__main__':
    av = raw_input("input the av number:")
    l = get_danmu(av)
    with open('result.txt', 'wb') as f:
        for i in l:
            if i:
                f.write(i.encode('utf-8')+'\n')
