# A6: электронные часы, формат h:mm:ss
n = int(input()) % 86400
hours = n // 3600
minutes = n // 60 % 60
seconds = n % 60
print('{}:{:02}:{:02}'.format(hours, minutes, seconds))
