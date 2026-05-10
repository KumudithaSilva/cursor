def main():
    print("Hello from cursor!")
    x = 1
    y = 2
    if x < y:
        print("x is smaller")
    else:
        print("x is bigger")


class demo:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("hello " + self.name)


if __name__ == "__main__":
    d = demo("John")
    d.greet()
