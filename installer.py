import os
packages = ["pyttsx3", "selenium", "PyQt5"]


print("Checking and installing modules . . .")

for pkg in packages:
    try:
        import pkg
    except ImportError:
        os.system('pip install %s' % pkg)

print("Checking for chrome-driver . . .")
if os.path.exists("query/chromedriver.exe"):
    print("Chrome-driver is installed")
else:
    print("Chrome-driver was not found for some reason, please download and place the driver within the query folder.")
