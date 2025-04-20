from collections import defaultdict, deque

def alien(words):
    adj = defaultdict(set)
    indegree = {c: 0 for word in words for c in word}
    n = len(words)
    for i in range(n-1):
        w1, w2 = words[i], words[i + 1]
        minLen = min(len(w1), len(w2))
        # Edge case: ["abc", "ab"] → invalid
        if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
            return ""
        for j in range(minLen):
            if w1[j] != w2[j]:
                if w2[j] not in adj[w1[j]]:
                    adj[w1[j]].add(w2[j])
                    indegree[w2[j]] += 1
                break

    queue = deque(c for c in indegree if indegree[c]==0)
    result = []

    while queue:
        c = queue.popleft()
        result.append(c)
        for neighbor in adj[c]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(result) < len(indegree):
        return ""  # cycle detected
    return "".join(result)


if __name__=='__main__':
    dict = ["baa", "abcd", "abca", "cab", "cad"]
    print(alien(dict))  # Possible output: bdac
