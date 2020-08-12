from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title("Nado GUI")

# file frame
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

btn_add_file = Button(file_frame, text="파일추가", padx=5, pady=5, width=10)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, text="선택삭제", padx=5, pady=5, width=10)
btn_del_file.pack(side="right")

# list frame
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

# save path frame
path_frame = LabelFrame(root, text="저장경로")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, ipady=4, padx=5, pady=5) #inner padding

btn_dest_path = Button(path_frame, text="찾아보기", width=10, padx=5, pady=5)
btn_dest_path.pack(side="right")

# option frame
option_frame = LabelFrame(root, text="옵션")
option_frame.pack(padx=5, pady=5, ipady=5)

#   1. width option
label_width = Label(option_frame, text="가로넓이", width=8)
label_width.pack(side="left")

option_width = ["원본유지","1024","800","640"]
combo_width = ttk.Combobox(option_frame, state="readonly", values=option_width, width=10)
combo_width.current(0)
combo_width.pack(side="left", padx=5, pady=5)

#   2. interval option
label_space = Label(option_frame, text="간격", width=8)
label_space.pack(side="left", padx=5, pady=5)

option_space = ["없음","좁게","보통","넓게"]
combo_space = ttk.Combobox(option_frame, state="readonly", values=option_space, width=10)
combo_space.current(0)
combo_space.pack(side="left", padx=5, pady=5)

#   3. file format option
label_format = Label(option_frame, text="포맷", width=8)
label_format.pack(side="left")

option_format = ["PNG","JPG","BMP"]
combo_format = ttk.Combobox(option_frame, state="readonly", values=option_format, width=10)
combo_format.current(0)
combo_format.pack(side="left")

# progress bar
prograss_frame = LabelFrame(root, text="진행상황")
prograss_frame.pack(fill="x", padx=5, pady=5, ipady=5)

p_var = DoubleVar()
prograss_var = ttk.Progressbar(prograss_frame, maximum=100, variable=p_var)
prograss_var.pack(fill="x", padx=5, pady=5)

# execute frame
run_frame = Frame(root)
run_frame.pack(fill="x", padx=5, pady=5)

btn_close = Button(run_frame, padx=5, pady=5, text="닫기", width=12, command=root.quit)
btn_close.pack(side="right")

btn_start = Button(run_frame, padx=5, pady=5, text="시작", width=12)
btn_start.pack(side="right")


root.resizable(False, False)
root.mainloop()