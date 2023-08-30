# pyinstallerpaths
Example of the INCREDIBLE amount of paths you have to think about on Win/Mac when using pyinstaller: os.getcwd, sys.path, sys.executable, sys._MEIPASS


#0: go over the kivy code first
#0.a: in pyinstaller, specfile is DEPENDENT ON YOUR OS.GETCWD
    this is nontrivial in the sense that it's basic, but not something you think about
    if i ask you what the cwd is for the spec file, then I ask you if the spec file can find the media folder, of course you can figure out the problem
    BUT if you are just trying to create the exe from an automatically generated spec file you're not in the mindset to think about getcwd
#1: os.getcwd is different
	In code: show os get cwd change depending on your terminal
        run 1: in pyinstallerpaths
        run 2: in media folder
	Executable might be python exe (depending where u run it)
	In pyinstaller: 
		change in pyinstaller: move pyinstaller to different directory
		show pyinstaller failing on different cwd
		Cwd DEPENDS
		So on windows cwd is your exe
		On mac, it's the folder above(?)
#2: so where should I look/how should I look?
sys.path + sys.executable + os.getcwd + sys._MEIPASS using rglob
	almost fool proof search strategy: 
	rglob search through sys.path, os.getcwd and MEIPASS if it exists
    https://docs.python.org/3/library/pathlib.html#pathlib.Path.rglob