#!/usr/bin/env python
# coding: utf-8

# ### 프로그래밍2 3주차 리스트 /  집합(set)
# 
# ## 3.1. List ADT
# - List() : 비어 있는 새로운 리스트를 만든다
# - insert(pos, e) : pos 위치에 새로운 요소 e 를 삽입한다
# - delete(pos) : pos 위치에 있는 요소를 꺼내고(삭제) 반환한다
# - IsEmpty() : 리스트가 비어있는지를 검사한다.
# - getEntry(pos): pos 위치에 있는 요소를 반환한다
# - size() : 리스트안의 요소의 개수를 반환한다.
# - clear() : 리스트를 초기화 한다.
# - find(items) : 리스트에서 item이 있는지 찾아 인덱스를 반환한다
# - replace(pos, item) : pos에 있는 항목을 item으로 바꾼다
# - sort() : 리스트의 항목들을 어떤 기준으로 정렬한다
# - merge(lst) : 다른 리스트 lst를 리스트에 추가한다
# - display() : 리스트를 화면에 출력한다
# - append(e) : 리스트의 맨 뒤에 새로운 항목을 추가한다

# In[ ]:


items = []

def insert(pos, e):
    items.insert(pos, e)    # items 리스트안에 pos 위치에 새로운 e 삽입
    
def delete(pos):
    return items.pop(pos)      # pos 위치에 꺼내고 반환
    
def getEntry(pos):
    return items[pos]   # pos 번째 항목 반환

def isEmpty():
    if len(items) == 0:
        return True
    else:
        return False             #크기가 0이면 True 아니면 False
           
def size():
    return len(items)      #리스트의 크기 반환

def clear():
    global items          #itms 전역 item 지역 global 함수로 전역으로 변경해줌
    items = []            #items를 초기화
    
def find(item):
    return items.index(item)        #탐색후 인덱스 변환

def replace(pos, e): 
    items[pos] = e            #pos 번째 항목 변경
    
def sort():
    items.sort()           # 정렬
    
def merge(lst):
    items.extend(lst)       #list에 lst 추가
    
def display(msg='ArrayList'):
    print(msg,size(),items)          #메시지 크기 배열내용 출력


# # class 사용하여 전역변수로 만들기

# In[14]:


class ArrayList:
    def __init__(self):
        self.items = []
    
    def insert(self,pos, e):
        self.items.insert(pos, e)   

    def delete(self,pos):
        return self.items.pop(pos)     

    def getEntry(self,pos):
        return self.items[pos]   

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False             

    def size(self):
        return len(self.items)    

    def clear(self):
        self.items = []           

    def find(self,item):
        return self.items.index(item)     

    def replace(self,pos, e): 
        self.items[pos] = e            

    def sort(self):
        self.items.sort()           

    def merge(self,lst):
        self.items.extend(lst)       

    def display(self,msg='ArrayList'):
        print(msg,self.size(),self.items)       


# # test

# In[15]:


s = ArrayList()


# In[16]:


s.display()


# In[18]:


s.insert(0,10)


# In[19]:


s.display()


# In[23]:


s.insert(1,50); s.insert(2,70); s.insert(3,40)   #한줄에 여러개 사용할때 ; 사용


# In[24]:


s.display()


# In[26]:


s.sort()
s.display()


# In[27]:


s.clear()
s.display()


# # 라인 편집기

# In[30]:


def myLineEditor():
    lst = ArrayList()
    while True:                  #반복문 무한하게 돌리기
        command = input('메뉴 선택 i: 입력, d:삭제, r: 변경, p:출력, l: 파일 읽기, s:자징, q 출력: ')
        if command == 'i':
            # insert (pos,e) 사용
            pos = int(input('위치를 입력하세요'))
            e = input('입력할 내용은?')
            lst.insert(pos,e)
            
        elif command == 'd':
            pos = int(input('삭제할 위치는?'))
            lst.delete(pos)
        
        elif command == 'r':
            pos = int(input('변경할 위치는?'))
            e = input('변경할 내용은?')
            lst.replace(pos,e)
            
        elif command == 'p':
            print('Line Editor')
            for pos in range(lst.size()):
                print('%2d : '%pos, end='')
                print(lst.getEntry(pos))
            print()
            
        elif command == 'l':
            filename =  'test.txt'
            infile = open(filename, 'r')
            lines = infile.readlines()
            for line in lines:
                lst.insert(lst.size(),line.rstrip('\n'))
            infile.close()
            
        elif command == 's':
            filename = 'test.txt'
            outfile = open(filename, 'w')
            for i in range(lst.size()):
                outfile.write(lst.getEntry(i) + '\n')
            outfile.close()
            
        elif command == 'q':
            return
        
        else:
            print('잘못 누르셧습니다')
    


# In[31]:


myLineEditor()


# In[ ]:




