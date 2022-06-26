import os
from .token import token # Create a token.py in the canvas_task folder and write token='<Your token>'
base_url="https://umjicanvas.com/"
threshold_day=7
data_folder=os.path.join(os.environ.get('HOME'),'canvas_task_data/')
