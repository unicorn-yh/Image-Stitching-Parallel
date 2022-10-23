# importing the required module
import matplotlib.pyplot as plt

x = [1,2,4,8,16]
y = [18.056,17.170,13.587,12.328,11.444]
plt.plot(x, y,label='Detect Keypoint')
plt.legend()
# naming the x axis
plt.xlabel('Thread Number')
# naming the y axis
plt.ylabel('Execution Time')

# giving a title to my graph
plt.title('')

# function to show the plot
plt.show()

x = [1,2,4,8,16]
y = [10.272,8.086,5.614,5.346,5.258]
plt.plot(x, y,label='Match Keypoint')
plt.legend()
# naming the x axis
plt.xlabel('Thread Number')
# naming the y axis
plt.ylabel('Execution Time')

# giving a title to my graph
plt.title('')

# function to show the plot
plt.show()

x = [1,2,4,8,16]
y = [0.328,0.270,0.266,0.264,0.259]
plt.plot(x, y,label='Homograph Transform')
plt.legend()

# naming the x axis
plt.xlabel('Thread Number')
# naming the y axis
plt.ylabel('Execution Time')

# giving a title to my graph
plt.title('')

# function to show the plot
plt.show()
