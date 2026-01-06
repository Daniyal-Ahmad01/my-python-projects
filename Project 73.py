class ScoreTracker:
    def __init__(self, points):
        self.points = points
    def __add__(self, other):
        return ScoreTracker(self.points + other.points)
    def __lt__(self, other):
        return self.points < other.points
    def __gt__(self, other):
        return self.points > other.points
    def __str__(self):
        return f"ScoreTracker(points={self.points})"
a = ScoreTracker(55)
b = ScoreTracker(67)
c=a+b
print(a + b)
print(c)