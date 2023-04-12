import tkinter as tk
import tkinter.ttk as ttk


class SUI:
    def __init__(self, pack_name, font=('Terminal', 8), font_big=('Terminal', 25)):
        self.app = tk.Tk()
        self.groups = tk.Frame(self.app)
        self.packages = tk.Frame(self.app)
        self.packages_val = []
        butt = ttk.Style()
        butt.configure('my.TButton', font=font)
        check = ttk.Style()
        check.configure('my.TCheckbutton', font=font)
        ttk.Label(self.app, text=pack_name, font=font_big).pack(anchor='center')
        self.app.title(pack_name)
        self.groups.pack(anchor='center')
        self.packages.pack(anchor='center')

    def set_code(self, code):
        for i, c in zip(self.packages_val, code):
            if not i[2]:
                i[0].set(c)

    def add_group(self, name, code):
        ttk.Label(self.groups).pack(side='left')
        ttk.Button(self.groups, text=name, style='my.TButton',
                   command=lambda x=code: self.set_code(x)).pack(side='left')

    def add_package(self, name, pack, value=True, disabled=False):
        self.packages_val.append([tk.IntVar(), pack, disabled])
        name = name + ' (' + pack + ')'
        chk = ttk.Checkbutton(self.packages, text=name, variable=self.packages_val[-1][0],
                              onvalue=1, offvalue=0, style='my.TCheckbutton')
        self.packages_val[-1][0].set(int(value))
        if disabled:
            chk.config(state='disabled')
        chk.pack()

    def get_user_data(self, close_name='Install'):
        ttk.Button(self.app, text=close_name, command=self.app.destroy, style='my.TButton').pack()
        self.app.mainloop()
        data = []
        for i in self.packages_val:
            if i[0].get():
                data.append(i[1])
        return {'packages': data}
