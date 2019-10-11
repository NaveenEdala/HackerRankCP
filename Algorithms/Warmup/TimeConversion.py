from datetime import datetime
t = input()

dt=datetime.strptime(t, '%I:%M:%S%p')
print(dt.strftime('%H:%M:%S'))
