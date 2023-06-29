def x(city):
    if city == 'a':
        return 'Arad'
    elif city == 'z':
        return 'Bucharest'
    elif city == 's':
        return 'Craiova'
    elif city == 't':
        return 'Eforie'
    elif city == 'o':
        return 'Fagaras'
    elif city == 'v':
        return 'Dobreta'
    elif city == 'n':
        return 'Hirsova'
    elif city == 'q':
        return 'lasi'
    elif city == 'g':
        return 'Lugoj'
    elif city == 'l':
        return 'Mehadia'
    elif city == 'f':
        return 'Neamt'
    elif city == 'b':
        return 'Oradea'
    elif city == 'p':
        return 'Pitesti'
    elif city == 'r':
        return 'Rimnicu Vilcea'
    elif city == 'c':
        return 'Timisoara'
    elif city == 'd':
        return 'Urziceni'
    elif city == 'h':
        return 'Vaslui'
    elif city == 'e':
        return 'Zerind'

def aStarAlgo(start_node, stop_node):
    start_node = start_node[0].lower()
    stop_node = stop_node[0].lower()
    open_set = set(start_node)
    closed_set = set()
    g = {}
    parents = {}
    total_distance = 0
    g[start_node] = 0
    parents[start_node] = start_node

    while len(open_set) > 0:
        n = None
        # node with Lowest f() is found
        for v in open_set:
            if n is None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v
        if n == stop_node or Graph_nodes[n] is None:
            pass
        else:
            for (m, weight) in get_neighbors(n):
                # nodes 'm' not in first and last set are added to first #n is set its parent
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                # for each node m, compare its distance from start i.e g(m) to the #from start through n node
                else:
                    if g[m] > g[n] + weight:  # update g(m)
                        g[m] = g[n] + weight
                        # change parent of m to n
                        parents[m] = n
                        total_distance = g[m]
                        # if m in closed set, remove and add to open
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)
        if n is None:
            print('Path does not exist!')
            return None
        # if the current node is the stop_node
        # then we begin reconstructin the path from it to the start_node
        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(x(n))
                n = parents[n]
            path.append(x(start_node))
            path.reverse()
            print('Path found: {}'.format(path))
            print('Total distance:', total_distance)
            with open("Output.txt", "w") as f:
                f.write("Path: ")
                for word in path:
                    f.write(word)
                    if(word != path[-1]):
                        f.write("->")
                f.write("\n")
                f.write("Total distance: " + str(total_distance))
            return path
        # remove n from the open_list, and add it to closed_list # because all of his neighbors were inspected
        open_set.remove(n)
        closed_set.add(n)
    print('Path does not exist!')
    return None


# define fuction to return neighbor and its distance #from the passed node
def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None


def heuristic(n):
    H_dist = {}
    file2 = open("Input file.txt", "r")
    for line in file2:
        line1 = line.split(" ")
        location = line1[0].strip()
        location = location.lower()
        linear_distance = int(line1[1])
        H_dist[location[0]] = linear_distance

    return H_dist[n]

Graph_nodes = {}
file1 = open("Input file.txt", "r")
for line in file1:
    line_list = line.split(" ")
    city_count = int(len(line_list) / 2)
    for i in range(city_count):
        city1 = line_list[0].lower()
        if i == 0:
            pass
        if i != 0:
            city2 = line_list[i * 2].lower()
            dct = int(line_list[1 + (i * 2)])
            Graph_nodes.setdefault(city1[0], []).append([city2[0], dct])

# Describe your graph here
print("Please enter the start node below (Case does not matter):")
Start_node = input().strip().lower()
print("Please enter the destination node below (Case does not matter):")
Dest_node = input().strip().lower()
aStarAlgo(Start_node, Dest_node)