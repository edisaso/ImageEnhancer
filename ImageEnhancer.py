import os
import replicate
import webbrowser
import  tkinter as tk
from tkinter import filedialog

os.environ['REPLICATE_API_TOKEN'] = 'Put your replicate.com API token here'
model = replicate.models.get("tencentarc/gfpgan")
version = model.versions.get("9283608cc6b7be6b65a8e44983db012355fde4132009bf99d976b2f0896856a3")

root = tk.Tk()
root.withdraw()
PCfile = filedialog.askopenfilename()
# https://replicate.com/tencentarc/gfpgan/versions/9283608cc6b7be6b65a8e44983db012355fde4132009bf99d976b2f0896856a3#input
inputs = {
    # Input
     'img': open(PCfile, "rb"),

    # GFPGAN version. v1.3: better quality. v1.4: more details and better
    # identity.
    'version': "v1.3",

    # Rescaling factor
    'scale': 2,
}

# https://replicate.com/tencentarc/gfpgan/versions/9283608cc6b7be6b65a8e44983db012355fde4132009bf99d976b2f0896856a3#output-schema
output = version.predict(**inputs)
print(output)
webbrowser.open_new_tab(output)
