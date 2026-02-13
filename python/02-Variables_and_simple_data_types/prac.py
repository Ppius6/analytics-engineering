from collections import namedtuple, Counter, defaultdict
from dataclasses import dataclass


# Track user visits
@dataclass
class User:
    user_id: int
    name: str


Visit = namedtuple("Visit", ["user_id", "page", "timestamp"])

visits = [
    Visit(1, "/home", "2024-01-01"),
    Visit(2, "/about", "2024-01-01"),
    Visit(1, "/products", "2024-01-02"),
    Visit(1, "/home", "2024-01-02"),
]

# Count page visits
page_visits = Counter(visit.page for visit in visits)
print(page_visits)

# Group visits by user
user_visits = defaultdict(list)
for visit in visits:
    user_visits[visit.user_id].append(visit)
print(user_visits[1])
