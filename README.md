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
		show pyinstaller failing on different cwd
		Cwd DEPENDS
		So on windows cwd is your exe
		On mac, it's the folder above(?)
#1.a: when making exe with pyinstaller, using specfile is DEPENDENT ON YOUR OS.GETCWD
    this is nontrivial in the sense that it's basic, but not something you think about
    If i ask you what the cwd is for the spec file, you will say that it's the cwd of the terminal running it. Then if I ask you if the spec file can find the media folder, of course you can figure out the problem!
    
	BUT if you are just trying to create the exe from an automatically generated spec file you're not in the mindset to think about getcwd.
#2: so where should I look/how should I look?
sys.path + sys.executable + os.getcwd + sys._MEIPASS using rglob
	almost fool proof search strategy: 
	rglob search through sys.path, os.getcwd and MEIPASS if it exists
    https://docs.python.org/3/library/pathlib.html#pathlib.Path.rglob

TL:DR:
	there are TWO ways to run a python file, 
	#1: from terminal/ide
	#2: as exe from PyInstaller
	You must be wary that os.getcwd changes in your terminal depending on your terminal cwd. In PyInstaller, os.getcwd changes BETWEEN Windows and Mac

	There are FOUR locations to look in for a file:
	#1: sys.path 
	#2: os.getcwd
	#3: sys.executable
	#4: sys._MEIPASS IF made with PyInstaller