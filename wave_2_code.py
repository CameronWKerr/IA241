# Cameron Kerr
# Language: Python 3.9.1
# This program plots voice identification and sound waves

import matplotlib.pyplot as plt
import math
def main():
  # generate integers to store in x list
  x1=[i*.1 for i in range (111)]
  x2=[i*.1 for i in range (111)]

  # use list x to generate y values
  y1=[3*math.sin(2*math.pi*t) for t in x1]
  y2=[5*(math.exp(-t))*math.cos(2*math.pi*t) for t in x2]

  # plot data
  plt.plot(x1,y1, color='green')
  plt.plot(x2,y2, color='red')

  # create legend
  plt.plot(x1,y1, "green", label='undamped wave')
  plt.plot(x2,y2, "red", label='damped wave')

  # locate legend
  plt.legend(loc='upper left')

  # labels
  plt.xlabel('time(seconds)')
  plt.ylabel('intensity(W/m^2)')

  # title
  plt.title('Voice Identification and Sound Waves')

  # save
  plt.savefig('kerr_1_wave.png')

  # show plot
  plt.show()

main()
