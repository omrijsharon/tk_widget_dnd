from tkinter import CENTER


def get_widgets(variables):
    return {k: v for k, v in variables.items() if "tkinter" in str(type(v)).lower() and str(type(v)).find("Var")==-1}


def dnd(variables, anchor=CENTER, mouse_button=1):
    assert mouse_button in [1, 2, 3], "mouse_button must be 1, 2 or 3"
    valid_widgets = get_widgets(variables)
    assert len(valid_widgets) > 0, "No valid widgets found. variables argument should be equal to locals() or globals(), depending on your scope."
    [v.bind("<B{}-Motion>".format(mouse_button), lambda event: event.widget.place(x=-event.widget.master.winfo_x() + event.x_root,
                                                            y=-event.widget.master.winfo_y() + event.y_root,
                                                            anchor=anchor)) for k, v in valid_widgets.items()]


def get_widgets_position(variables):
    valid_widgets = get_widgets(variables)
    return {k: (v.winfo_x(), v.winfo_y()) for k, v in valid_widgets.items()}


def set_widgets_position(variables, positions):
    for k, v in positions.items():
        variables[k].place(x=v[0], y=v[1])
