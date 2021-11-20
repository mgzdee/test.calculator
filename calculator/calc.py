import sys

def read_args():
    args = sys.argv
    return args[1]

def compute(string_inp = None):
    if string_inp is None:
        string_inp = read_args()
        return eval(string_inp)

def main():
    print(compute())

if __name__ == "__main__":
    main()