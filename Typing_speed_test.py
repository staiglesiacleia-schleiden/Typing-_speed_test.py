import time

text = "I love python"

print("Type this:")
print(text)

input("Press Enter to start")

start = time.time()
typed = input()
end = time.time()

time_used = end - start
words = len(text.split())
wpm = (words / time_used) * 60

print("Time:", round(time_used, 2), "seconds")
print("Speed:", round(wpm, 2), "WPM")

if typed == text:
    print("Perfect!")
else:
    print("Try again!")

