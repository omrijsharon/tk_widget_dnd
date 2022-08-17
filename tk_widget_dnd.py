from tkinter import CENTER


def dnd(anchor=CENTER, mouse_button=1):
    assert mouse_button in [1, 2, 3], "mouse_button must be 1, 2 or 3"
    [v.bind("<B{}-Motion>".format(mouse_button), lambda event: event.widget.place(x=-event.widget.master.winfo_x() + event.x_root,
                                                            y=-event.widget.master.winfo_y() + event.y_root,
                                                            anchor=anchor)) for k, v in globals().items() if
     "tkinter" in str(type(v)).lower()]


def get_widgets_position():
    return {k: (v.winfo_x(), v.winfo_y()) for k, v in globals().items() if "tkinter" in str(type(v)).lower()}


def set_widgets_position(positions):
    for k, v in positions.items():
        globals()[k].place(x=v[0], y=v[1])