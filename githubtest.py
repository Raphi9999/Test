import argparse

ap = argparse.ArgumentParser()
ap.add_argument("--test", required=False)

args = ap.parse_args()

print(args.test)
