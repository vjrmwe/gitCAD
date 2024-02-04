import tkinter as tk
from tkinter.filedialog import askdirectory
import os

def run():
    root = tk.Tk()
    root.title('gitCAD')

    global path
    path = tk.StringVar()
    path.set(os.path.abspath("."))

    tk.Label(root, text="目标路径:").grid(row=0, column=0)
    tk.Entry(root, textvariable=path, state="readonly").grid(row=0, column=1, ipadx=200)
    tk.Button(root, text="选择文件夹", command=selectPath).grid(row=0, column=2)
    root.mainloop()

def selectPath():
    path_ = askdirectory() #使用askdirectory()方法返回文件夹的路径
    if path_ == "":
        path.get() #当打开文件路径选择框后点击"取消" 输入框会清空路径，所以使用get()方法再获取一次路径
    else:
        path_ = path_.replace("/", "\\")  # 实际在代码中执行的路径为“\“ 所以替换一下
        path.set(path_)
