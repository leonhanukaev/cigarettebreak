import sys
import time
import subprocess

WORK_MINUTES = 0.1
BREAK_MINUTES = 0.1

def main():
    while True:
        try:
            if len(sys.argv) <= 1:
                countdown(WORK_MINUTES, "🚬 GO SMOKE")
                countdown(BREAK_MINUTES, "GO BACK TO WORK")
            elif sys.argv[1] == "-t":
                minutes = int(sys.argv[2]) if len(sys.argv) > 2 else WORK_MINUTES
                countdown(minutes, "🚬 GO SMOKE")
            elif sys.argv[1] == "-b":
                minutes = int(sys.argv[2]) if len(sys.argv) > 2 else BREAK_MINUTES
                countdown(minutes, "GO BACK TO WORK")
            elif sys.argv[1] == "-h":
                help()
            elif sys.argv[1] in ("-F", "-f"):
                credits()
            else:
                help()
        except KeyboardInterrupt:
            print("\nGo back to work! Hustle")
            break
        except Exception as ex:
            print(ex)
            exit(1)

def countdown(minutes, notify_msg):
    start_time = time.perf_counter()
    total_seconds = minutes * 60
    while True:
        diff_seconds = int(round(time.perf_counter() - start_time))
        left_seconds = total_seconds - diff_seconds
        if left_seconds <= 0:
            print("")
            break
        countdown_display(left_seconds, total_seconds)
        time.sleep(1)
    notify(notify_msg)

def countdown_display(seconds, total_seconds):
    minutes = seconds // 60
    seconds %= 60
    progress = (total_seconds - seconds) / total_seconds
    progress_bar = "▰" * int(progress * 20) + "▱" * (20 - int(progress * 20))
    print(f"{minutes:02}:{seconds:02} ⏰ [{progress_bar}] {int(progress * 100)}%", end="\r")

def notify(msg):
    print(msg)
    try:
        if sys.platform.startswith("user"):
            subprocess.Popen(["notify-send", "🚬 GO SMOKE", msg])
    except:
        pass

def help():
    appname = sys.argv[0]
    appname = appname if appname.endswith(".py") else "cigarette" 
    print(f"{appname}: Work for {WORK_MINUTES} minutes and take a {BREAK_MINUTES} minutes break.")
    print(f"{appname} -t [minutes]: Work for a specified number of minutes.")
    print(f"{appname} -F or {appname} -f: Trigger credits")

def credits():
    print("leon hanukaev CS50 final")

if __name__ == "__main__":
    main()
