class IP():
   def __init__(self,ipaddress):
      url='http://m.ip138.com/ip.asp?ip='
      self.IP=ipaddress
      self.site=url+self.IP
      self.header={'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}
   def get_phy(self):
      import requests as RQ
      import re
      try:
         r=RQ.get(self.site)

         r.raise_for_status()
         r.encoding=r.apparent_encoding
         html=r.text[-1000:]
         #print(html)
         answer=re.findall('本站主数据：(.*?)</p><p',html,re.S)
         answer=answer[0]
         return '您查询的IP:%s物理地址应该在:%s '%(self.IP,answer)
      except:
         return 'sth wrong'


#素质裤衩分析
'''<h1 class="query">您查询的IP：1.1.1.1</h1><p class="result">
本站主数据：澳大利亚 </p><p class="result">
参考数据一：澳大利亚</p>
'''
'''
while True:
   point='.'
   for I in range(7,100,7):
      for j in range(1,100,7):
         for k in range(1,100,70):
            for L in range(1,100,20):
               add=str(I)+point+str(j)+point+str(k)+point+str(L)
               print(add)
               #ip=input() 
               i=IP(add)
               ans=i.get_phy()
               print(ans)
'''
#第一个利用接口写的东西

'''num=input()
num_list=list(num)
num_list.remove(' ')
num_list.remove(' ')
new_num_list=[]
print(num_list)
for i in range(6):
   if num_list[i]=='-':
      new_num_list.append(int(num_list[i]+num_list[i+1]))
   '''


'''
sentinel ='' # 遇到这个就结束
lines = []
for line in iter(input, sentinel):
    lines.append(line)

init=list(str(input()))
try:
   init.remove(' ')
except:
   pass
print(int(init[0])+int(init[1]))

string=input()
str_list=list(string)
str_list=str_list.reverse()
new_str=str(str_list)
print(new_str)
'''
