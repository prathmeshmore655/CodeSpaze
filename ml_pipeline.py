import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression  
import matplotlib.pyplot as plt



def evaluate_model(model , x_test , y_test):

    score = model.score(x_test , y_test)

    print('Accuracy :' ,score*100)

    return model

    


def train_model(dataset):

    input_data = dataset[['Years of Experience']]
    output_data = dataset['Salary']
    x_train , x_test , y_train , y_test = train_test_split(input_data , output_data , train_size=0.2 , random_state=56)
    model = LinearRegression() 
    model.fit(x_train , y_train)


    return model , x_test , y_test



def process_data(dataset):

    dataset.isnull().sum()
    dataset = dataset.fillna(0)
    dataset = dataset.select_dtypes(include=['int64' , 'float64'])

    return dataset



def load_data(file_path):

    dataset = pd.read_csv(file_path)

    return dataset




def pipeline(file_path):

    data = load_data(file_path)
    processed_data = process_data(data)
    model , x_test , y_test = train_model(processed_data)
    model = evaluate_model(model , x_test , y_test)

    return model

def predict_salary(model,experience):

    predict = model.predict([[experience]])

    print(predict)








if __name__ == "__main__":

    file_path = r'/home/ordinary-person/Downloads/archive/Salary_Data.csv'
    model = pipeline(file_path)
    

    exp = int(input('Enter Your Expereince : '))

    

    sal  = predict_salary(model,exp)
    
      
    print(sal)





