import sys

import pandas as pd
import pythainlp

class TextClassifier:

    def __init__(self, csv_file_name):
        self.model_params = pd.read_csv(csv_file_name, index_col=0) 

    def compute_probability(self, text_string):
        pass

    def get_all_possible_features(self):
        return self.model_params.columns 
        # pass

    def get_all_possible_labels(self):
        return self.model_params.index   
        pass

    def classify(self, text_string):
        pass


if __name__ == '__main__':
    if (len(sys.argv) != 2):
        data = TextClassifier("toy_model.csv")
        # data = TextClassifier("toy_model2.csv")
        print('usage:\tpython logistic_regression.py <model_file>')
        print(data.model_params)
        print(data.get_all_possible_features())
        print(data.get_all_possible_labels())
        text = "Hi Bro, I love you"
        print(data.compute_probability(text))
        print(data.classify(text))  
        sys.exit(0)
    model_file_name = sys.argv[1]
    model = TextClassifier(model_file_name)

