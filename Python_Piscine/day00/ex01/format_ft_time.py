from datetime import datetime

time = datetime.now()
print(f"Seconds since January 1, 1970:{time.timestamp(): .0f} or{time.timestamp(): .2e} in scientific notation")
print(time.strftime("%b"), time.day, time.year)
