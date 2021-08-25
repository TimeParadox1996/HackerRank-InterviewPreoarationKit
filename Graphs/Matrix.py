def minTime(n, roads, machines):
    roads.sort(key=lambda x: x[2])
    roads.reverse()

    machine_regions = dict()
    visited = [-1 for _ in range(n)]
    regions = [-1 for _ in range(n)]
    for machine in machines:
        machine_regions[machine] = {machine}
        visited[machine] = "M"
        regions[machine] = machine

    time = 0
    clusters = dict()
    for road in roads:
        c1, c2, weight = map(int, road)
        if visited[c1] == -1 and visited[c2] == -1:
            clusters[c1] = {c1, c2}
            visited[c1] = "C"
            visited[c2] = "C"
            regions[c1] = c1
            regions[c2] = c1
        elif visited[c1] == -1:
            region = regions[c2]
            if visited[c2] == "M":
                machine_regions[region].add(c1)
                visited[c1] = "M"
                regions[c1] = region
            else:
                clusters[region].add(c1)
                visited[c1] = "C"
                regions[c1] = region
        elif visited[c2] == -1:
            region = regions[c1]
            if visited[c1] == "M":
                machine_regions[region].add(c2)
                visited[c2] = "M"
                regions[c2] = region
            else:
                clusters[region].add(c2)
                visited[c2] = "C"
                regions[c2] = region
        else:
            if visited[c1] == "M" and visited[c2] == "M":
                time += weight
            elif visited[c1] == "M":
                cluster = clusters.pop(regions[c2])
                region = regions[c1]
                for x in cluster:
                    machine_regions[region].add(x)
                    visited[x] = "M"
                    regions[x] = region
            elif visited[c2] == "M":
                cluster = clusters.pop(regions[c1])
                region = regions[c2]
                for x in cluster:
                    machine_regions[region].add(x)
                    visited[x] = "M"
                    regions[x] = region
            else:
                cluster = clusters.pop(regions[c2])
                region = regions[c1]
                for x in cluster:
                    clusters[region].add(x)
                    regions[x] = region

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
        result = minTime(n, roads, machines)
    else:
        result = 8

    print(result)
