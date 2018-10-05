from dataHandler import readCSV
from functions import writeTheta, predict

import matplotlib.pyplot as plt


##il faut normaliser


def train():
    #read the data
    km = readCSV()["km"]
    price = readCSV()["price"]

    #need to normalize the data
    #compute mean and standard deviation for km and price
    sum_km = 0
    sum_2_km = 0
    sum_price = 0
    sum_2_price = 0
    for i in km :
        sum_km += i
        sum_2_km += i**2
    for i in price :
        sum_price += i
        sum_2_price += i**2

    mean_km = sum_km/len(km)
    std_km = (sum_2_km/len(km)-(mean_km)**2)**0.5
    mean_price = sum_price/len(price)
    std_price = (sum_2_price/len(price)-(mean_price)**2)**0.5

    #normalisation
    km_norm = []
    price_norm = []

    for i in range(len(km)) :
        km_norm.append((km[i]-mean_km)/std_km)
        price_norm.append((price[i]-mean_price)/std_price)

    #initialisation of the constants
    theta0 = 0
    theta1 = 0
    learning_rate= 0.01

    list_theta0 = []
    list_theta1 = []
    list_loss = []

    #loop 1000 times
    for n_iter in range (1000):
        tmp0 = 0
        tmp1 = 0
        #computation of the derivation
        for i in range(len(km)):
            tmp0 += predict(km_norm[i],[theta0,theta1]) - price_norm[i]
            tmp1 += (predict(km_norm[i],[theta0,theta1])-price_norm[i])*km_norm[i]

        tmp0 = learning_rate*float(tmp0)/len(km)
        tmp1 = learning_rate*float(tmp1)/len(km)
        #update theta0 and theta1
        theta0 = (theta0-tmp0)
        theta1 = theta1-tmp1
        #keep track of the values computed
        list_theta0.append(theta0)
        list_theta1.append(theta1)
        list_loss.append(abs(tmp0/learning_rate))




    #we rescale theta0 and theta1
    # price_norm = th0_norm+th1_norm*km_norm
    #(price-mean_price)/std_price = th0_norm+th1_norm*(km-mean_km)/std_km
    theta0 = theta0*std_price+mean_price-theta1*mean_km*std_price/std_km
    theta1 = theta1*std_price/std_km
    #write the theta in a pickle document, to avoid recompute them each time we need thme
    writeTheta([theta0, theta1])
    print("theta0 : ",theta0)
    print("theta1 : ",theta1)
    return {"t0":list_theta0,"t1":list_theta1,"loss":list_loss}


train()


#idee :
# gerer NA
