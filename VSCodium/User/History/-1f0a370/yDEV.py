import time

print("Default settings (25 min 5 min 15 min) - 0 or Custom - 1?")
choice = int(input(">"))

if choice == 0:
    pomodoro_time = 25
    break_time = 5
    big_bob_oreshki = 15
else:
    pomodoro_time = int(input("1 Pomodoro Time = "))
    break_time = int(input("1 Break Time  = "))
    big_bob_oreshki = int(input("1 Big Break Time = "))

pomodoro_amount = int(input("Amount of Pomodoros = "))

pomodoro_secs = pomodoro_time * 60
break_secs = break_secs * 60
big_bob_oreshki_secs = big_bob_oreshki * 60

def countdown(pomodoro_secs, break_secs, big_bob_oreshki_secs, pomodoro_amount):
    def pomodoro_countdown(pomodoro_secs):
        while seconds > 0:
            mins, secs = divmod(seconds, 60)  # Calculate minutes and seconds
            timer = '{:02d}:{:02d}'.format(mins, secs) # Format for display
            print(timer, end='\r') # Print and overwrite the line
            time.sleep(1) # Pause for 1 second
            seconds -= 1 # Decrement the time
            if seconds == 0:
                print("Time's up!") # Message when countdown finishes
                break


countdown(seconds, minutes, pomodoro_amount, pomodoro_time, break_time, big_bob_oreshki)