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

#In the previous screen we were able to parse the headers from a csv file. With these headers, a helpful function for analyzing a dataset is to grab all the column data for a given header label. This is helpful since you might want to extract data from a specific column of a dataset and then process it.
#Looking at nfl_data, you may notice that the header's index lines up with the rest of the rows. To grab the column data, all we need to do is search through the headers, find the index of the given label, and then loop through the rest of the data returning the value of the index every iteration.
# Default display code
class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]

    # Add your method here.
    def column(self, label):
        if label not in self.header:
            return None

        index = 0
        for idx, element in enumerate(self.header):
            if label == element:
                index = idx

        column = []
        for row in self.data:
            column.append(row[index])
        return column


nfl_dataset = Dataset(nfl_data)
year_column = nfl_dataset.column('year')
player_column = nfl_dataset.column('player')


#Let's add a count_unique() method to our class so that a user can choose a label and then get the total amount of unique results in the column. This is not too tricky since we have already done all the hard lifting in the column() method but it returns all the elements in a column. Keep this in mind when writing the count_unique() method.

# Default display code
class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]

    def column(self, label):
        if label not in self.header:
            return None

        index = 0
        for idx, element in enumerate(self.header):
            if label == element:
                index = idx

        column = []
        for row in self.data:
            column.append(row[index])
        return column

    # Add your count unique method here
    def count_unique(self, label):
        unique_results = set(self.column(label))
        count = len(unique_results)
        return count

nfl_dataset = Dataset(nfl_data)
total_years = nfl_dataset.count_unique('year')

Add a method to the Dataset class called __str__()

#Convert the first 10 rows of self.data to a string and set it as the return value.
#Create an instance of the class called nfl_dataset and call print on it.

class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]

    # Add the special method here
    def __str__(self):
        data_string = self.data[:10]
        return str(data_string)

    def column(self, label):
        if label not in self.header:
            return None

        index = 0
        for idx, element in enumerate(self.header):
            if label == element:
                index = idx

        column = []
        for row in self.data:
            column.append(row[index])
        return column


    def count_unique(self, label):
        unique_results = set(self.column(label))
        count = len(unique_results)
        return count

nfl_dataset = Dataset(nfl_data)
print(nfl_dataset)
