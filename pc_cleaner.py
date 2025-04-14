import os
import tkinter as tk
from tkinter import messagebox

# ألوان ثابتة
BG_COLOR = "#f0f0f0"
BTN_COLOR = "#007ACC"
TEXT_COLOR = "white"
FONT = ("Cairo", 12)

# دوال الأزرار
def clean_temp():
    try:
        os.system('del /f /s /q %temp%\\*')
        os.system('rd /s /q %temp%')
        os.makedirs(os.environ['TEMP'], exist_ok=True)
        messagebox.showinfo("تم", "✅ تم تنظيف ملفات TEMP بنجاح.")
    except Exception as e:
        messagebox.showerror("خطأ", str(e))

def restart_pc():
    os.system("shutdown /r /t 0")

def shutdown_pc():
    os.system("shutdown /s /t 0")

def clean_system_cache():
    try:
        os.system("cleanmgr /sagerun:1")
        messagebox.showinfo("تم", "✅ تم تشغيل تنظيف النظام.")
    except Exception as e:
        messagebox.showerror("خطأ", str(e))

# إنشاء النافذة
root = tk.Tk()
root.title("منظف الكمبيوتر - Mohammed Hamza")
root.geometry("350x400")
root.configure(bg=BG_COLOR)
root.resizable(False, False)

# عنوان باسمك
title = tk.Label(root, text="🧹 منظف الكمبيوتر", font=("Cairo", 16, "bold"), bg=BG_COLOR, fg="#333")
title.pack(pady=(20,5))

subtitle = tk.Label(root, text="by Mohammed Hamza", font=("Cairo", 11), bg=BG_COLOR, fg="#666")
subtitle.pack(pady=(0,20))

# أزرار الوظائف
def create_button(text, command):
    return tk.Button(root, text=text, command=command, height=2, width=30, bg=BTN_COLOR, fg=TEXT_COLOR, font=FONT, relief="ridge")

create_button("🗑️ تنظيف ملفات TEMP", clean_temp).pack(pady=10)
create_button("🧼 تنظيف كاش النظام", clean_system_cache).pack(pady=10)
create_button("🔄 إعادة تشغيل الجهاز", restart_pc).pack(pady=10)
create_button("⏻ إيقاف التشغيل", shutdown_pc).pack(pady=10)

# تشغيل النافذة
root.mainloop()
