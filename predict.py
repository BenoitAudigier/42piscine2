import numpy as np

from functions import askMileage, predict, readTheta

def main():
    mil = askMileage()
    if(mil is None):
        print("Alright I warned you. Bye.")
        return("None")

    try:
        theta = readTheta()
        pred = predict(mil, theta)
        print("This very powerful algorithm predicts the price to be around " + pred + " of whatever money that is.")
    except TypeError:
        print("Yeah no I haven't been trained before so I'm gonna try to guess: how about " + str(np.random.randint(-99999999, 99999999)) + "?")
        print("Seriously tho, run python train.py first.")
        return(None)
    predict(mil, theta)

main()
