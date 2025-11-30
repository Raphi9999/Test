import argparse
import tkinter as tk

ap = argparse.ArgumentParser()
ap.add_argument("--test", required=True)
ap.add_argument("--text", required=True)

args = ap.parse_args()



root = tk.Tk()
root.title(args.text + args.test)

text = tk.Label(root, text=args.text)
root.mainloop()