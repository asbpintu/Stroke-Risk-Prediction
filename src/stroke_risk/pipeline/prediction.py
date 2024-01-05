import joblib
from pathlib import Path

class PredictionFromData:
    def __init__(self, user_data) -> None:
        self.userdata = user_data

    
    def making_nested_list(self):
        data_dict = self.userdata
        nested_list = []
        for key, value in data_dict.items():
            if value == 'Govt. Job':
                value = [1, 0, 0, 0]
                nested_list.append(value)
            elif value == 'Un-Employed':
                value = [0, 1, 0, 0]
                nested_list.append(value)
            elif value == 'Private Job':
                value = [0, 0, 1, 0]
                nested_list.append(value)
            elif value == 'Self Employed':
                value = [0, 0, 0, 1]
                nested_list.append(value)
            elif value == 'formerly Smoked':
                value = [1, 0, 0]
                nested_list.append(value)
            elif value == 'Never Smoked':
                value = [0, 1, 0]
                nested_list.append(value)
            elif value == 'Smokes':
                value = [0, 0, 1]
                nested_list.append(value)
            else:
                nested_list.append(value)
        return nested_list
    

    def typecasting(self):
        nested_list = self.making_nested_list()
        zero = ['Female', 'No', 'UnMarried', 'Rural']
        one = ['Male', 'Yes', 'Married', 'Urban']
        nested_list_casted = []
        for item in nested_list:
            if item in one:
                m_item = 1
                nested_list_casted.append(m_item)
            elif item in zero:
                m_item = 0
                nested_list_casted.append(m_item)
            else:
                nested_list_casted.append(item)
        return nested_list_casted


    def making_flatten_list(self):
        nested_list_casted = self.typecasting()
        flattened_list = []
        for item in nested_list_casted:
            if isinstance(item, list):
                flattened_list.extend(item)
            else:
                flattened_list.append(item)
        return flattened_list
    
    def predict(self):
        final_data = [self.making_flatten_list()]

        model = joblib.load(Path('model\model.joblib'))
        result = model.predict(final_data)
        prob = model.predict_proba(final_data)

        if result == 0:
            prediction_value = "You don't have a Brain Stroke Risk"
            return prediction_value , prob
        else:
            prediction_value = "You have a Brain Stroke Risk"
            return prediction_value , prob