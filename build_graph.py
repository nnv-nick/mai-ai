import os
import random
import requests
import time


def sleep_for_some_time():
    time_to_sleep_ms = random.randint(10, 30)
    time.sleep(0.001 * time_to_sleep_ms)


def request_friends(id):
    access_token = os.environ["ACCESS_TOKEN"]
    response = requests.get("https://api.vk.com/method/friends.get?v=5.199&user_id={}&access_token={}".format(id, access_token))
    sleep_for_some_time()
    friends_json = response.json()
    if "response" not in friends_json:
        return None
    return friends_json["response"]["items"]


groupmates = [225790978, 752279211, 202377873, 138716736, 306787585, 202038842, 352418484, 142470714, 203626707, 218147810, 253647021, 210835290, 175952275, 206038535, 178728261]
graph_vertices = set(groupmates)
graph_edges = set()
id_to_friends = {}

# getting groupmates' friends
for groupmate in groupmates:
    friends = request_friends(groupmate)
    if friends is not None:
        id_to_friends[groupmate] = friends
        for id in friends:
            graph_vertices.add(id)

cnt = 0
# getting friends of friends
for groupmate in groupmates:
    if groupmate not in id_to_friends:
        continue
    for friend_id in id_to_friends[groupmate]:
        if friend_id in id_to_friends:
            continue
        friends = request_friends(friend_id)
        if friends is not None:
            id_to_friends[friend_id] = friends
            for id in friends:
                graph_vertices.add(id)
    cnt += 1
    print("Processed {} groupmates' friends".format(cnt))

print("Got {} vertices".format(len(graph_vertices)))

# getting friends of friends of friends to cover all edges
cnt = 0
for id in graph_vertices:
    if id in id_to_friends:
        continue
    friends = request_friends(id)
    if friends is not None:
        id_to_friends[id] = friends
    cnt += 1
    if cnt % 1000 == 0:
        print("Processed {} friends of friends".format(cnt))

# calculating edges
cnt = 0
for id, friends in id_to_friends.items():
    for friend_id in friends:
        if friend_id not in graph_vertices:
            continue
        u = id
        v = friend_id
        if u > v:
            u, v = v, u
        graph_edges.add((u, v))
    cnt += 1
    if cnt % 1000 == 0:
        print("Processed {} users".format(cnt))

print("Writing graph data about {} vertices and {} edges".format(len(graph_vertices), len(graph_edges)))

# writing graph data to the file
with open("graph_data.txt", "w") as f:
    print("Vertices:", file=f)
    for vertex in graph_vertices:
        print(vertex, file=f)
    print("Edges:", file=f)
    for edge in graph_edges:
        print(*edge, file=f)
