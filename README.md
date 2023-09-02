# pyinstallerpaths
Example of the INCREDIBLE amount of paths you have to think about on Win/Mac when using pyinstaller: os.getcwd, sys.path, sys.executable, sys._MEIPASS

#0: go over the kivy code first (show the mac update)

#1: os.getcwd is different
	In code: show os get cwd change depending on your terminal
        terminal run 1: in pyinstallerpaths
        terminal run 2: in lv1 folder
	Executable is python exe from ternimal, and your exe if made with pyinstaller
	In pyinstaller: 
		change in pyinstaller: move pyinstaller app to different directory
		show pyinstaller specfile failing on different cwd
			#1: show on lv1 failing
			#2: show on pyinstallerpaths trying on lv1/mainONEFILE.spec (will still fail)
		cwd DEPENDS on your terminal!
		So on windows cwd is your exe on pyinstaller
		On mac, it's the user folder
		How MEIPASS relates to spec file, https://kivyschool.com/PyInstaller%20Instructions/#step-4b-add-your-kv-file-resources-hooks-and-hiddenimports
#1.a: when making exe with pyinstaller, your specfile is the cwd. Reminder that you can use full paths or construct a full path and give that to pyinstaller 

#2: so where should I look/how should I look?
2 options:
	ADD MEIPASS TO PATHS:
		https://stackoverflow.com/questions/7674790/bundling-data-files-with-pyinstaller-onefile
		this is OK if you don't need persistent data, but since tempfolder gets deleted you can't save to sys._MEIPASS. The naive way is to just save data in the folder that the .exe is in.
	SEARCH EVERYWHERE:
	sys.path + sys.executable + os.getcwd + sys._MEIPASS using rglob
		almost fool proof search strategy: 
		rglob search through sys.path, os.getcwd and MEIPASS if it exists
		https://docs.python.org/3/library/pathlib.html#pathlib.Path.rglob

#3: do the same for Mac
Mac specific problem: unix executable works for .app is prevented from looking at network folders (since getcwd is /)

what is bad: os.getcwd

WHAT, getcwd on pyinstaller .app on mac is / which is the root folder
but getcwd on pyinstaller which is a unix executable is user folder
so u can't use getcwd on .app

One last note: __file__ and os.path.dirname(__file__)


TL:DR:
	there are TWO ways to run a python file, 
	#1: from terminal/ide
	#2: as exe from PyInstaller
	You must be wary that os.getcwd changes in your terminal depending on your terminal cwd. In PyInstaller, os.getcwd changes BETWEEN Windows and Mac
	on Windows it is your exe folder. On Mac it is your user folder (as a unix executable) or root / folder (as an .app).

	There are FIVE locations to look in for a file:
	#1: sys.path 
	#2: os.getcwd
	#3: sys.executable
	#4: sys._MEIPASS IF made with PyInstaller
	#5: __file__/ os.path.dirname(__file__)

	If you want a decent solution, look through all 4 paths using rglob. If you want a fast solution, just add sys._MEIPASS to sys.path. But be careful! the _MEIPASS folder is a temp folder, and will not persist between runs.
