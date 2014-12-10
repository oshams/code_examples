import numpy as np
import matplotlib.pyplot as plt
import math

#How do you remove points on a 2d grid that are below noise level -- ie generateed by a uniform random probability distribution?  
#This method removes noise from a 2d grid at a given sigma level and grid length. e.g. num_of_sigma = 5, grid_len = 10 means that all points  <= 5 standard devs below mean distrubtion on a 10x10 board will be removed
#The method both returns the indices of values to be removed, as well as the values to keep. Can be easily tailored to more specific purposes
def remove_noise(x_vals,y_vals,num_of_sigma,grid_len):
    x_vals = np.array(x_vals)
    y_vals = np.array(y_vals)
    
    if len(x_vals) != len(y_vals):
        raise Exception('mismatched values')
    
    x_range = (max(x_vals)-min(x_vals))
    y_range = (max(y_vals)-min(y_vals))
    x_vals_renorm = (x_vals - min(x_vals))/x_range
    y_vals_renorm = (y_vals - min(y_vals))/y_range

    #OK so store each coordinate according to where in the grid it is.
    #Then go over the grid and remove points (where points assumed to be uniquely identified by value) from list of coords
    
    grid  = [ [[] for j in xrange(grid_len)] for i in xrange(grid_len)]
        
    for i in xrange(len(x_vals_renorm)):
        temp_x_loc = int(x_vals_renorm[i]*grid_len)
        if temp_x_loc == grid_len:
            temp_x_loc=grid_len-1
        temp_y_loc = int(y_vals_renorm[i]*grid_len)
        if temp_y_loc == grid_len:
            temp_y_loc=grid_len-1
        grid[temp_x_loc][temp_y_loc].append(i)
    
    indices_to_remove = []
    x_vals_keep = []
    y_vals_keep = []
    
    for i in xrange(len(grid)):
        for j in xrange(len(grid)):
            cutoff = 1.0*num_of_sigma*math.sqrt(len(x_vals_renorm)/(len(grid)**2.))
            if len(grid[i][j]) < cutoff:
                for elem in grid[i][j]:
                    indices_to_remove.append(elem)
            else:
                for elem in grid[i][j]:
                    x_vals_keep.append(x_vals[elem])
                    y_vals_keep.append(y_vals[elem])
                
    return indices_to_remove, x_vals_keep,y_vals_keep
    
