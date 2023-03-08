# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 07:20:04 2023

@author: John Paul J
"""

# Standard imports
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
#Seaborn is a Python data visualization library based on matplotlib. 
#It provides a high-level interface for drawing attractive and informative statistical graphics.

# Bias value
# This can be changed to make the coin biased or unbiased. 
# If it BiVal (Biasing value) is 0.5 the coine is unbiased. 
# Any other value other than 0.5 from 0 to 1 it is biased coin.
BiVal = 0.5


#In probability theory and statistics, Bayes' theorem, 
#named after Thomas Bayes, describes the probability of an event, 
#based on prior knowledge of conditions that might be related to the event.

# We flip n coins and observe h heads,

def binomial(data, n, h):
    # We can ignore the combination since it divides out in the normalization
    # Build up our probabilities
    p = [(x**h * (1 - x)**(n - h)) for x in data]
    
    #Using bionomial distrubitation the probablity is found. 
    
    # Normalizing the probabilities 
    return (p / sum(p))


fig, ax = plt.subplots(figsize=(12, 8))
#to create common layouts of subplots, including the enclosing figure object,
#in a single call.

# Sample points
x = np.arange(0.0, 1.0, 0.01)
#(Start,stop,stepsize)

# Prior is fair coin, so we assume 12 flips, 6 heads.
prior = binomial(x, 12, 6)
ax.plot(x, prior, linewidth=3, color='r', linestyle='-', label='Reference')

# Now simulate posterior for biased coin

# First, 10 coin flips
num_flips = 24
likelihood1 = binomial(x, num_flips, num_flips *BiVal )
post1 = likelihood1 * prior
post1 /= np.sum(post1)
ax.plot(x, post1, linewidth=1, color='c', linestyle='-', 
        label=f'{{{num_flips}, {num_flips * BiVal:4.0f}}}')

# Second, 100 coin flips
num_flips = 100
likelihood2 = binomial(x, num_flips, num_flips * BiVal)
post2 = likelihood2 * prior
post2 /= np.sum(post2)
ax.plot(x, post2, linewidth=1, color='b', linestyle='--', 
        label=f'{{{num_flips}, {num_flips * BiVal:4.0f}}}')

# Third, 1000 coin flips
num_flips = 1000
likelihood3 = binomial(x, num_flips, num_flips * BiVal)
post3 = likelihood3 * prior
post3 /= np.sum(post3)
ax.plot(x, post3, linewidth=2, color='g', linestyle=':', 
        label=f'{{{num_flips}, {num_flips * BiVal:4.0f}}}')

# Decorate plot
ax.set_xlabel("P(H)", fontsize=18)
ax.set_ylabel("Probability", fontsize=18)
ax.set_title("Bell curve using {N tosses, H heads}", fontsize=20)
ax.set_xlim(0, 1)
ax.set_yticks([])

# Plot biased coin value
ax.axvline(BiVal, 0, 1, c='k', linewidth=1, linestyle='-')
ax.legend(loc=1, fontsize = 18)

# Clean-up
sns.despine(offset = 10, trim=True)
#Remove the top and right spines from plot i.e the boder.
#end of the program