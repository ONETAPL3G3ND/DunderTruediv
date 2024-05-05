class Div:
    def __init__(self, value):
        self.value = value

    def __truediv__(self, other):
        return int(self.value / other)

if __name__ == "__main__":
    v = Div(4)
    print(v / 2)