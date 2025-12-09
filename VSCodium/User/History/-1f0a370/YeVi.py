import time

pomodoro_time = int(input("1 Pomodoro Time = "))
break_time = int(input("1 Break Time  = "))
big_bob_oreshki = int(input("1 Big Break Time = "))
pomodoro_amount = int(input("Amount of Pomodoros = "))
minutes = pomodoro_time + break_time
seconds = minutes * 60

def countdown(seconds, minutes, pomodoro_amount, pomodoro_time, break_time, big_bob_oreshki):
    while seconds > 0:
        mins, secs = divmod(t, 60)  # Calculate minutes and seconds
        timer = '{:02d}:{:02d}'.format(mins, secs) # Format for display
        print(timer, end='\r') # Print and overwrite the line
        time.sleep(1) # Pause for 1 second
        seconds -= 1 # Decrement the time
    print("Time's up!") # Message when countdown finishes

countdown()