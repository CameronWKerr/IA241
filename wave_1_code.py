# Cameron Kerr
# Language: Python 3.9.1
# This program plots an exponentially decaying sound wave

import matplotlib.pyplot as plt
import math
def main():
  # generate integers to store in x list
  x=[i*.1 for i in range (111)]

  # use list x to generate y values
  y=[5*(math.exp(-t))*math.cos(2*math.pi*t) for t in x]

  # plot data
  plt.plot(x,y, color='green')

  # labels
  plt.xlabel('time(seconds)')
  plt.ylabel('intensity(W/m^2)')

  # title
  plt.title('Exponentially Decaying Sound Wave')

  # save
  plt.savefig('kerr_1_wave.png')

  # show plot
  plt.show()

main()
