import sys
import time
import subprocess

WORK_MINUTES = 0.1
BREAK_MINUTES = 0.1

def main():
    while True:
        try:
            if len(sys.argv) <= 1:
                countdown(WORK_MINUTES, "Time for a break")
                countdown(BREAK_MINUTES, "Time to work")
            elif sys.argv[1] == "-t":
                minutes = int(sys.argv[2]) if len(sys.argv) > 2 else WORK_MINUTES
                countdown(minutes, "Time for a break")
            elif sys.argv[1] == "-b":
                minutes = int(sys.argv[2]) if len(sys.argv) > 2 else BREAK_MINUTES
                countdown(minutes, "Time to work")
            else:
                help()
        except KeyboardInterrupt:
            print("\nGoodbye")
            break
        except Exception as ex:
            print(ex)
            exit(1)

def countdown(minutes, notify_msg):
    start_time = time.perf_counter()
    while True:
        diff_seconds = int(round(time.perf_counter() - start_time))
        left_seconds = minutes * 60 - diff_seconds
        if left_seconds <= 0:
            print("")
            break
        countdown_display(left_seconds)
        time.sleep(1)
    notify(notify_msg)

def countdown_display(seconds):
    minutes = seconds // 60
    seconds %= 60
    print(f"{minutes:02}:{seconds:02} ⏰", end="\r")

def notify(msg):
    print(msg)
    try:
        if sys.platform.startswith("linux"):
            subprocess.Popen(["notify-send", "🚬", msg])
    except:
        pass

def help():
    appname = sys.argv[0]
    appname = appname if appname.endswith(".py") else "cigarette" 
    print(f"{appname}: Work for {WORK_MINUTES} minutes and take a {BREAK_MINUTES} minutes break.")
    print(f"{appname} -t [minutes]: Work for a specified number of minutes.")
    print(f"{appname} -b [minutes]: Take a specified break of minutes.")
    print(f"{appname} -h: Show this help message.")

if __name__ == "__main__":
    main()
