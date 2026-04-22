def closetTarget(words, target, startIndex):
    n = len(words)
    min_distance = float('inf')

    for i in range(n):
        if words[i] == target:
            # forward distance
            forward = abs(i - startIndex)

            # circular shortest distance
            distance = min(forward, n - forward)

            min_distance = min(min_distance, distance)

    return -1 if min_distance == float('inf') else min_distance