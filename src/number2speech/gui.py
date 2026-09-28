"""
图形界面实现，就两个按钮
"""

import threading
import tkinter as tk
from tkinter import ttk

from . import audio
from .converter import digits_to_chinese,num_to_chinese

class App:
    def __init__(self,root):
        self.root = root
        self.player = audio.Player

        root.title("数字文本转语言")
        root.resizable(False,False)

        frm = ttk.Frame(root,padding=14)
        frm.grid(sticky="nsew")

        ttk.Label(frm, text="输入数字文本：").grid(row=0, column=0, sticky="w")
        self.entry = ttk.Entry(frm, width=34)
        self.entry.grid(row=1, column=0, columnspan=4, sticky="we", pady=(2, 8))
        self.entry.insert(0, "2382")

        self.var_mode = tk.BooleanVar(value=False)
        ttk.Checkbutton(frm, text="逐位读（手机号：二三八二）",
                        variable=self.var_mode).grid(row=2, column=0, columnspan=2, sticky="w")

        ttk.Label(frm, text="片段间隔(秒)：").grid(row=2, column=2, sticky="e")
        self.var_gap = tk.DoubleVar(value=0.0)
        ttk.Spinbox(frm, from_=0.0, to=0.5, increment=0.02, width=5,
                    textvariable=self.var_gap).grid(row=2, column=3, sticky="w")

        self.lbl_result = ttk.Label(frm, text="", foreground="#185FA5", wraplength=310)
        self.lbl_result.grid(row=3, column=0, columnspan=4, sticky="w", pady=(8, 6))

        btns = ttk.Frame(frm)
        btns.grid(row=4, column=0, columnspan=4, sticky="we")
        ttk.Button(btns, text="朗读", command=self.on_play).pack(side="left")
        ttk.Button(btns, text="停止", command=self.player.stop).pack(side="left", padx=6)

        self.entry.focus_set()

    # ---- 事件 ----
    def _reading(self):
        raw = self.entry.get()
        return digits_to_chinese(raw) if self.var_mode.get() else num_to_chinese(raw)

    def on_play(self):
        try:
            cn = self._reading()
        except ValueError as e:  # 超出 int 上限：红字提示，不播放
            self.lbl_result.config(text=str(e), foreground="#993C1D")
            return
        self.lbl_result.config(foreground="#185FA5",
                               text=("读法：" + cn) if cn else "（没有可读的数字）")
        if not cn:
            return
        gap = float(self.var_gap.get() or 0)
        threading.Thread(target=self.player.play, args=(cn, gap), daemon=True).start()

def run_gui():
    root = tk.Tk()
    App(root)
    root.mainloop()


def main():
    run_gui()


if __name__ == "__main__":
    main()