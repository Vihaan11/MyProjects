import time
import webbrowser
import os
module=input("Module name (case sensitive): ")
command="cmd /k pip install " + module
try:
    docus="https://pypi.org/project/"+module+"/#description"
    print('''
------------------------------------------------------------------------
Please exit the window when installation is done
------------------------------------------------------------------------
''')
    time.sleep(2.75)
    webbrowser.open_new_tab(docus)
    os.system(command)
except:
    print("ERROR!!")
exit()
