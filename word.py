import argparse
parser = argparse.ArgumentParser()
parser.add_argument("file")
arg = parser.parse_args()
print(arg.file)
parser.add_argument()