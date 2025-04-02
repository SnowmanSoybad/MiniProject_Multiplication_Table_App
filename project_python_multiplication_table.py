import tkinter as tk 

def show_output():  # ฟังก์ชันสำหรับแสดงผลลัพธ์สูตรคูณ
    number = int(number_input.get())  # ดึงข้อความที่เรากรอกไปแล้วนำมาใช้ได้ 
    
    output = ""  # กำหนดตัวแปรสำหรับเก็บข้อความผลลัพธ์
    for i in range(1, 13):  
        output += str(number) + " x " + str(i)  # สร้างข้อความสูตรคูณ
        output += " = " + str(number * i) + "\n"  # คำนวณผลลัพธ์และขึ้นบรรทัดใหม่
    
    output_label.configure(text=output)  # แสดงผลลัพธ์ใน Label

# สร้างหน้าต่างหลักของโปรแกรม
window = tk.Tk()
window.title("JustPython")  # ตั้งชื่อหน้าต่าง
window.minsize(width=400, height=400)  # กำหนดขนาดขั้นต่ำของหน้าต่าง

# สร้างป้ายข้อความหัวข้อ
title_label = tk.Label(master=window, text="สูตรคูณแม่")
title_label.pack(pady=20) 

# สร้างช่องป้อนค่าตัวเลข
number_input = tk.Entry(master=window, width=15)
number_input.pack()

# สร้างปุ่มกดเพื่อคำนวณสูตรคูณ
go_button = tk.Button(
    master=window, text="ได้แก่",  # ข้อความบนปุ่ม
    command=show_output, width=9, height=2  # กำหนดขนาดของปุ่มและกำหนดให้กดแล้วเรียก show_output()
)
go_button.pack()

# สร้างป้ายข้อความสำหรับแสดงผลลัพธ์สูตรคูณ
output_label = tk.Label(master=window)
output_label.pack(pady=20)  # จัดตำแหน่งและเพิ่มระยะห่าง


window.mainloop()  # star แอป
