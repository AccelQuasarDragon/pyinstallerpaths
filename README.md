# pyinstallerpaths
Example of the INCREDIBLE amount of paths you have to think about on Win/Mac when using pyinstaller: os.getcwd, sys.path, sys.executable, sys._MEIPASS

#0: go over the kivy code first

#1: os.getcwd is different
	In code: show os get cwd change depending on your terminal
        run 1: in pyinstallerpaths
        run 2: in lv1 folder
	Executable might be python exe (depending where u run it)
	In pyinstaller: 
		change in pyinstaller: move pyinstaller to different directory
		show pyinstaller specfile failing on different cwd
		cwd DEPENDS on your terminal!
		So on windows cwd is your exe on pyinstaller
		On mac, it's the user folder
		How MEIPASS relates to spec file, https://kivyschool.com/PyInstaller%20Instructions/#step-4b-add-your-kv-file-resources-hooks-and-hiddenimports
#1.a: when making exe with pyinstaller, using specfile is DEPENDENT ON YOUR OS.GETCWD
    this is nontrivial in the sense that it's basic, but not something you think about

    If i ask you what the cwd is for terminal running pyinstaller on the spec file, you will obviously know by looking at where your terminal is at. Then if I ask you if the command on the spec file can find the media folder, of course you can figure out if the terminal is in the right cwd!
    
	BUT if you are just trying to create the exe from an automatically generated spec file you're not in the mindset to think about getcwd.

#2: so where should I look/how should I look?
sys.path + sys.executable + os.getcwd + sys._MEIPASS using rglob
	almost fool proof search strategy: 
	rglob search through sys.path, os.getcwd and MEIPASS if it exists
    https://docs.python.org/3/library/pathlib.html#pathlib.Path.rglob
#3: do the same for Mac
TL:DR:
	there are TWO ways to run a python file, 
	#1: from terminal/ide
	#2: as exe from PyInstaller
	You must be wary that os.getcwd changes in your terminal depending on your terminal cwd. In PyInstaller, os.getcwd changes BETWEEN Windows and Mac
	on Windows it is your exe folder. On Mac it is your user folder.

	There are FOUR locations to look in for a file:
	#1: sys.path 
	#2: os.getcwd
	#3: sys.executable
	#4: sys._MEIPASS IF made with PyInstaller

	If you want a decent solution, look through all 4 paths using rglob. If you want a fast solution, just add sys._MEIPASS to sys.path. But be careful! the _MEIPASS folder is a temp folder, and will not persist between runs.