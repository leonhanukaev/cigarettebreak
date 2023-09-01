import sys
import time
import subprocess

WORK_MINUTES = 25
BREAK_MINUTES = 5


def main():
    try:
        if len(sys.argv) <= 1:
            print(f"Work {WORK_MINUTES} minutes. Ctrl+C to exit")
            cigarette(WORK_MINUTES, "It is time to take a break")
            print(f"cigarette break {BREAK_MINUTES} minutes. Ctrl+C to exit")
            cigarette(BREAK_MINUTES, "It is time to work")

        elif sys.argv[1] == "-t":
            minutes = int(sys.argv[2]) if len(sys.argv) > 2 else WORK_MINUTES
            print(f"Work {minutes} minutes. Ctrl+C to exit")
            cigarette(minutes, "It is time to take a break")

        elif sys.argv[1] == "-b":
            minutes = int(sys.argv[2]) if len(sys.argv) > 2 else BREAK_MINUTES
            print(f"cigarette break {minutes} minutes. Ctrl+C to exit")
            cigarette(minutes, "It is time to work")

        elif sys.argv[1] == "-h":
            help()

        else:
            help()

    except KeyboardInterrupt:
        print("\n👋 goodbye")
    except Exception as ex:
        print(ex)
        exit(1)


def cigarette(minutes, notify_msg):
    start_time = time.perf_counter()
    while True:
        diff_seconds = int(round(time.perf_counter() - start_time))
        left_seconds = minutes * 60 - diff_seconds
        if left_seconds <= 0:
            print("")
            break

        countdown = f"{int(left_seconds / 60)}:{int(left_seconds % 60)} ⏰"
        duration = min(minutes, 25)
        progressbar(diff_seconds, minutes * 60, duration, countdown)
        time.sleep(1)

    notify_me(notify_msg)


def progressbar(curr, total, duration=10, extra=""):
    frac = curr / total
    filled = round(frac * duration)
    print(
        "\r",
        "🚬" * filled + "--" * (duration - filled),
        f"[{frac:.0%}]",
        extra,
        end="",
    )


def notify_me(msg):
    print(msg)
    try:
        if sys.platform.startswith("linux"):
            # ubuntu desktop notification
            subprocess.Popen(["notify-send", "🚬", msg])
        else:
            pass
    except:
        pass


def help():
    appname = sys.argv[0]
    appname = appname if appname.endswith(".py") else "cigarette"  # cigarette is pypi package
    print("====== 🚬 cigarette Clock =======")
    print(
        f"{appname}         # start a {WORK_MINUTES} minutes cigarette clock + {BREAK_MINUTES} minutes break"
    )
    print(f"{appname} -t      # start a {WORK_MINUTES} minutes cigarette clock")
    print(f"{appname} -t <n>  # start a <n> minutes cigarette clock")
    print(f"{appname} -b      # take a {BREAK_MINUTES} minutes break")
    print(f"{appname} -b <n>  # take a <n> minutes break")
    print(f"{appname} -h      # help")


if __name__ == "__main__":
    main()