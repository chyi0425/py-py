import tkinter
import tkinter.messagebox

"""
基本上使用tkinter来开发GUI应用需要以下5个步骤
1.导入tkinter模块中我们需要的东西。
2.创建一个顶层窗口对象并用它来承载整个GUI应用
3.在顶层窗口对象上添加GUI组件
4.通过到吗将这些GUI组件的功能组织起来
5.进入主事件循环
"""
def main():
    flag = True

    # modify the text on the lable
    def change_label_text():
        nonlocal flag
        flag = not flag
        color, msg = ('red', 'Hello,world!')\
            if flag else ('blue', 'Goodbye,world!')
        label.config(text=msg,fg=color)

    # confirm quit
    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('温馨提示','确定要退出吗？'):
            top.quit

    # create the top window
    top = tkinter.Tk()
    # set the size of window
    top.geometry('240x160')
    # set the title of window
    top.title('小游戏')
    # create label and add it to top window
    label = tkinter.Label(top, text='Hello,world!',font='Arial -32',fg='red')
    label.pack(expand=1)
    # create a container for button
    panel = tkinter.Frame(top)
    # create button object specify which container to add it.
    # bind event callback function via command parameter
    button1 = tkinter.Button(panel,text='修改',command=change_label_text)
    button1.pack(side='left')
    button2 = tkinter.Button(panel,text='退出',command=confirm_to_quit)
    button2.pack(side='right')
    panel.pack(side='bottom')
    # open main loop
    tkinter.mainloop()

if __name__ == "__main__":
    main()
