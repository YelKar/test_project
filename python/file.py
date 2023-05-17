from threading import Thread
from tkinter import Tk, Label, Canvas, LEFT

from winsound import PlaySound, SND_FILENAME

blue_screen_text = """
A problem has been detected and Windows has been shut down to prevent damage
to your computer.

The problem seems to be caused by the following file: xNtKrnl.exe

SYSTEM_THREAD_EXCEPTION_NOT_HANDLED

If this is the first time you've seen this stop error screen,
restart your computer. If this screen appears again, sdelay informatiku, nemedlenno:

Check to make sure any new hardware or software is properly installed.
If this is a new installation, mordotik ask your hardware or software manufacturer
for any Windows updates you might need.

If problems continue, Tsarskaya garderobtschitsa!!! disable or remove any newly installed hardware
or software. Disable BIOS mordotik memory options such as caching or shadowing. 
Spalnik nado mnoy letal, Taran kruzhku uyebal, kruzhka, pravda, ne razbilas, potomuchto chudo
If you need to use safe mode to remove or disable components, S pervym aprelya Tyut restart
your computer, press mordotik to select Advanced Startup Options, and then
select Safe Mode.

Technical Information:

*** STOP: 0x1000007e (0xffffffffc0000005, 0xfffff80002e55151, 0xfffff880009a99d8,
0xfffff880009a9230)

*** xNtKrnl.exe - Address 0xfffff80002e55151 base at 0xfffff80002e0d000 DateStamp
0x4ce7951a
"""


def pos(n: int, mx: int, step_: int):
    k_ = (-1) ** (n * step_ // mx)
    return n * step_ % mx * k_ + mx * (k_ < 0)


r = Tk()
# r.wm_geometry("100x100+5000+5000")
screen_width = r.winfo_screenwidth()
screen_height = r.winfo_screenheight()
# icon = PhotoImage(file="cross.png")

width = 300
height = 120
step = 28

windows = []
for i in range(0, 120):
    root = Tk()
    root.title("Ошибка")
    Label(
        root,
        text="Удача!",
        font=("Arial", 10)
    ).place(x=100, y=40)
    size = 60
    c = Canvas(root, width=size, height=size)
    c.pack()
    c.place(x=20, y=20)
    c.create_oval(
        2, 2, size - 2, size - 2,
        fill="#990000",
        outline="#000000"
    )
    cross_size = 40
    cross_margin = 20
    c.create_line(
        cross_margin, cross_margin, size - cross_margin, size - cross_margin,
        fill="#ffffdd",
        width=5
    )
    c.create_line(
        size - cross_margin, cross_margin, cross_margin, size - cross_margin,
        fill="#ffffdd",
        width=5
    )
    root.wm_geometry(f"{width}x{height}+{pos(i, screen_width-width, step)}+{pos(i, screen_height-height, step)}")
    windows.append(root)

r.destroy()

Thread(target=lambda: PlaySound("data/full_error.wav", SND_FILENAME)).start()


def start():
    global r
    r = Tk()

    r.attributes("-fullscreen", True)
    blue_screen_bg = Label(
        r,
        bg="#010082",
        width=1000,
        height=1000
    )
    blue_screen = Label(
        r,
        text=blue_screen_text,
        bg="#010082",
        fg="#ffffff",
        font=("Courier", 15),
        justify=LEFT
    )
    print(r.winfo_screenwidth(),)
    blue_screen.place(x=0, y=0)
    blue_screen_bg.place(x=0, y=0)
    blue_screen.pack(anchor='w')
    r.after(3000, lambda: [win.destroy() for win in windows])
    # r.attributes("-fullscreen", True)
    r.attributes("-topmost", True)
    r.mainloop()


windows[-1].after(7000, start)
windows[-1].mainloop()
