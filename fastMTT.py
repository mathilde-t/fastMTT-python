import numpy as np
from MeasuredTauLepton import *

###Reference: https://github.com/SVfit/ClassicSVfit/blob/fastMTT_2024/src/FastMTT.cc ###

class Likelihood:
    def __init__(self, Leptonparams, aMET, aCovMET, aPars = np.array([6, 1/1.15])):
        #Here we define all the parameters of the function (self.X)
        #and we will initialise the Leptonparams according to the setLeptonInputs function from the original code
        #(unless, for clarity, it is better to do this in a separate function and paste)
        return
    
    def massLikelihood(self, m):
        #Implementation
        return #value
    
    def ptLikelihood(self, pTTauTau, type):
        #Implementation
        return #value
    
    def metTF(metP4, nuP4, covMET):
        #Implementation
        return #value
    
   """Attention
    ComponentParams will replace enable/disable Component
    which (if I understand correctly) include or not specific probabilities (pt, metTF, mass) in the final result
    We can do this in value or in __init__ - I don't yet know what is needed for the code to work properly."""

    def value(self, x, ComponentsParams = True):
        #Implementation
        #contains references to massLikelihood, ptLikelihood, metTF
        #as long as they are unlocked when the function is defined
        return

###ATTENTION###
"""numba does not support inheritance of functions so the preferred compiler is probably jit.
Nevertheless, rewriting the code to a single class should not possibly be a problem either 
(sooner for MeasuredTauLepton than for likelihood).
If the performance with numba would be significantly greater so by default I would write 
the code with jit, and then possibly check how it works with numba (if we consider that 
Implementation is not too heavy compared to the result)"""

class FastMTT(Likelihood):
    def __init__(self):
        #initialisation
        #aPars and ComponentParams parameters by inheritance from Likelihood
        #We will let go of initialising things for minimisation, since it is not in the code anyway
        return
    
    def run(self, measuredTauLeptons: np.ndarray, measuredMETx, measuredMETy, covMET) -> np.ndarray:
        return
    
    def compareLeptons(self, measuredTauLepton1: MeasuredTauLepton, measuredTauLepton2: MeasuredTauLepton): #used in the run
        #Implementation
        return
    
    def scan(self): #used in the run
        #Uses MyLikelihood.value
        #Implementation with loops
        #or gradient_descent (it was mentioned in the article that it can improve the speed of the algorithm)
        return
    
"""To all of this, we will add functions for timing (e.g. import time) for testing, as in the original code"""