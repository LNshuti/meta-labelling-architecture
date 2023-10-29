import unittest
import pandas as pd
import numpy as np 
import streamlit_app  # Assuming the code is in a file named 'streamlit_app.py'

class TestStreamlitApp(unittest.TestCase):

    def test_load_data(self):
        # Test the load_data function
        data = streamlit_app.load_data()
        self.assertIsNotNone(data)  # Check if data is not None

    def test_train_model(self):
        # Test the train_model function
        # Create a dummy data frame for testing
        dummy_data = pd.DataFrame({
            'time': pd.date_range('2023-01-01', periods=100, freq='H'),
            'price': np.random.rand(100)
        })
        model, mse = streamlit_app.train_model(dummy_data)
        self.assertIsNotNone(model)  # Check if model is not None
        self.assertIsInstance(mse, float)  # Check if mse is a float

    # Add more tests for other functions if needed

if __name__ == '__main__':
    unittest.main()
