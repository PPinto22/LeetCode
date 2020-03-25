# FIXME: Runtime Error on the 2nd test case


class TrieNode:
    def __init__(self, data=None):
        # char -> TrieNode
        self.edges = dict()
        # nr. of strings that end in this node
        self.count = 0
        # nr. of strings that share this prefix
        # i.e., count + number of children
        self.prefixes = 0

    def add(self, string):
        current = self
        for char in string:
            if char not in current.edges:
                current.edges[char] = TrieNode()
            current = current.edges[char]
            current.prefixes += 1
        current.count += 1


def solve(N, K, strings):
    trie_root = init_trie(strings)
    score, _ = propagate(trie_root, group_size=K, depth=0)
    return score


def init_trie(strings):
    root = TrieNode()
    for string in strings:
        root.add(string)
    return root


def propagate(trie_node, group_size, depth=0):
    # Recursively group strings in the children nodes and get the total score and the nr of strings left ungrouped
    children_results = map(lambda node: propagate(node, group_size, depth + 1), trie_node.edges.values()) \
        if trie_node.edges else [(0, 0)]
    children_score, children_excess = map(sum, zip(*children_results))
    # Now group strings in the current node
    curr_count = trie_node.count + children_excess
    curr_groups = curr_count // group_size
    curr_excess = curr_count % group_size
    curr_score = curr_groups * depth
    return curr_score + children_score, curr_excess


if __name__ == '__main__':
    T = int(input())
    for Ti in range(1, T + 1):
        # N: Strings; K: Group size
        N, K = map(int, input().split())
        strings = [input() for _ in range(N)]
        result = solve(N, K, strings)
        print('Case #{}: {}'.format(Ti, result), flush=True)
