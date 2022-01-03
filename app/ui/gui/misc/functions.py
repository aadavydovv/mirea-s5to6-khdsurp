def setup_widget_size(widget, width_c=1.2, height_c=1.1, resizable=False, maxsize=False):
    if not resizable:
        widget.resizable(False, False)

        width = int(widget.winfo_screenwidth() / width_c)
        height = int(widget.winfo_screenheight() / height_c)

        widget.minsize(width, height)
        widget.maxsize(width, height)

    if maxsize:
        width = widget.winfo_screenwidth()
        height = widget.winfo_screenheight()
        widget.maxsize(int(width / width_c), int(height / height_c))
