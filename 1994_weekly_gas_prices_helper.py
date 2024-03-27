import matplotlib.pyplot as plt

# Cameron Kerr

# Create your function (or functions) to compute statistics

def main():
	# Open the gas data file.
  infile = open('1994_Weekly_Gas_Averages.txt', 'r')

    # Read and process the file contents and store in a list (these are your y-values).
  prices = infile.readlines()

    # Close the file.
  infile.close

    # Print the list
  index = 0
  while index<len(prices):
    prices[index]=float(prices[index])
  print(prices)

    # compute the statistics
  minimum = min(prices)
  maximum = max(prices)
  average = sum(prices)/len(prices)

  return minimum
  return maximum
  return average
  
    # Print the statistics
  print('The minimum gas price was: ', minimum)
  print('The maximum gas price was: ', maximum)
  print('The average gas price was: ', average)
    # Create a list containing the week numbers (to use as the x-values).
  weeks = [0]
  while weeks < len(prices):
    weeks += 1
    # Build the graph.
  plt.plot(weeks)
  plt.plot(prices)
    # Add a title.
  plt.title('1994 Weekly Gas Prices')
    # Add labels to the axes.
  plt.xlabel('Weeks (by number)')
  plt.ylabel('Average Prices')
    # Display and save the graph.
  plt.savefig('Kerr_1994_gas_prices.png')
  plt.show()
main()
