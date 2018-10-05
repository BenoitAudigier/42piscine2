import pickle
import numpy as np

# pickling a dict
def writeTheta(theta):
    with open("params/theta.P", "wb") as fp:
        pickle.dump(theta, fp)

# unpickling a dict
def readTheta():
    try:
        with open("params/theta.P", "rb") as fp: # Pickling
            theta = pickle.load(fp)
        return(theta)
    except IOError:
        return(None)

def askMileage(alreadyAsked = False):
    try:
        if(alreadyAsked): mil = input("Dude, an integer. Ain't that hard eh?? Last chance. ")
        else: mil = input("Would you be kind to give me a mileage as an integer? ")
        print("Thanks.")
        return(mil)
    except NameError:
        if(alreadyAsked):
            return(None)
        else:
            return(askMileage(True))

def predict(mileage, theta):
    return(theta[0] + mileage*theta[1])

#print(predict(200,[20,30]))
