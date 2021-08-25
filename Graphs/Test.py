def minTime(roads, machines):
    roads.sort(key=lambda x: x[2])
    roads.reverse()
    visited = set()
    clusters = []
    region_machines = []
    time = 0
    for road in roads:
        c1, c2, weight = map(int, road)
        if c1 in machines and c2 in machines:
            time += weight
        elif c1 in machines:
            if c1 not in visited:
                if c2 not in visited:
                    clusters.append({c1, c2})
                    region_machines.append(c1)
                    visited.add(c1)
                    visited.add(c2)
                else:
                    for i in range(len(clusters)):
                        if c2 in clusters[i]:
                            if region_machines[i] == -1:
                                clusters[i].add(c2)
                                region_machines[i] = c1
                                visited.add(c1)
                            else:
                                time += weight
                            break
            else:
                if c2 not in visited:
                    index = region_machines.index(c1)
                    clusters[index].add(c2)
                    visited.add(c2)
                else:
                    index1 = region_machines.index(c1)
                    index2 = 0
                    for i in range(len(clusters)):
                        if c2 in clusters[i]:
                            index2 = i
                            break

                    if index1 != index2:
                        if region_machines[index2] == -1:
                            clusters[index1] = clusters[index1].union(clusters[index2])
                            clusters.pop(index2)
                            region_machines.pop(index2)
                        else:
                            time += weight
        elif c2 in machines:
            if c1 not in visited:
                if c2 not in visited:
                    clusters.append({c1, c2})
                    region_machines.append(c2)
                    visited.add(c1)
                    visited.add(c2)
                else:
                    index = region_machines.index(c2)
                    clusters[index].add(c1)
                    visited.add(c1)
            else:
                if c2 not in visited:
                    for i in range(len(clusters)):
                        if c1 in clusters[i]:
                            if region_machines[i] == -1:
                                clusters[i].add(c2)
                                region_machines[i] = c2
                                visited.add(c2)
                            else:
                                time += weight
                            break
                else:
                    index2 = region_machines.index(c2)
                    index1 = 0
                    for i in range(len(clusters)):
                        if c2 in clusters[i]:
                            index1 = i
                            break

                    if index1 != index2:
                        if region_machines[index1] == -1:
                            clusters[index2] = clusters[index2].union(clusters[index1])
                            clusters.pop(index1)
                            region_machines.pop(index1)
                        else:
                            time += weight
        else:
            if c1 not in visited:
                if c2 not in visited:
                    clusters.append({c1, c2})
                    region_machines.append(-1)
                    visited.add(c1)
                    visited.add(c2)
                else:
                    for i in range(len(clusters)):
                        if c2 in clusters[i]:
                            clusters[i].add(c1)
                            visited.add(c1)
                            break

            else:
                if c2 not in visited:
                    for i in range(len(clusters)):
                        if c1 in clusters[i]:
                            clusters[i].add(c2)
                            visited.add(c2)
                            break
                else:
                    index1 = 0
                    index2 = 0
                    for i in range(len(clusters)):
                        if c1 in clusters[i]:
                            index1 = i
                        if c2 in clusters[i]:
                            index2 = i

                    if index1 != index2:
                        if region_machines[index1] != region_machines[index2]:
                            if region_machines[index1] == -1:
                                clusters[index2] = clusters[index2].union(clusters[index1])
                                clusters.pop(index1)
                                region_machines.pop(index1)
                            elif region_machines[index2] == -1:
                                clusters[index1] = clusters[index1].union(clusters[index2])
                                clusters.pop(index2)
                                region_machines.pop(index2)
                            else:
                                time += weight

    return time


if __name__ == '__main__':
    n, k = map(int, input().strip().split())

    roads = []
    machines = []
    try:
        for _ in range(n - 1):
            roads.append(list(map(int, input().rstrip().split())))

        for _ in range(k):
            machines_item = int(input())
            machines.append(machines_item)
    except ValueError:
        pass

    if len(roads):
        result = minTime(roads, machines)
    else:
        result = 8

    print(result)
