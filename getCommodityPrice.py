
# coding: utf-8

# In[2]:

import argparse
import pandas as pd
import numpy as np
def main():
    # Parse arguments from command line
    parser = argparse.ArgumentParser()

    # Set up required arguments this script
    parser.add_argument('function', type=str, help='function to call')
    parser.add_argument('start_date', type=str, help='first argument')
    parser.add_argument('end_date', type=str, help='second argument')
    parser.add_argument('commodity_type', type=str, help='third argument')

    # Parse the given arguments
    args = parser.parse_args()

    # Get the function based on the command line argument and 
    # call it with the other two command line arguments as 
    # function arguments
    eval(args.function)(args. start_date, args. end_date, args.commodity_type)

def getCommodityPrice(start_date,end_date,commodity_type):
    
    if (commodity_type == 'gold'):
      data = pd.read_csv('gold.csv', sep=';')
    else:
      data = pd.read_csv('silver.csv', sep=';')
    mean = data['Price'].mean()
    variance = np.var(data['Price'])
    new = commodity_type + " "+str(mean) +" " +str(variance)
    print (new)

if __name__ == '__main__':
    main()


# In[ ]:



