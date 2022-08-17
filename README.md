# tkinter widget Drag & Drop
Place tkinter widgets visually in the UI. Just drag and drop (dnd) the widgets with your mouse!
It is about time we all stop placing widgets in code and start doing it visually.
This implementation taks only one line of code.

## How to use?
Before your mainloop, place dnd(). i.e.:
```
from tk_widget_dnd import dnd, get_widgets_position, set_widgets_position
from functools import partial

def main():
  # some tkinter code
  dnd(locals(), mouse_button=3)
  
  # in quit_app function we will save the widgets position.
  window.protocol("WM_DELETE_WINDOW", partial(quit_app, locals()) 
  window.mainloop()
```
or
```
from tk_widget_dnd import dnd

# some tkinter code

dnd(globals(), mouse_button=1)

# in quit_app function we will save the widgets position.
window.protocol("WM_DELETE_WINDOW", partial(quit_app, globals()) 
window.mainloop()
```

### Save widgets position when quiting:
```
def quit_app(variables, *args, **kwargs)
  widgets_position = get_widgets_position(variables)
  # Here you can save widgets_position to a yaml, json, pickle file... 
```
### Load widgets position:
```
# Here you load widgets_position from a yaml, json, pickle file... 
set_widgets_position(locals(), widgets_position)
```

