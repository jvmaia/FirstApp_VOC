import android
from android.util import Log
from android.widget import LinearLayout
from android.widget import Button
from android.widget import TextView
from android.view import Gravity
import android.view

class ButtonClick(implements=android.view.View[OnClickListener]):
    def __init__(self, callback, *args, **kwargs):
        self.callback = callback
        self.args = args
        self.kwargs = kwargs

    def onClick(self, view: android.view.View) -> void:
        self.callback(*self.args, **self.kwargs)

class MyApp:
    def __init__(self):
        self._activity = android.PythonActivity.setListener(self)
        self.message = 'click on button to change me'
        self.message_button = 'try me'

    def onCreate(self):
        self.label = TextView(self._activity)
        self.label.setTextSize(50)
        self.label.setText(self.message)

        vlayout = LinearLayout(self._activity)
        vlayout.setOrientation(LinearLayout.VERTICAL)
        vlayout.addView(self.label)

        self.switch_button = Button(self._activity)
        self.switch_button.setText(self.message_button)
        self.switch_button.setOnClickListener(ButtonClick(self.update))

        vlayout.addView(self.switch_button)

        self._activity.setContentView(vlayout)

    def update(self):
        if self.message == 'On':
            self.message = 'Off'
            self.message_button = 'On'
        else:
            self.message = 'On'
            self.message_button = 'Off'
        self.switch_button.setText(self.message_button)
        self.label.setText(self.message)

def main():
    MyApp()
