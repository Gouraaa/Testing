import tkinter as tk 
import time

def print_lirik(interval):
    lirik = [
        'Aku Muak :(',
        '"Katanya Cinta Sedalam Samudra"',
        '"Bohong Nyata Kita Berakhir Juga"',
        '"Muuaaaakkk"'
    ]
    for baris in lirik:
        listbox.insert(tk.END, baris)
        root.update()
        time.sleep(interval)

root = tk.Tk()
root.title(" A S I N G ")
root.geometry("400x300")

listbox = tk.Listbox(root)
listbox.pack(fill=tk.BOTH, expand=True)

if __name__ == '__main__':
    interval = 5
    print_lirik(interval)
    root.mainloop()