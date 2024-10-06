import networkx as nx


G = nx.Graph()

with open("graph_data.txt", "r") as f:
    f.readline()
    cur_line = f.readline()
    while cur_line != "Edges:\n":
        G.add_node(int(cur_line.strip("\n")))
        cur_line = f.readline()
    cur_line = f.readline()
    while cur_line != "":
        u, v = map(int, cur_line.strip("\n").split())
        G.add_edge(u, v)
        cur_line = f.readline()

groupmates = [(225790978, "Алексеев Владислав Евгеньевич"),
              (752279211, "Гундоров Всеволод Сергеевич"),
              (202377873, "Жуков Тимофей Дмитриевич"),
              (138716736, "Ильин Илья Олегович"),
              (306787585, "Круглова Мария Сергеевна"),
              (202038842, "Ланин Олег Викторович"),
              (352418484, "Леонов Михаил Игоревич"),
              (142470714, "Лобанов Захар Олегович"),
              (203626707, "Лошманов Юрий Андреевич"),
              (218147810, "Макарцев Артем Михайлович"),
              (253647021, "Мохляков Павел Александрович"),
              (210835290, "Насонков Никита Владимирович"),
              (175952275, "Недосеков Иван Дмитриевич"),
              (206038535, "Полюбин Арсений Игоревич"),
              (178728261, "Филатова Лада Вячеславовна")]

betweenness_centrality = nx.betweenness_centrality(G)
closeness_centrality = nx.closeness_centrality(G)
eigenvector_centrality = nx.eigenvector_centrality(G)
for groupmate in groupmates:
    print(f"Центральность по посредничеству для человека {groupmate[1]} (id={groupmate[0]}): {betweenness_centrality[groupmate[0]]}")
    print(f"Центральность по близости для человека {groupmate[1]} (id={groupmate[0]}): {closeness_centrality[groupmate[0]]}")
    print(f"Центральность по собственному вектору для человека {groupmate[1]} (id={groupmate[0]}): {eigenvector_centrality[groupmate[0]]}")
    print()