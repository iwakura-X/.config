import time

pomodoro_time = int(input("1 Pomodoro Time = "))
break_time = int(input("1 Break Time  = "))
pomodoro_amount = int(input("Amount of Pomodoros = "))
minutes = pomodoro_time + break_time
seconds = minutes * 60

def countdown(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer_display = f"{mins:02d}:{secs:02d}"
        print(timer_display, end='\r')  # Overwrite previous output
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

# Example usage: countdown for 10 seconds
countdown(10)