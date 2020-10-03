# Ctrl + Shift+ F10 запускает текущий файл
import vk_api

A = [[0, 1, 0, 0, 0],
     [1, 0, 1, 0, 0],
     [0, 1, 0, 1, 1],
     [0, 0, 1, 0, 1],
     [0, 0, 1, 1, 0]]
length_A = len(A)

# Количество друзей у каждой вершины
old_node_value = [0 for i in range(length_A)]
med_node_value = [0 for i in range(length_A)]
new_node_value = [0 for i in range(length_A)]

for i in range(length_A):
    friends = 0
    for j in range(length_A):
        if A[i][j] == 1:
            friends += 1
    old_node_value[i] = friends

Epsilon = 0.1
difference = 1
cnt = 0

while difference > Epsilon:
    for i in range(length_A):
        new_node_value[i] = 0
        delitel = 0
        for j in range(length_A):
            if A[i][j] != 0:
                new_node_value[i] += old_node_value[j]
                delitel += 1
        med_node_value[i] = new_node_value[i]/(delitel)
    difference = 0
    for i in range(length_A):
        if abs(old_node_value[i] - med_node_value[i]) < Epsilon:
            difference += 1
    if difference == length_A:
        difference = 0  # Если все различаются меньше чем на Epsilon - заканчивай
    else:
        difference = 1
    for i in range(length_A):
        old_node_value[i] = med_node_value[i]
    cnt += 1

print(cnt)
print(old_node_value)
print(med_node_value)

# Индекс элемента центрального по значению собственного вектора
print(1+old_node_value.index(max(old_node_value)))

# import matplotlib.pyplot as plt
# import networkx as nx
# import numpy as np
#
# G = nx.from_numpy_matrix(np.matrix(A))
#
# G.add_nodes_from(["Маша", "Саша", "Cергей", "Даша"])
# labelmap = dict(zip(G.nodes(), ["1", "2", "3", "4","5","6","7","8"]))
# nx.draw(G, labels=labelmap, with_labels=True)
# plt.show()


#, labels=labelmap, with_labels=True



#plt.rcParams['figure.figsize'] = (10, 6)

#G.add_nodes_from(["1", "2", "3", "4", "5"])
#nx.draw(G, with_labels=True, font_weight='bold')


# G.add_nodes_from() Добавить узлы из
# draw_networkx_edge_labels(G, pos, edge_labels='Нет', label_pos=0.5, font_size=10, font_color='k', font_family='sans-serif', font_weight='normal', bbox=None, ax=None, rotate=True)
# edge_labels = nx.draw_networkx_edge_labels(G, pos=nx.spring_layout(G))
# pos = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
# edge_labels = nx.draw_networkx_edge_labels(G, pos, edge_labels='Нет', label_pos=0.5, font_size=10, font_color='k', font_family='sans-serif', font_weight='normal', bbox=None, ax=None, rotate=True))
# nx.draw_networkx_edge_labels(G, pos)
