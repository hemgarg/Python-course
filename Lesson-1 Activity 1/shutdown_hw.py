import time
def shutdown():
    print("Shutting Down")
    time.sleep(2)
    print("Shut down!")
    quit()
def abortshutdown():
    print("Aborted Shut down")

command = input("Do you want to shutdown the computer? (Y/N)")

if command == "Y":
    shutdown()
elif command == "N":
    abortshutdown()
else:
    print("Sorry but your input isn't valid!")