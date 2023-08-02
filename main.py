import json
import random
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog


class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_data()

    def load_data(self):
        try:
            with open('data.json', 'r') as file:
                self.accounts = json.load(file)
                print(self.accounts)
        except FileNotFoundError:
            pass

    def save_data(self):
        with open('data.json', 'w') as file:
            json.dump(self.accounts, file)

    def create_account(self, username, password, initial_balance = 0):
        if username not in self.accounts:
            if initial_balance >= 0:
                self.accounts[username] = {'password': password, 'balance': initial_balance, 'transactions': []}
                self.save_data()
                messagebox.showinfo("账户创建成功", f"用户{username}的账户已创建，初始余额为{initial_balance}元。")
            else:
                messagebox.showerror("错误", "初始余额不能为负数。")
        else:
            messagebox.showerror("错误", f"用户{username}已存在。")

    def authenticate(self, username, password):
        print("chenggongdiaoyong")
        print("ok", username, password)
        # print(self.accounts[username]['password'], password)
        if username in self.accounts:
            if self.accounts[username]['password'] == password:
                return True
        return False

    def deposit(self, username, amount):
        if username in self.accounts:
            if amount >= 10:
                service_fee = amount * 0.5
                roll = random.randint(1, 5)
                print(roll)
                if roll == 1:
                    success = True
                else:
                    success = False

                # success = random.randint(1, 5) == 1
                # print(random.randint(1, 5))

                if success:
                    self.accounts[username]['balance'] += amount
                    self.accounts[username]['transactions'].append(f"存款：+{amount}元")
                    self.accounts[username]['balance'] -= service_fee
                    self.accounts[username]['transactions'].append(f"服务费：-{service_fee}元")
                    messagebox.showinfo("存款成功",
                                        f"用户{username}存款成功！存款金额为{amount}元，服务费为{service_fee}元。")
                else:
                    self.accounts[username]['transactions'].append(f"存款失败：手续费-{service_fee}元")
                    messagebox.showinfo("存款失败",
                                        f"用户{username}存款失败！存款金额不计入账户，服务费为{service_fee}元。")

                self.save_data()

            else:
                messagebox.showerror("错误", "存款金额不能小于10元。")
        else:
            messagebox.showerror("错误", f"用户{username}不存在。")

    def withdraw(self, username, amount):
        if username in self.accounts:
            if amount >= 0:
                service_fee = amount * 0.5
                verification_code = random.randint(0, 5)
                print(verification_code)
                success = False

                while True:
                    input_code = tk.simpledialog.askinteger("取款", "请输入校验码（0-5）")
                    if input_code == verification_code:
                        success = True
                        break
                    else:
                        # messagebox.showerror("错误", "校验码错误，请重新输入或放弃取款。")
                        self.accounts[username]['balance'] -= service_fee
                        result = messagebox.askyesno("错误",
                                                     f"校验码错误，请重新输入或放弃取款。\n手续费已从余额扣除，当前余额{self.accounts[username]['balance']}元。")
                        if result == True:
                            continue
                        else:
                            break

                if success:
                    self.accounts[username]['balance'] -= amount
                    self.accounts[username]['transactions'].append(f"取款：-{amount}元")
                    self.accounts[username]['balance'] -= service_fee
                    self.accounts[username]['transactions'].append(f"服务费：-{service_fee}元")
                else:
                    self.accounts[username]['transactions'].append(f"取款失败")

                self.save_data()

                if success:
                    messagebox.showinfo("取款成功",
                                        f"用户{username}取款成功！取款金额为{amount}元，服务费为{service_fee}元。")
                else:
                    messagebox.showinfo("取款失败", f"用户{username}取款失败！服务费为{service_fee}元。")
            else:
                messagebox.showerror("错误", "取款金额不能为负数。")
        else:
            messagebox.showerror("错误", f"用户{username}不存在。")

    def query_balance(self, username):
        if username in self.accounts:
            balance = self.accounts[username]['balance']
            messagebox.showinfo("账户余额", f"用户{username}的账户余额为{balance}元。")
        else:
            messagebox.showerror("错误", f"用户{username}不存在。")

    def print_transactions(self, username):
        if username in self.accounts:
            transactions = self.accounts[username]['transactions']
            messagebox.showinfo("交易记录", f"用户{username}的交易记录：\n" + "\n".join(transactions))
        else:
            messagebox.showerror("错误", f"用户{username}不存在。")


# 创建Bank对象
bank = Bank()


def login():
    username = username_entry.get()
    password = password_entry.get()
    print(username, password, "def login")

    if bank.authenticate(username, password):
        messagebox.showinfo("登录成功", f"欢迎回来，{username}！")
        login_frame.pack_forget()
        main_menu_frame.pack()
    else:
        messagebox.showerror("登录失败", "用户名或密码错误。")


def create_account():
    username = username_entry.get()
    password = password_entry.get()
    initial_balance = initial_balance_entry.get()

    if initial_balance.isnumeric():
        bank.create_account(username, password, int(initial_balance))
        create_account_frame.pack_forget()
        login_frame.pack()
    else:
        messagebox.showerror("错误", "初始余额必须为数字。")


def show_create_account_frame():
    login_frame.pack_forget()
    create_account_frame.pack()


def exit_app():
    if messagebox.askyesno("退出", "确定要退出吗？"):
        root.destroy()


root = tk.Tk()
root.title("银行系统")
root.geometry("300x200")

login_frame = tk.Frame(root)
login_frame.pack()

username_label = tk.Label(login_frame, text = "用户名：")
username_label.grid(row = 0, column = 0)

username_entry = tk.Entry(login_frame)
username_entry.grid(row = 0, column = 1)

password_label = tk.Label(login_frame, text = "密码：")
password_label.grid(row = 1, column = 0)

password_entry = tk.Entry(login_frame, show = "*")
password_entry.grid(row = 1, column = 1)

login_button = tk.Button(login_frame, text = "登录", command = login)
login_button.grid(row = 2, column = 0, columnspan = 2, pady = 10)

create_account_button = tk.Button(login_frame, text = "创建账户", command = show_create_account_frame)
create_account_button.grid(row = 3, column = 0, columnspan = 2)

create_account_frame = tk.Frame(root)

username_label = tk.Label(create_account_frame, text = "用户名：")
username_label.grid(row = 0, column = 0)

username_entry = tk.Entry(create_account_frame)
username_entry.grid(row = 0, column = 1)

password_label = tk.Label(create_account_frame, text = "密码：")
password_label.grid(row = 1, column = 0)

password_entry = tk.Entry(create_account_frame, show = "*")
password_entry.grid(row = 1, column = 1)

initial_balance_label = tk.Label(create_account_frame, text = "初始余额：")
initial_balance_label.grid(row = 2, column = 0)

initial_balance_entry = tk.Entry(create_account_frame)
initial_balance_entry.grid(row = 2, column = 1)

create_account_button = tk.Button(create_account_frame, text = "创建账户", command = create_account)
create_account_button.grid(row = 3, column = 0, columnspan = 2, pady = 10)

main_menu_frame = tk.Frame(root)


def deposit():
    amount = simpledialog.askfloat("存款", "请输入存款金额")
    if amount is not None:
        bank.deposit(username_entry.get(), amount)


def withdraw():
    amount = simpledialog.askfloat("取款", "请输入取款金额")
    if amount is not None:
        bank.withdraw(username_entry.get(), amount)


deposit_button = tk.Button(main_menu_frame, text = "存款", command = deposit)
withdraw_button = tk.Button(main_menu_frame, text = "取款", command = withdraw)

# deposit_button = tk.Button(main_menu_frame, text="存款", command=lambda: bank.deposit(username_entry.get(), 50))
deposit_button.pack(pady = 10)

# withdraw_button = tk.Button(main_menu_frame, text="取款", command=lambda: bank.withdraw(username_entry.get(), 30))
withdraw_button.pack(pady = 10)

query_balance_button = tk.Button(main_menu_frame, text = "查询余额",
                                 command = lambda: bank.query_balance(username_entry.get()))
query_balance_button.pack(pady = 10)

print_transactions_button = tk.Button(main_menu_frame, text = "打印交易记录",
                                      command = lambda: bank.print_transactions(username_entry.get()))
print_transactions_button.pack(pady = 10)

exit_button = tk.Button(main_menu_frame, text = "退出", command = exit_app)
exit_button.pack(pady = 10)

login_frame.pack()

root.mainloop()
