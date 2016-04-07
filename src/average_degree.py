# Data insight coding challenge
# Average degree
# Author: Dinesh kumar attem

import json
from time import strptime, mktime #to process time
from itertools import combinations # to implement combinations
from heapq import heappush, heappop #to implement heapq

# seperates hashtags from raw tweet
def hashtag_list(text_tweet):
    tag_list = []
    for text in text_tweet:
        if text['text']:
            tag_list.append(text['text'])
    return tag_list

# calculates degree of the graph after processing the tweet
def calculate_degree(graph):
    nodes = 0
    edges = 0
    for key,items in graph.items():
        nodes += 1
        edges += len(set(items))

    try:
        degree =float (edges/nodes)
    except ZeroDivisionError:
        degree = 0.0
    return degree

# creates graph using hashtages from the tweet
def add_edges(graph,hash_tags,max_time):
        heap = []
        if len(hash_tags)> 1:
            edges = list(combinations(hash_tags,2))
            for each in edges:
                if each[0] not in graph.keys():
                    graph[each[0]] = [each[1]]
                else:
                    graph[each[0]].append(each[1])

                if each[1] not in graph.keys():
                    graph[each[1]] = [each[0]]
                else:
                    graph[each[1]].append(each[0])

            heappush(heap,(max_time,edges))
            degree = calculate_degree(graph)
            output.write("%.2f\n"%degree)
        else:
            heappush(heap,(max_time,0))#since no need to keep track of edges since they are not added
            degree = calculate_degree(graph)
            output.write("%.2f\n"%degree)

        return heap,graph

# deletes edges from the graph if tweet not in 60 second window
def delete_edges(graph, edges):
    try:
        if edges != 0:
            for edge in edges:
                graph[edge[0]].remove(edge[1])
                graph[edge[1]].remove(edge[0])
                if graph[edge[1]] == 0:
                    del graph[edge[1]]
                if graph[edge[0]] == 0:
                    del graph[edge[0]]
    except IndexError:
        pass

    return graph


# Main program

tweet_number = 1
max_time = 0
graph = {}
lines = open(".\\tweet_input\\tweets.txt", "r")
output = open(".\\tweet_output\\output.txt", "w+")
for line in lines:
    tweet = json.loads(line)
    try:
        time_stamp = tweet['created_at']
    except:  #omits the limiting tweets
        continue

    current_time = mktime(strptime(time_stamp,'%a %b %d %H:%M:%S +0000 %Y'))
    text_tweet = tweet['entities']['hashtags']
    hash_tags = hashtag_list(text_tweet)
    if tweet_number == 1:
        max_time = current_time
        heap, graph = add_edges(graph,hash_tags, max_time)
    else:
        try:
            while current_time - heap[0][0] > 60:
                graph = delete_edges(graph, heap[0][1])
                heappop(heap)
        except IndexError:
            pass

        heap, graph = add_edges(graph,hash_tags, current_time)

    tweet_number += 1

lines.close()
output.close()









