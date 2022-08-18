# tkinter Widget Drag & Drop
Place tkinter widgets visually in the UI. Just drag and drop (dnd) the widgets with your mouse!
It is about time we all stop placing widgets in code and start doing it visually.
This implementation taks only one line of code.

## How to use?
Before your mainloop, place dnd(). i.e.:
### Without saving:
```
from tk_widget_dnd import dnd

# some tkinter code
def main():
  # some tkinter code

  dnd(locals(), mouse_button=3)
  window.mainloop()
```
or
```
from tk_widget_dnd import dnd

# some tkinter code

dnd(globals(), mouse_button=1)

window.mainloop()
```

### With saving:
```
from tk_widget_dnd import dnd, quit_wrapper

def main():
  # some tkinter code
  dnd(locals(), mouse_button=3)

  quit_func = quit_wrapper(locals(), quit_app, save_widget_position, path)
  window.protocol("WM_DELETE_WINDOW", quit_func) 
  window.mainloop()
```
* `locals()` are the local variables in the scope. The widgets are a subset of these variables. Only bindable tkinter widgets are saved.
* `quit_app` function is the original quiting function you put in window.protocol("WM_DELETE_WINDOW", quit_app).
* `save_widget_position` function saves the dictionary of the widgets and their position in a file to "path".

### Load widgets position:
```
# some tkinter code
# Here you load widgets_position from a yaml, json, pickle file... 
set_widgets_position(locals(), widgets_position)
```

