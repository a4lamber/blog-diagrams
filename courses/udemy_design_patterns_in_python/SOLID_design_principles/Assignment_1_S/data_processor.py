class DataReader():
    """
    recall how pandas do the input, 
    
    df = pd.read_csv('file.csv')
    df = pd.read_json('file.json')
    
    It reads it and returns DataFrame object
    """
    @staticmethod
    def read_data(filename):
        """_summary_

        :param _type_ filename: _description_
        """
        with open(filename, mode = 'r') as fh:
            res = [line.strip() for line in fh]
        
        return res
            

# Option 1:
# We can either don't pass the data in as an instance variable. 
# If only a small fraction of our methods is manipulating the data, 
# We don's have to pass it in as an instance variables

            
class DataProcessorOption1:
    def __init__(self):
        pass
    
    def process_data(self, data):
        pass
    

# Option 2:
# if lots of your methods are manipulating the data
# it might be worthwhile pass it in as an instance variable
# it's clearer and cleaner that way

class DataProcessorOption2:
    def __init__(self, data):
        self.data = data
        
    def process_data_method_a(self):
        pass
    
    def process_data_method_b(self):
        pass
    

        
    