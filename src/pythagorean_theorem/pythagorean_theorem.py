import tkinter as tk
from tkinter import messagebox
import math

# ****************************************************************
#                           関数
# ****************************************************************
# 斜辺の計算関数
def calculate_hypotenuse():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = math.sqrt(a**2 + b**2)
        result_label.config(text=f"斜辺の長さ: {c:.2f}")
        update_triangle_labels(a, b, c)
    except ValueError:
        messagebox.showerror("入力エラー", "数値を入力してください")

# 底辺の計算関数
def calculate_side():
    try:
        c = float(entry_c.get())
        # aを計算 ... b,cから
        if entry_a.get() == "" and entry_b.get() != "":
            b = float(entry_b.get())
            if c <= b:
                messagebox.showerror("入力エラー", "斜辺は他の辺より長くする必要があります")
                return
            a = math.sqrt(c**2 - b**2)
            result_label.config(text=f"他の辺の長さ (a): {a:.2f}")
            update_triangle_labels(a, b, c)
        # bを計算 ... a,cから
        elif entry_b.get() == "" and entry_a.get() != "":
            a = float(entry_a.get())
            if c <= a:
                messagebox.showerror("入力エラー", "斜辺は他の辺より長くする必要があります")
                return
            b = math.sqrt(c**2 - a**2)
            result_label.config(text=f"他の辺の長さ (b): {b:.2f}")
            update_triangle_labels(a, b, c)
        else:
            messagebox.showerror("入力エラー", "適切な辺の組み合わせを入力してください")
    except ValueError:
        messagebox.showerror("入力エラー", "数値を入力してください")

def update_triangle_labels(a, b, c):
    # 各辺の長さを更新
    canvas.itemconfig(label_a, text=f"a: {a:.2f}")
    canvas.itemconfig(label_b, text=f"b: {b:.2f}")
    canvas.itemconfig(label_c, text=f"c: {c:.2f}")

# ****************************************************************
#                           GUI
# ****************************************************************
# ウィンドウの作成
root = tk.Tk()
root.title("三平方の定理 計算ツール")
root.configure(bg="#E5D0FF")

# フレームの作成
frame = tk.Frame(root, bg="#E5D0FF")
frame.pack(padx=10, pady=10)

# ラベルとエントリの配置
label_a = tk.Label(frame, text="辺 a:", font=("Arial", 16), bg="#E5D0FF", fg="#A020F0")
label_a.grid(row=0, column=0)
entry_a = tk.Entry(frame, font=("Arial", 16), width=10, bg="#F3E8FF")
entry_a.grid(row=0, column=1)

label_b = tk.Label(frame, text="辺 b:", font=("Arial", 16), bg="#E5D0FF", fg="#A020F0")
label_b.grid(row=1, column=0)
entry_b = tk.Entry(frame, font=("Arial", 16), width=10, bg="#F3E8FF")
entry_b.grid(row=1, column=1)

label_c = tk.Label(frame, text="斜辺 c:", font=("Arial", 16), bg="#E5D0FF", fg="#A020F0")
label_c.grid(row=2, column=0)
entry_c = tk.Entry(frame, font=("Arial", 16), width=10, bg="#F3E8FF")
entry_c.grid(row=2, column=1)

# 計算ボタン
button_hypotenuse = tk.Button(frame, text="斜辺を計算", command=calculate_hypotenuse, font=("Arial", 14), bg="#DDA0DD", fg="white")
button_hypotenuse.grid(row=3, column=0, pady=5)

button_side = tk.Button(frame, text="他の辺を計算", command=calculate_side, font=("Arial", 14), bg="#DDA0DD", fg="white")
button_side.grid(row=3, column=1, pady=5)

# 結果表示ラベル
result_label = tk.Label(root, text="結果がここに表示されます", font=("Arial", 16), bg="#E5D0FF", fg="#A020F0")
result_label.pack(pady=10)

# 三角形描画用キャンバス
canvas = tk.Canvas(root, width=400, height=300, bg="#F3E8FF", highlightthickness=0)
canvas.pack(pady=10)

# 三角形のあらかじめ描画
x1, y1 = 50, 250
x2, y2 = x1, y1 - 150
x3, y3 = x1 + 200, y1
canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill="#E5D0FF", outline="#A020F0", width=2)

# 辺のラベルを追加（初期状態では空）
label_a = canvas.create_text((x1 + x2) / 2 - 10, (y1 + y2) / 2, text="", fill="#A020F0", font=("Arial", 12))
label_b = canvas.create_text((x1 + x3) / 2, y1 + 10, text="", fill="#A020F0", font=("Arial", 12))
label_c = canvas.create_text((x2 + x3) / 2 + 10, (y2 + y3) / 2, text="", fill="#A020F0", font=("Arial", 12))
# ****************************************************************

# メインループの開始
root.mainloop()