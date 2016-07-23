#Stick Hero Automtaion Bot

#### Game Link: http://m.silvergames.com/game/stick-hero/
#### Video Link: https://youtu.be/01Q3bSwZm_o

Aim of the game is to click and hold the mouse for just the right time so that the rod generated is enough to make the character reach the 
next platform and not too big that it will overshoot.


Challenge is to decide for how long we need to click so that the rod length is just enough to make us reach the next platform. So 
the problem is to predict or find Duration as a function of Distance (between two consequetive platforms). We can observe that the rod length 
is actually increasing linearly with duration of hold. To verify this, we vary the duration for which we click and hold, 
and find out the rod length in each scenario and these data points are plotted:

![Sample Points](https://github.com/tusharsircar95/GameBot/blob/master/Stick%20Hero/Plot_SamplePoints.jpeg)

As expected the trend is linear. A line is fitted using linear regression to obtain coefficients and this is used to predict duration 
based on the distance between the two platforms.


![Regression](https://github.com/tusharsircar95/GameBot/blob/master/Stick%20Hero/Plot_Regression.jpeg)

##Future Improvements
Make the algorithm machine learning based so that the coefficients or duration to hold will be learnt by the bot itself over time
