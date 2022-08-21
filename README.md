# tkinter Widget Drag & Drop
Place tkinter widgets visually in the UI. Just drag and drop (dnd) the widgets with your mouse!
It is about time we all stop placing widgets in code and start doing it visually.
This implementation taks only one line of code.

## How to use?
Before your mainloop, place dnd(). i.e.:
### Without saving:
```
from tk_widget_dnd import dnd, quit_wrapper

# some tkinter code
def main():
  # some tkinter code

  dnd(locals(), mouse_button=3)
  root.protocol("WM_DELETE_WINDOW", quit_wrapper(locals(), verbose=True))
  window.mainloop()
```
or
```
from tk_widget_dnd import dnd, quit_wrapper

# some tkinter code

dnd(globals(), mouse_button=1)
root.protocol("WM_DELETE_WINDOW", quit_wrapper(locals(), verbose=True))
window.mainloop()
```
dnd function lets you move widgets freely.
quit_wrapper lets you do somthing with the widgets coordinates. Its arguments:
- quit_function: the original quit function that runs when user quits the program.
- save_function: a function that saves the dictionary of {widgets_names: widgets_coordinates} to a file
  - This funcion takes 2 arguments: widgets_dict, path.
- path: the path given to the save function.
- verbose: True/False - to print or not to print the widgets coordinates when the user quits.
-  *args, **kwargs: all the inputs to quit_function.


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
* `locals()` or `globals()` are the variables in the desired scope. The widgets are a subset of these variables. *Only bindable tkinter widgets are saved*.
* `quit_app` function is the original quiting function you put in window.protocol("WM_DELETE_WINDOW", quit_app).
* `save_widget_position` function saves the dictionary of the widgets and their position in a file to "path".

### Load widgets position:
```
# some tkinter code
# Here you load widgets_position from a yaml, json, pickle file... 
set_widgets_position(locals(), widgets_position)
```

