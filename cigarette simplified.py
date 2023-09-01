import sys
import time
import subprocess

WORK_MINUTES = 25
BREAK_MINUTES = 5

def main():
    try:
        if len(sys.argv) <= 1:
            work(WORK_MINUTES)
            break_time(BREAK_MINUTES)
        elif sys.argv[1] == "-t":
            minutes = int(sys.argv[2]) if len(sys.argv) > 2 else WORK_MINUTES
            work(minutes)
        elif sys.argv[1] == "-b":
            minutes = int(sys.argv[2]) if len(sys.argv) > 2 else BREAK_MINUTES
            break_time(minutes)
        elif sys.argv[1] == "-h":
            help()
        else:
            help()
    except KeyboardInterrupt:
        print("\n👋 goodbye")
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
        else:
            pass
    except:
        pass

def help():
    appname = sys.argv[0]
    appname = appname if appname.endswith(".py") else "cigarette" 
    print("====== 🚬 cigarette Clock =======")
    print(f"{appname}         # start a {WORK_MINUTES} minutes cigarette clock + {BREAK_MINUTES} minutes break")
    print(f"{appname} -t      # start a {WORK_MINUTES} minutes cigarette clock")
    print(f"{appname} -t <n>  # start a <n> minutes cigarette clock")
    print(f"{appname} -b      # take a {BREAK_MINUTES} minutes break")
    print(f"{appname} -b <n>  # take a <n> minutes break")
    print(f"{appname} -h      # help")

def work(minutes):
    print(f"Work {minutes} minutes. Ctrl+C to exit")
    countdown(minutes, "It is time to take a break")

def break_time(minutes):
    print(f"Cigarette break {minutes} minutes. Ctrl+C to exit")
    countdown(minutes, "It is time to work")

if __name__ == "__main__":
    main()
