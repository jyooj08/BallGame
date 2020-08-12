import os
from tkinter import *
import tkinter.ttk as ttk
from tkinter import filedialog
import tkinter.messagebox as msbox
from PIL import Image

root = Tk()
root.title("Nado GUI")

# file frame
def add_file():
    files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요", \
        filetypes=(("PNG 파일", "*.png"), ("모든 파일", "*.*")), \
        initialdir="C:/Users/User/Desktop/Python/gui_project") #최초 보여줄 경로
    
    for f in files:
        list_file.insert(END, f)

def del_file():
    for idx in reversed(list_file.curselection()):
        list_file.delete(idx)

file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

btn_add_file = Button(file_frame, text="파일추가", padx=5, pady=5, width=10, command=add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, text="선택삭제", padx=5, pady=5, width=10, command=del_file)
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
def browse_dest_path():
    selected_folder = filedialog.askdirectory()
    if selected_folder == '':
        return
    
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, selected_folder)

path_frame = LabelFrame(root, text="저장경로")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, ipady=4, padx=5, pady=5) #inner padding

btn_dest_path = Button(path_frame, text="찾아보기", width=10, padx=5, pady=5, command=browse_dest_path)
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
progress_bar = ttk.Progressbar(prograss_frame, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)

def merge_image():
    try:
        img_width = combo_width.get()
        if img_width == "원본유지":
            img_width = -1
        else:
            img_width = int(img_width)
        
        img_space = combo_space.get()
        if img_space == "좁게":
            img_space = 30
        elif img_space == "보통":
            img_space = 60
        elif img_space == "넓게":
            img_space = 90
        else:
            img_space = 0
        
        img_format = combo_format.get().lower()

        ####################################################3

        images = [Image.open(x) for x in list_file.get(0,END)]

        img_sizes = []
        if img_width > -1:
            img_sizes = [(int(img_width), int(img_width * x.size[1] / x.size[0])) for x in images]
        else:
            img_sizes = [(x.size[0], x.size[1]) for x in images]

        widths, heights = zip(*(img_sizes))

        max_width, max_height = max(widths), sum(heights)
        
        # 스케치북 준비
        if img_space > 0:
            max_height += (img_space * (len(images)-1))

        result_img = Image.new("RGB", (max_width, max_height), (255,255,255))
        y_offset = 0

        for idx, img in enumerate(images):
            if img_width > -1:
                img = img.resize(img_sizes[idx])
            result_img.paste(img, (0,y_offset))
            y_offset += (img.size[1] + img_space)

            progress = (idx + 1) / len(images) * 100
            p_var.set(progress)
            progress_bar.update()

        file_name = "nado_photo."+img_format
        dest_path = os.path.join(txt_dest_path.get(), file_name)
        result_img.save(dest_path)
        msbox.showinfo("알림", "작업이 완료되었습니다.")
    except Exception as err:
        msbox.showerror("에러", err)

# execute frame
def start():
    # get each option
    # print("가로넓이 ", combo_width.get())
    # print("간격 ", combo_space.get())
    # print("포맷 ", combo_format.get())

    if list_file.size() == 0:
        msbox.showwarning("경고", "이미지 파일을 추가하세요")
        return
    if len(txt_dest_path.get()) == 0:
        msbox.showwarning("경고", "저장 경로를 선택하세요")
        return

    merge_image()

run_frame = Frame(root)
run_frame.pack(fill="x", padx=5, pady=5)

btn_close = Button(run_frame, padx=5, pady=5, text="닫기", width=12, command=root.quit)
btn_close.pack(side="right")

btn_start = Button(run_frame, padx=5, pady=5, text="시작", width=12, command=start)
btn_start.pack(side="right")


root.resizable(False, False)
root.mainloop()