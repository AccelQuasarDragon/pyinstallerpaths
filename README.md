### pyinstallerpaths
Example of the INCREDIBLE amount of paths you have to think about on Win/Mac when using pyinstaller: os.getcwd, sys.path, sys.executable, sys._MEIPASS, `__file__`, os.path.dirname(`__file__`)) 

### TL:DR:

| Windows        | terminal                                   | pyinstaller exe                                                         |
|----------------|--------------------------------------------|-------------------------------------------------------------------------|
| os.getcwd      | your terminal's get cwd                    | the directory that holds your exe                                       |
| sys.executable | your environment's python.exe              | the pyinstaller exe itself                                              |
| sys.path       | your python PATH                           | the PATH of sys._MEIPASS                                                |
| sys._MEIPASS   | does not exist                             | MEIxxxxx tempfolder                                                     |
| `__file__`     | the location of the python file you invoke | the location of the python file you invoke with the exe in sys._MEIPASS |

| MAC            | terminal                                   | unix executable file                                                    | .app bundle                                                             |
|----------------|--------------------------------------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------|
| os.getcwd      | your terminal's getcwd                     | your user directory ("/Users/Kevin")                                    | root folder ("/")                                                       |
| sys.executable | your environment's python.exe              | the unix executable itself                                              | the unix executable in the content folder of the .app bundle            |
| sys.path       | your python PATH                           | the PATH of sys._MEIPASS                                                | the path of sys._MEIPASS                                                |
| sys._MEIPASS   | does not exist                             | MEIxxxxx tempfolder                                                     | MEIxxxxx tempfolder                                                     |
| `__file__`     | the location of the python file you invoke | the location of the python file you invoke with the exe in sys._MEIPASS | the location of the python file you invoke with the exe in sys._MEIPASS |

### 1: os.getcwd is different
* In code: show os get cwd change depending on your terminal
	* terminal run 1: in pyinstallerpaths
	* terminal run 2: in lv1 folder
* Executable is python exe from terminal, and your exe if made with pyinstaller
* In pyinstaller: 
	* change in pyinstaller: move pyinstaller app to different directory
	* show pyinstaller specfile failing on different cwd
		* #1: show on lv1 failing
		* #2: show on pyinstallerpaths trying on lv1/mainONEFILE.spec (will still fail)
	* cwd DEPENDS on your terminal!
	* So on windows cwd is your exe on pyinstaller
	* On mac, it's the user folder as a unix executable, and the root / folder when run as a .app file.
	* How MEIPASS relates to spec file, https://kivyschool.com/PyInstaller%20Instructions/#step-4b-add-your-kv-file-resources-hooks-and-hiddenimports
### 1.a: when making exe with pyinstaller, your specfile's dir is the cwd. Reminder that you can use full paths or construct a full path and give that to pyinstaller 

### 2: so where should I look/how should I look?
* 2 options:
	* ADD MEIPASS TO PATHS:
		* https://stackoverflow.com/questions/7674790/bundling-data-files-with-pyinstaller-onefile
		* this is OK if you don't need persistent data, but since tempfolder gets deleted you can't save to sys._MEIPASS. The naive way is to just save data in the folder that the .exe is in.
	* SEARCH EVERYWHERE:
		* sys.path + sys.executable + os.getcwd + sys._MEIPASS + os.path.dirname(`__file__`) using rglob
			* One last location to look at: __file__ and os.path.dirname(__file__)
			* almost fool proof search strategy: 
			* rglob search through sys.path, os.getcwd and MEIPASS if it exists
			* https://docs.python.org/3/library/pathlib.html#pathlib.Path.rglob

### 3: do the same for Mac
* Mac specific problem: unix executable works for .app is prevented from looking at network folders (since getcwd is /)
* Reminder that you can also look inside .app files on Mac
* what is bad: os.getcwd gets root folder if you are running from .app on Mac!
* getcwd on pyinstaller .app on mac is / which is the root folder
* but getcwd on pyinstaller which is a unix executable is user folder
* so u can't use getcwd on .app

### TL:DR:
* there are THREE ways to run a python file, 
	* #1: from terminal/ide
	* #2: as exe from PyInstaller
	* #3: On Mac, you are given two options: as a unix executable or a .app file
* You must be wary that os.getcwd changes in your terminal depending on your terminal cwd.
* In PyInstaller, os.getcwd changes.
	* on Windows it is your exe folder. On Mac it is your user folder (as a unix *executable) or root / folder (as an .app).
* There are FIVE locations to look in for a file:
	* #1: sys.path 
	* #2: os.getcwd
	* #3: sys.executable
	* #4: sys._MEIPASS if made with PyInstaller
	* #5: __file__/ os.path.dirname(__file__)
* If you want a decent solution, look through all 5 paths using rglob. 
* If you want a fast solution, just add sys._MEIPASS to sys.path. But becareful!
	* the _MEIPASS folder is a temp folder, and will not persist betweenruns.
