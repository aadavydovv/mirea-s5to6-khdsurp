from dataclasses import dataclass


@dataclass
class Node:
    host: str
    port: int
