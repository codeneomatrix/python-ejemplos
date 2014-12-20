import pynotify
import gtk

def notify(title, msg, icon=None):
    """Send notification icon messages through libnotify.

    Parameters:

    (str) title -- The notification title
    (str) msg -- The message to display into notification
    (str / uri) icon -- Type of icon (ok|info|error|warm|ask|sync) or icon file

    """
    if not pynotify.is_initted():
        pynotify.init(title)
    gtk_icon = {'ok':gtk.STOCK_YES, 'info':gtk.STOCK_DIALOG_INFO,
                'error':gtk.STOCK_DIALOG_ERROR, 'warm':gtk.STOCK_DIALOG_WARNING,
                'ask':gtk.STOCK_DIALOG_QUESTION, 'sync':gtk.STOCK_JUMP_TO}
    try:
        note = pynotify.Notification(title, msg)
        helper = gtk.Button()
        gtk_icon = helper.render_icon(gtk_icon[icon], gtk.ICON_SIZE_BUTTON)
        note.set_icon_from_pixbuf(gtk_icon)
    except KeyError:
        note = pynotify.Notification(title, msg, icon)
    note.show()


def main():
    """Main section"""
    notify('TEST', 'This is an Ok Message', 'ok')
    notify('TEST', 'This is an Info Message', 'info')
    notify('TEST', 'This is an Error Message', 'error')
    notify('TEST', 'This is a Warm Message', 'warm')
    notify('TEST', 'This is an Ask Message', 'ask')
    notify('TEST', 'This is an Sync Message', 'sync')
    notify('TEST', 'This is a Personalized Icon Message',
           '/usr/share/icons/gnome/scalable/places/ubuntu-logo.svg')
    notify('TEST',
           '''
Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At
vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd
gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.
           ''', wrap=60)


if __name__ == "__main__":
    main()