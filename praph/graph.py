import collections
from typing import Any


class Graph(object):
    _directed: bool
    _graph: dict
    _weights: dict
    _labels: dict

    def __init__(self, directed: bool = True):
        self._graph = collections.defaultdict(list)
        self._weights = dict()
        self._labels = dict()
        self._directed = directed

    @property
    def vertices(self) -> list:
        return list(self._graph.keys())

    def get_label(self, vertex: int) -> Any:
        return self._labels[vertex]

    def set_label(self, vertex: int, label: Any) -> None:
        self._labels[vertex] = label

    def get_weight(self, edge: tuple) -> Any:
        return self._weights[edge]

    def set_weight(self, edge: tuple, weight: Any) -> None:
        self._weights[edge] = weight

    def successors(self, vertex: int) -> list:
        return self._graph[vertex]

    def add_vertex(self, vertex: int, label: Any = None) -> None:
        self._graph[vertex] += []

        if label:
            self._labels[vertex] = label

    def add_edge(self, edge: tuple, weight: Any = None) -> None:
        e1 = edge[0]
        e2 = edge[1]

        self._graph[e1].append(e2)

        if self._directed:
            self._graph[e2] += []
        else:
            self._graph[e2].append(e1)

        if weight:
            self._weights[edge] = weight
