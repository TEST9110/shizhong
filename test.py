import time

def focus_timer(minutes):
    seconds = minutes * 60
    start_time = time.time()
    end_time = start_time + seconds

    while time.time() < end_time:
        remaining_seconds = int(end_time - time.time())
        minutes = remaining_seconds // 60
        seconds = remaining_seconds % 60
        print(f"Remaining time: {minutes:02d}:{seconds:02d}", end="\r")
        time.sleep(1)

    print("Time's up! You have completed your focus session.")

# 使用示例：设置一个25分钟的专注时钟
focus_timer(25)
