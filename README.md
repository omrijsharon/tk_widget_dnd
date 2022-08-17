# tkinter widget Drag & Drop
Place tkinter widgets visually in the UI. Just drag and drop (dnd) the widgets with your mouse!
It is about time we all stop placing widgets in code and start doing it visually.
This implementation taks only one line of code.

## How to use?
Before your mainloop, place dnd(). i.e.:
```
from tk_widget_dnd import dnd

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
