########################################################################################################################
# REMARKS
########################################################################################################################
'''
## Coding
- please note, this no SE course and much of the code in ML is more akin to executing workflows
- please try to use the scripts as a documentation of your analysis, including comments, results and interpretations

## GRADING
- Please refer to the moodle course for grading information

## UPLOAD
- upload your solution on Moodle as: "yourLASTNAME_yourFIRSTNAME_yourMOODLE-UID___exercise_blockX.py"
- please no non-ascii characters on last/first name :)
- NO zipfile, NO data!, ONLY the .py file!

## PRE-CODED Parts
- all exercises might contain parts which where not yet discussed in the course
- these sections are pre-coded then and you are encouraged to research their meaning ahead of the course
- so, if you find something in the exercise description you haven´t heard about, look at the ode section and check if this is pre-coded

## ERRORS
- when you open exercise files you'll see error (e.g. unassigned variables)
- this is due to the fact that some parts are missing, and you should fill them in
'''


########################################################################################################################
# IMPORTS
########################################################################################################################


import pandas as pd
import numpy as np


########################################################################################################################
# PART 1 // IMPLEMENT A STUMP USING ONLY BASIC PACKAGES
########################################################################################################################
'''
- implement a decision stump - only the building phase
- a stump is a decision tree with depth one
- to find the best split one must loop over all attributes and over all meaningful split values (=split point candidates) along an attribute
- please see the docstring of ex1() for details
- in this exercise we will use the vertebral column data set https://archive.ics.uci.edu/ml/datasets/Vertebral+Column

    data:
    -----
    data_ex1_vertebral_column_3C.dat

    what you DONT need to care about:
    ---------------------------------
    - you do not need to care about missing values, exception handling, ...
    - you do not need to care about categorical attributes

    what you NEED to care about:
    ----------------------------
    - splits are based on entropy and information gain
        - CHECK THE PDF FILE ON ENTROPY ON HOW THIS MEASURE IS CALCULATED!
    - features and (unique!) values should be evaluated in order
        - features: starting with index 0
        - values: start with smallest value (sorting)
    - use <= as a comparison operator. if values are <= x --> left branch (true), otherwise right branch
    - prevent evaluating unnecessary split point candidates which lead to empty partitions!
    - use feature values of sample points as split point candidates (no "in-between" calculation)
    - all entropy calculation results must be rounded to 6 decimals (np.round(x,6))
    - all information gain calculation results must be rounded to 6 decimals (np.round(x,6))
        - yes, this implies that information gain will be calculated from already rounded entropy calculations!

    - output is a pandas dataframe which should capture every checked split point candidate when building the stump
    - every row of the data frame contains information about one split point candidate
    - please note, order is important here (features in order, values starting from the smallest possible one)
    
    IMPORTANT:
    ----------
    - please capture the results of the procedure in a dataframe s.t. you can really see what's going on when building 
        a tree
    - for each feature/value combination capture the values listed below!
    - please note: to capture information gain you need to calculate entropy of the parent partition (the root)

    - the output DF must have the following columns
      --------------------------------------
        - feature:object, the feature used when evaluating a split point candidate
        - value:float64, the value the split was attempted on
        - information_gain:float64, the information gain which would have resulted from this split
        - h_left:float64, entropy of the left partition for the corresponding split point candidate
        - h_right:float64, entropy of the right partition for the corresponding split point candddate
    '''

# read the data ----------------------------------
# -- precoded --
cols = ["pelvic_incidence", "pelvic_tilt", "lumbar_lordosis_angle", "sacral_slope", "pelvic_radius",
        "degree_spondylolisthesis", "class"
       ]
pth = r'C:\Users\Lenovo\Desktop\FH\SS23\DSML\TreesExample\data_ex1_vertebral_column_3C.dat'
df = pd.read_csv(pth, sep=' ', header=None, names=cols)

# stump --------------------------------------------
# -- student work --
def stump(df):
    def EntropyCalc(y):
        _, counts = np.unique(y, return_counts=True)
        p = counts /len(y)
        #value = np.mean(y) # if the mean is 0 or 1
    # making the entropy from randome data, because we dont need randomness or uncertiniaty, only 1 and 0
    # for the entropy 0 is perfect
        #if value == 0 or value == 1:
         #   return 0
        #else:
         #   return -np.sum(value * np.log2(value))
        return -np.sum(p*np.log2(p))

#information gathering
    def information(value,_left, _right):

        hIndex = EntropyCalc(value) # target variable
        hLeft = EntropyCalc(_left)
        hRight = EntropyCalc(_right) # split
        nth = len(value)
        nthLeft = len(_left)
        nthRight = len(_right)
        return hIndex - (nthLeft / nth * hLeft + nthRight / nth * hRight)
 #the output DF must have the following columns

  #    --------------------------------------
   #     - feature:object, the feature used when evaluating a split point candidate
    #    - value:float64, the value the split was attempted on
     #   - information_gain:float64, the information gain which would have resulted from this split
      #  - h_left:float64, entropy of the left partition for the corresponding split point candidate
       # - h_right:float64, entropy of the right partition for the corresponding split point candddate
#Create dataframe
    solution = pd.DataFrame(columns=["feature", "value","information_gain", "h_left","h_right"])


    for feature in df.columns[:-1]:
    #uniquel values
    #sorts the unique values
        unique_values = np.sort(df[feature].unique())

    #loop over all split points
        for k in range(len(unique_values)-1):
            _splits = (unique_values[k] + unique_values[k+1])/2
        #chose or put in partition -> left or right
            leftPart = df[df[feature] <= _splits]["class"].values
            rightPart = df[df[feature] > _splits]["class"].values
        # check if its empty
            if len(rightPart) == 0 or len(leftPart) ==0:
                continue

            #inforamtion calculation
            iCalc= information(df["class"].values, leftPart, rightPart)

            # entropy of part.

            E_left = EntropyCalc(leftPart)
            E_right = EntropyCalc(rightPart)

            solution = solution.append({"feature": feature,
                                    "value": _splits,
                                    "information_gain": np.round(iCalc, 6),
                                    "h_left": np.round(E_left, 6),
                                    "h_right": np.round(E_right, 6)}, ignore_index=True)

    return solution



_function = stump(df)

print(_function)
#solution = ""




