import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject, GLib, Gdk
import glob

# Define the list of images

images = glob.glob('/media/pipi/USBMOVIES/Master_Master_Final/*.jpg')
# images = glob.glob('/home/charliepi/Pictures/converted/*.jpg')
# images = glob.glob('/media/charliepi/F3FB-CFFB/Master_Master/*.jpg')
# Initialize GTK
Gtk.init()

# Create a new window
window = Gtk.Window()

# Create an image widget
image = Gtk.Image()
window.add(image)

# Set the initial image
image.set_from_file(images[0])
# current_index = 0
color = Gdk.Color(red=0, green=0, blue=0)
window.modify_bg(Gtk.StateType.NORMAL, color)
# window.fullscreen()
current_index = 0

def show_next_image():
    global current_index  # Add this line to access the global variable

    print("this is idx {}".format(current_index))
    print("this is len images {}".format(len(images)))

    # Get the next image index
    if current_index + 1 < len(images):
        current_index = current_index + 1  # Assign the value of idx + 1 to current_index
        next_index = current_index
        image.set_from_file(images[next_index])
        GLib.timeout_add(15000, show_next_image)

    else:
        # Reset to the first image
        current_index = 0
        print(current_index)
        next_index = current_index
        print(images[next_index])
        image.set_from_file(images[next_index])
        GLib.timeout_add(15000, show_next_image)

# Start the timer for the first image

GLib.timeout_add(15000, show_next_image)

# Connect the window's destroy event to quit GTK
window.connect('destroy', Gtk.main_quit)

# Show the window
window.show_all()

# Start the GTK main loop
Gtk.main()