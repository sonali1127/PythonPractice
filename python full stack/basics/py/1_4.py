import time
timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
if int(time.strftime('%H')) <=11:
    print("Good Morning")
elif int(time.strftime('%H')) <=16:
    print("Good Afternoon")
elif int(time.strftime('%H')) <=19:
    print("Good Evening")
else:
    print("Good Night")