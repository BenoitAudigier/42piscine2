import csv


# Give back str or float following the str given as argument
def to_number_or_str(s):
    try:
        s = float(s)
        return s
    except ValueError:
        return s

# Reads a correctly formed csv
def readCSV():
    res = dict() # Storing the res with key = colomn name and val = list of values
    colNames = dict() # Storing the index of each colomn names to remember the order when parcouring the text file
    with open("resources/data.csv") as csv_file: # Should be already a valid file. Few improvements could be made (checking the length of rows and such) but let's suppose we have a valid data set
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader: # Reading the lines
            if line_count == 0: # Treating the headers
                for i in range(len(row)):
                    colNames[i] = row[i]
                    res[row[i]] = []
                line_count += 1
            else:
                for i in range(len(row)): # adding the values to each column
                    res[colNames[i]] += [to_number_or_str(row[i])]
                # line_count += 1
    return res
