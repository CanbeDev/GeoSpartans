import pickle

# Load the pickle file to inspect its contents
with open("C:\\Users\\PC\\OneDrive - University of Johannesburg\\Desktop\\FLASK_TASK\\model_and_preprocessor.pkl", 'rb') as file:
    content = pickle.load(file)
    print(type(content))
    print(len(content))
    print(content)
