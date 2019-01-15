#PYTHON DATA Science

#* Add a data parameter to the __init__() method, and set the value to the self.data attribute.
#* Read the data from nfl.csv and set it to the variable nfl_data.
#* Make an instance of the class, passing in nfl_data to the __init__()method (when you call Dataset(...)).
#* Assign the result to the variable nfl_dataset.
#* Use the data attribute to access the underlying data for nfl_dataset and assign the result to the variable dataset_data.


# Default display code
class Dataset:
    def __init__(self, data):
        self.type = "csv"
        self.data = data

f = open("nfl.csv", 'r')
csvreader = csv.reader(f)
nfl_data = list(csvreader)

nfl_dataset = Dataset(nfl_data)
dataset_data = nfl_dataset.data

____________
# Default display code
class Dataset:
    def __init__(self, data):
        self.data = data

    # Your method goes here
    def print_data(self, num_rows):
        print(self.data[:num_rows])

nfl_dataset = Dataset(nfl_data)
print(nfl_dataset.print_data(5))


#You may have noticed when printing the data that the first element in the list of rows contains some header information. Using the csv module, we don't have a way of extracting this header unless we grab the first element. However, with our dataset class, we could add an instance method that would grab the first result of self.data, set it as a header attribute, and then remove it from the data attribute. Let's try that now:

# Default display code
class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]

nfl_dataset = Dataset(nfl_data)
nfl_header = nfl_dataset.header
