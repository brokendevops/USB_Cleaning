import subprocess
import os
import string
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


def suruculeri_getir():
    mevcutlar = []
    for harf in string.ascii_uppercase:
        if os.path.exists(f"{harf}:\\"):
            mevcutlar.append(f"{harf}:")
    return mevcutlar

def temizle_usb():
    surucu = surucu_var.get()
    if not surucu:
        messagebox.showerror("Hata","Lütfen bir sürücü seçin.")
        return
    try:
        komutlar = [
            f'attrib -h -r -s /s /d {surucu}\\*.*',
            f'del /f /s /q {surucu}\\autorun.inf',
            f'del /f /s /q {surucu}\\*.vbs',
            f'del /f /s /q {surucu}\\*.lnk',
            f'del /f /s /q {surucu}\\*.bat',
            f'del /f /s /q {surucu}\\*.dat',
            f'del /f /s /q {surucu}\\desktop.ini',
            f'rmdir /s /q {surucu}\\rootdir'
        ]
        for komut in komutlar:
            subprocess.call(komut, shell=True)
        messagebox.showinfo("Başarılı", f"{surucu}başarıyla temizlendi.")
    except Exception as e:
        messagebox.showerror("Hata", f"Hata oluştu:\n{e}")
        
#GUI

pencere = tk.Tk()
pencere.title("USB Virüs Temizleyeci")
pencere.geometry("350x180")
pencere.resizable(False, False)

etiket = tk.Label(pencere,text="Temizlenecek sürücüyü seçin")
etiket.pack(pady=10)

surucu_var= tk.StringVar()
surucu_secici = ttk.Combobox(pencere, textvariable=surucu_var, state="readonly")
surucu_secici['values'] = suruculeri_getir()
surucu_secici.pack()

buton = tk.Button(pencere,text="Temizle", command=temizle_usb, bg="green", fg="white")
buton.pack(pady=20)

pencere.mainloop()