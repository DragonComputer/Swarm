import sys

class Ribosome:

    def __init__(self, filename):
        self.variables = []

        with open(filename) as f:
            program = ''.join(line.strip() for line in f)
            print program


if __name__ == "__main__":
    Ribosome(sys.argv[1])
