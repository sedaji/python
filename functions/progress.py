import time
progLength = 500
for i in range(progLength):
	progCount = (i * 100 / (progLength - 1))
	progIncrement = (int(progCount / 5))
	print("Progress: [" + "=" * progIncrement + '] ', end='')
	print(str("%.2f" %progCount), end='%\r')
	time.sleep(0.01)
print()