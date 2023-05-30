import tkinter
from decimal import Decimal
from tkinter import DISABLED, END, NORMAL, RIGHT


# 関数の定義
# 数字を削除する関数
def clear_number():
    screen.delete(0, END)  # screenエントリーの文字を削除
    unlock_button()


# 入力した数字の±を変換する関数
def negate():
    calculated_number = -1 * Decimal(
        screen.get()
    )  # screen.get(): screenエントリーに表示されている文字列を取得。Decimalで数値に変換
    screen.delete(0, END)  # 結果を表示するために現在のスクリーンに表示されている数字を削除
    screen.insert(0, calculated_number)  # マイナス変換した数字をscreenエントリーに挿入


def percentage():
    calculated_number = 0.01 * Decimal(screen.get())
    # 結果を表示するために現在のスクリーンに表示されている数字を削除
    screen.delete(0, END)
    screen.insert(0, calculated_number)


def add_element(number):
    screen.insert(END, number)
    # .が挿入された場合、それ以降、.を挿入できなくする処理
    if "." in screen.get():
        decimal_button.config(state=DISABLED)


# ボタンのロックを解除
def unlock_button():
    decimal_button.config(state=NORMAL)
    add_button.config(state=NORMAL)
    substract_button.config(state=NORMAL)
    multiply_button.config(state=NORMAL)
    divide_button.config(state=NORMAL)


def operate(operator):
    global operation, first_number
    # 演算の種類と入力された数字の保持
    operation = operator
    first_number = screen.get()

    print(operation, first_number)

    # 最初の数字を削除
    screen.delete(0, END)

    # =またはclearが押されるまで演算ボタンを押せなくする処理
    add_button.config(state=DISABLED)
    substract_button.config(state=DISABLED)
    multiply_button.config(state=DISABLED)
    divide_button.config(state=DISABLED)

    # 演算子のボタンが押されたときは.ボタンのロックを解除
    decimal_button.config(state=NORMAL)


# operate関数で設定した演算と数字を使って計算する関数
def calculate():
    # 演算の実行
    if operation == "add":
        calculated_number = Decimal(first_number) + Decimal(screen.get())
    elif operation == "substract":
        calculated_number = Decimal(first_number) - Decimal(screen.get())
    elif operation == "multiply":
        calculated_number = Decimal(first_number) * Decimal(screen.get())
    elif operation == "divide":
        if screen.get() == "0":
            calculated_number = "ERROR"
        else:
            calculated_number = Decimal(first_number) / Decimal(screen.get())

    # 計算結果を表示するために現在スクリーンに表示されている数字を削除
    screen.delete(0, END)
    screen.insert(0, calculated_number)

    # ボタンのロック解除
    unlock_button()


if __name__ == "__main__":
    # ウィンドウの作成
    root = tkinter.Tk()
    root.title("電卓アプリ")
    root.iconbitmap("calculator.ico")
    root.geometry("325x415")
    root.resizable(False, False)

    # 色とフォントの設定
    screen_font = ("Segoe UI", 30, "bold")
    button_font = ("Segoe UI", 20, "bold")
    light_orange = "#FFEFD5"
    light_gray = "#DCDCDC"
    orange = "#FFA500"

    # フレームの作成
    screen_frame = tkinter.LabelFrame(root)
    button_frame = tkinter.LabelFrame(root)
    screen_frame.pack(padx=2, pady=(5, 0))
    button_frame.pack(padx=2)

    # エントリーの作成
    screen = tkinter.Entry(
        screen_frame,
        width=40,
        font=screen_font,
        bg=light_orange,
        justify=RIGHT,  # 文字を右寄せ
        borderwidth=5,
    )
    screen.pack()

    # ボタンの作成　引数ありのときはlambda関数を使用
    clear_button = tkinter.Button(
        button_frame, text="C", font=button_font, bg=light_gray, command=clear_number
    )
    negate_button = tkinter.Button(
        button_frame, text="+/-", font=button_font, bg=light_gray, command=negate
    )
    percentage_button = tkinter.Button(
        button_frame, text="%", font=button_font, bg=light_gray, command=percentage
    )
    divide_button = tkinter.Button(
        button_frame,
        text="÷",
        font=button_font,
        bg=orange,
        command=lambda: operate("divide"),
    )
    seven_button = tkinter.Button(
        button_frame,
        text="7",
        font=button_font,
        bg="black",
        fg="white",
        command=lambda: add_element(7),
    )
    eight_button = tkinter.Button(
        button_frame,
        text="8",
        font=button_font,
        bg="black",
        fg="white",
        command=lambda: add_element(8),
    )
    nine_button = tkinter.Button(
        button_frame,
        text="9",
        font=button_font,
        bg="black",
        fg="white",
        command=lambda: add_element(9),
    )
    multiply_button = tkinter.Button(
        button_frame,
        text="x",
        font=button_font,
        bg=orange,
        command=lambda: operate("multiply"),
    )
    four_button = tkinter.Button(
        button_frame,
        text="4",
        font=button_font,
        bg="black",
        fg="white",
        command=lambda: add_element(4),
    )
    five_button = tkinter.Button(
        button_frame,
        text="5",
        font=button_font,
        bg="black",
        fg="white",
        command=lambda: add_element(5),
    )
    six_button = tkinter.Button(
        button_frame,
        text="6",
        font=button_font,
        bg="black",
        fg="white",
        command=lambda: add_element(6),
    )
    substract_button = tkinter.Button(
        button_frame,
        text="-",
        font=button_font,
        bg=orange,
        command=lambda: operate("substract"),
    )
    one_button = tkinter.Button(
        button_frame,
        text="1",
        font=button_font,
        bg="black",
        fg="white",
        command=lambda: add_element(1),
    )
    two_button = tkinter.Button(
        button_frame,
        text="2",
        font=button_font,
        bg="black",
        fg="white",
        command=lambda: add_element(2),
    )
    three_button = tkinter.Button(
        button_frame,
        text="3",
        font=button_font,
        bg="black",
        fg="white",
        command=lambda: add_element(3),
    )
    add_button = tkinter.Button(
        button_frame,
        text="+",
        font=button_font,
        bg=orange,
        command=lambda: operate("add"),
    )
    zero_button = tkinter.Button(
        button_frame,
        text="0",
        font=button_font,
        bg="black",
        fg="white",
        command=lambda: add_element(0),
    )
    decimal_button = tkinter.Button(
        button_frame,
        text=".",
        font=button_font,
        bg="black",
        fg="white",
        command=lambda: add_element("."),
    )
    equal_button = tkinter.Button(
        button_frame, text="=", font=button_font, bg=orange, command=calculate
    )

    # 1行目の配置 pady: 外側の縦の隙間を指定
    clear_button.grid(row=0, column=0, sticky="WE", pady=1)  # sticky W:左、E:右
    negate_button.grid(row=0, column=1, sticky="WE", pady=1)
    percentage_button.grid(row=0, column=2, sticky="WE", pady=1)
    divide_button.grid(row=0, column=3, sticky="WE", pady=1)

    # 2行目の配置 ipadx: 内側の横の隙間を指定
    seven_button.grid(row=1, column=0, sticky="WE", ipadx=20, pady=1)
    eight_button.grid(row=1, column=1, sticky="WE", ipadx=20, pady=1)
    nine_button.grid(row=1, column=2, sticky="WE", ipadx=20, pady=1)
    multiply_button.grid(row=1, column=3, sticky="WE", ipadx=20, pady=1)

    # 3行目の配置
    four_button.grid(row=2, column=0, sticky="WE", pady=1)
    five_button.grid(row=2, column=1, sticky="WE", pady=1)
    six_button.grid(row=2, column=2, sticky="WE", pady=1)
    substract_button.grid(row=2, column=3, sticky="WE", pady=1)

    # 4行目の配置
    one_button.grid(row=3, column=0, sticky="WE", pady=1)
    two_button.grid(row=3, column=1, sticky="WE", pady=1)
    three_button.grid(row=3, column=2, sticky="WE", pady=1)
    add_button.grid(row=3, column=3, sticky="WE", pady=1)

    # 5行目の配置
    zero_button.grid(row=4, column=0, sticky="WE", columnspan=2, pady=1)
    decimal_button.grid(row=4, column=2, sticky="WE", pady=1)
    equal_button.grid(row=4, column=3, sticky="WE", pady=1)

    # ウィンドウのループ処理
    root.mainloop()
