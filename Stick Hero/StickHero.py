from PIL import ImageGrab
import os
import win32api, win32con
import time
 
 
# All values are browser / laptop / screen resolution specific
# Below given values are for a 14 inch Dell Inspiron laptop with the game running on Chrome browser
xPadding = 497
yPadding = 60

xStart = 179
yStart = 366 

xRestart = 258
yRestart = 423

xPlatformStart = 76
yPlatformStart = 607

xPlay = 182
yPlay = 272
 
yStick = 447
xStick = 70

# Returns image of current game screen
def screenGrab():
    box = (xPadding,yPadding,xPadding + 373,yPadding + 663)
    im = ImageGrab.grab(box)
    return im
 
# Saves image of current game screen
def saveScreenGrab():
    box = (xPadding,yPadding,xPadding + 373,yPadding + 663)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
'.png', 'PNG')
 
# Left click mouse and hold for 'duration' number of seconds
def leftClick(duration):
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(duration)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
	
# Returns current mouse co-ordinates relative to game screen
def get_cords():
    x,y = win32api.GetCursorPos()
    x = x - xPadding
    y = y - yPadding
    print x,y
 
# Moves mouse to specified location relative to the game screen
def moveMouse(cord):
    win32api.SetCursorPos((xPadding + cord[0], yPadding + cord[1]))
 
# Starts game by first pressing 'Restart' and then 'Start'
def startGame():
	moveMouse((xRestart,yRestart))
	leftClick(0.1)
	moveMouse((xStart,yStart))
	leftClick(0.1)
 
# Main game loop
def playGame():
	
	# Start game and give 1 sec for loading
	startGame()
	time.sleep(1)
	score = 0
	
	while True:
		
		# Moves mouse to game play position
		moveMouse((xPlay,yPlay))

		# Gets screen shot of game screen
		im = screenGrab()
		
		# Calculate distance to next platform relative to xPlatformStart
		distanceFront = 1
		for i in range(1,300):
			pixel = im.getpixel((xPlatformStart+i,yPlatformStart))
			if pixel == (41,29,20):
				distanceFront = i
				break
				
		# Calculate distance to previous platform relative to xPlatformStart
		distanceBack = 1
		for i in range(1,50):
			pixel = im.getpixel((xPlatformStart-i,yPlatformStart))
			if pixel == (41,29,20):
				distanceBack = i
				break
				
		# Total Distance
		distance = distanceFront + distanceBack
				
		# Add safeguard distance if next platform is broad enough
		epsilon = 0
		if (xPlatformStart + distance + 20) < (373):
			if im.getpixel((xPlatformStart + distance + 15,yPlatformStart+2)) == (41,29,20):
				epsilon = 10
				
		distance = distance + epsilon - 3
		if epsilon != 0:
			print "Padding detected\n"
		
		print("Distance in pixels: " + str(distance))
		
		# Values obtained for linear regression fit
		duration = (0.027779) + (0.003587 * (distance))
		print("Holding for secs..." + str(duration))
		leftClick(duration)
		
		# Wait for rod to fall and then take screenshot
		time.sleep(1)
		im = screenGrab()
		
		# Calculate rod length
		rodLength = 0
		for i in range(1,300):
			pixel = im.getpixel((xStick+i,yStick))
			if pixel != (10,7,5):
				rodLength = i
				break
		
		print("Rod length: " + str(rodLength))
		
		# Allow player to reach next platform (or fall) and take screenshot
		time.sleep(2)
		im = screenGrab()
		
		# Check if game is over with the presence of restart button
		if im.getpixel((xRestart,yRestart)) == (103,103,103):
			print('Game Over')
			
			# Start the game again
			startGame()
			time.sleep(1.5)
			print("SCORE: " + str(score))
			score = 0
		else: score = score + 1