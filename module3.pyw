import tkinter as tk

count = 0
running = False

def klik_otomatis():
    global count, running
    if running:
        count += 1
        label_count.config(text=f"Jumlah klik: {count}")
        # Jadwalkan klik berikutnya setelah 1 detik
        root.after(500, klik_otomatis)

def mulai():
    global running
    running = True
    klik_otomatis()  # mulai klik pertama

def berhenti():
    global running
    running = False

# Buat jendela utama
root = tk.Tk()
root.title("Auto Clicker Sederhana")
root.geometry("300x200")

# Label counter
label_count = tk.Label(root, text="Jumlah klik: 0", font=("Arial", 14))
label_count.pack(pady=20)

# Tombol Mulai
tombol_mulai = tk.Button(root, text="Mulai Auto Klik", command=mulai, width=15)
tombol_mulai.pack(pady=5)

# Tombol Berhenti
tombol_berhenti = tk.Button(root, text="Berhenti", command=berhenti, width=15)
tombol_berhenti.pack(pady=5)

root.mainloop()
