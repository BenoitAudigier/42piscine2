import matplotlib.pyplot as plt
from dataHandler import readCSV
from functions import readTheta
from train import train


#vis of the distribution of the initial data
def representation_data():
  km = readCSV()["km"]
  price = readCSV()["price"]
  plt.plot(km,price,'o')
  plt.title("Visualisation of the data")
  plt.xlabel("Distance parcourue (en km)")
  plt.ylabel("Prix du kilomètre")
  plt.show()

#vis of the result, with the linear regression
def representation_final():
  km = readCSV()["km"]
  price = readCSV()["price"]
  theta = readTheta()

  pred = []
  for j in km:
      pred.append(theta[0]+theta[1]*j)
  plt.plot(km,price,'o')
  plt.plot(km,pred)
  plt.title("Visualisation of the linear rgression")
  plt.xlabel("Distance parcourue (en km)")
  plt.ylabel("Prix du kilomètre")
  plt.show()

#vis of the evolution of theta0, theta1 and loss along the iterations
def evolution_iter():
    res = train()
    x = range(len(res["t0"]))
    t0 = res["t0"]
    t1 = res["t1"]
    loss = res["loss"]
    f,ax = plt.subplots(1,3,figsize=[20,5])
    ax[0].plot(x,t0)
    ax[0].set_title("Evolution of theta_0")
    ax[1].plot(x,t1)
    ax[1].set_title("Evolution of theta_1")
    ax[2].plot(x,loss)
    ax[2].set_title("Evolution of loss")
    plt.show()


representation_data()
representation_final()
evolution_iter()
