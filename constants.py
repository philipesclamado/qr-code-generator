import os
import pyqrcode

IMAGE = pyqrcode.create(os.environ["URL"])
