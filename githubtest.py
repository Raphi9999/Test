import argparse
import tkinter as tk

ap = argparse.ArgumentParser()
ap.add_argument("--test", required=False)

args = ap.parse_args()

print(args.test)
print("HeyHoy")


root = tk.Tk()
root.mainloop()