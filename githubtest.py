import argparse
import tkinter as tk

ap = argparse.ArgumentParser()
ap.add_argument("--test", required=True)
ap.add_argument("--text", required=True)

args = ap.parse_args()

print(args.test)
print("HeyHoy")


root = tk.Tk()


text = tk.Label(root, text=args.text)
root.mainloop()