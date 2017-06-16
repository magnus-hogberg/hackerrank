from io import StringIO
import sys
from os import path


def setup_input(case, n):
    file_name = "{0}/input{1}.txt".format(case, n)
    if not path.isfile(file_name):
        return False
    with open(file_name) as f:
        test_input = f.read()
    s = StringIO(test_input)
    sys.stdin = s
    return True


def setup_output():
    buf = StringIO()
    sys.stdout = buf
    return buf


def restore_stdout():
    sys.stdout = sys.__stdout__


def run_solution(case):
    sys.path.append(case)
    solution = __import__("solution")
    solution.run()


def verify_output(case, out, n):
    actual = str(out.getvalue()).strip()
    with open("{0}/expected{1}.txt".format(case, n)) as f:
        e = f.read().strip()
    return e == actual, e, actual


def main():
    case = "kangaroo"

    for n in range(10):
        if not setup_input(case, n):
            break
        out = setup_output()
        run_solution(case)
        ok, expected, actual = verify_output(case, out, n)

        restore_stdout()
        print("Test: {0}".format(n))
        if ok:
            print("OK")
        else:
            print("Result was:")
            print(actual)
            print("Expected:")
            print(expected)
        print()

if __name__ == "__main__":
    main()
