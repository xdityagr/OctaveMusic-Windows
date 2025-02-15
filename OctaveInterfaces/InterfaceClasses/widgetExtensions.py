import sys
from PySide6.QtCore import Qt, QTimer, QSize
from PySide6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout

class ScrollingLabel(QLabel):
    def __init__(self, text="", parent=None):
        # Check if the parent is not QWidget and cast it if necessary
        if not isinstance(parent, QWidget):
            parent = None
        super(ScrollingLabel, self).__init__(parent)  # Initialize QLabel with optional parent

        self.full_text = text
        self.truncated_text = ""
        self.text_position = 0

        # Animation settings
        self.scroll_delay = 5000  # 5 seconds before scrolling starts
        self.scroll_loops = 2     # Number of times to loop the scroll
        self.scroll_speed = 150   # Speed of scrolling (lower values = faster scroll)
        self.loop_count = 0       # Track the number of scroll loops completed
        self.is_scrolling = False # Flag to track if scrolling is active

        # Set alignment (customizable)
        self.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        # Set up timers
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.scroll_text)

        self.reset_timer = QTimer(self)
        self.reset_timer.setSingleShot(True)
        self.reset_timer.timeout.connect(self.start_scrolling)

        # Set the initial text and show the ellipsis version
        self.setText(self.full_text)
        self.show_ellipsis_text()
        self.reset_timer.start(self.scroll_delay)  # Start the timer for scrolling delay

    def setText(self, text):
        """Override setText method to support full_text and ellipsis logic."""
        self.full_text = text
        self.show_ellipsis_text()

    def show_ellipsis_text(self):
        """Show the text with ellipsis if it overflows."""
        label_width = self.width()
        text_width = self.fontMetrics().width(self.full_text)

        if text_width > label_width:
            # Create the ellipsis text
            clipped_text = self.full_text
            while self.fontMetrics().width(clipped_text + "...") > label_width:
                clipped_text = clipped_text[:-1]  # Trim one character at a time
            self.truncated_text = clipped_text + "..."
            super(ScrollingLabel, self).setText(self.truncated_text)  # Use QLabel's setText
        else:
            # If the text fits, show the full text
            super(ScrollingLabel, self).setText(self.full_text)

    def start_scrolling(self):
        """Start the scrolling animation after the initial delay."""
        self.is_scrolling = True
        self.loop_count = 0
        self.text_position = 0
        self.timer.start(self.scroll_speed)

    def stop_scrolling(self):
        self.is_scrolling = True
        self.loop_count = 0
        self.text_position = 0
        self.timer.start(self.scroll_speed)


    def stop_scrolling(self):
        """Stop the scrolling animation."""
        self.timer.stop()
        self.show_ellipsis_text()  # 
    
    def setText(self, text):
        """Override the setText method to set both full text and visible text."""
        self.full_text = text
        self.show_ellipsis_text()

    def resizeEvent(self, event):
        """Handle resizing of the label and adjust text accordingly."""
        super().resizeEvent(event)
        self.show_ellipsis_text()

    def scroll_text(self):
        """Scroll the text in a loop."""
        text_width = self.fontMetrics().width(self.full_text)
        label_width = self.width()

        # If the text is wider than the label, scroll
        if text_width > label_width:
            visible_text = self.full_text[self.text_position:]
            if self.text_position > 0:
                visible_text += " " + self.full_text[:self.text_position]

            super(ScrollingLabel, self).setText(visible_text[:len(self.full_text)])

            # Move the position forward, and wrap around when we reach the end
            self.text_position += 1
            if self.text_position > len(self.full_text):
                self.text_position = 0
                self.loop_count += 1

            # If we have completed the required scroll loops, reset to ellipsis mode
            if self.loop_count >= self.scroll_loops:
                self.timer.stop()
                self.is_scrolling = False
                self.show_ellipsis_text()
                self.reset_timer.start(self.scroll_delay)  # Wait for delay before next scroll
        else:
            # No need to scroll if the text fits
            super(ScrollingLabel, self).setText(self.full_text)


            