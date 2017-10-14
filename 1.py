import os
import re

#arp 리스트 얻기
r = os.popen('arp -a','r',1)
#line=r.read().split('\n')[3:][:-1]
line=r.read()


for x in line :
    #ip와 mac 분리
    x=x.strip()
    x=re.sub("\s{2,}", ' ', x).split(' ')
    arp=[x[0],x[1]]

    #static으로 설정
    command="arp -s %s %s"%(arp[0],arp[1])
    #print(command)
    os.popen(command)

