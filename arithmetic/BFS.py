# 广度优先搜索

from collections import deque

graph = {}
graph['you'] = ['alice','bob','claire']
graph['bob'] = ['anuj','peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom','jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

def person_is_seller(name):
    return name[-1] == 'm'

def search(name):
    search_queue = deque()   #创建一个队列
    search_queue += graph[name]   #将节点都加入到搜索队列中
    searched = []   #用于记录检查过的人
    while search_queue:  #只要队列不为空
        person = search_queue.popleft()   #就取出第一个节点
        if person not in searched:   #仅当这个节点没检查过时才检查
            if person_is_seller(person):
                print (person + ' is a mango seller!')
                return True
            else:
                search_queue +=graph[person]
                searched.append(person)   #将这个节点标记为检查过
    return False

search('you')


