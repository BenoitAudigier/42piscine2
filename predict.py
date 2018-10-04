from functions import askMileage, predict

def main():
    mil = askMileage()
    if(mil is None):
        print("Alright I warned you. Bye.")
        return("None")

    predict(mil)

main()
