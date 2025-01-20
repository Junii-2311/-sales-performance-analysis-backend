import pandas as pd

# def load_data(file_path):
#     """
#     Loads sales data from a CSV or JSON file.

#     Args:
#         file_path (str): Path to the data file.

#     Returns:
#         pandas.DataFrame: Loaded sales data.

#     Raises:
#         ValueError: If the file format is unsupported.
#     """
#     try:
#         # Check file extension and load accordingly
#         if file_path.endswith('.csv'):
#             data = pd.read_csv(file_path)
#         elif file_path.endswith('.json'):
#             data = pd.read_json(file_path)
#         else:
#             raise ValueError("Unsupported file format. Only CSV and JSON are allowed.")
        
#         return data
#     except Exception as e:
#         raise RuntimeError(f"Error loading data: {e}")

# if __name__ == "__main__":
#     # Test the function with a sample CSV file
#     test_file_path = "../data/sales_performance_data.csv"
#     print("Testing Data Ingestion...")
#     try:
#         df = load_data(test_file_path)
#         print(f"Data loaded successfully. Shape: {df.shape}")
#         print(df.head())  # Display first few rows of the DataFrame
#     except Exception as e:
#         print(f"Error: {e}")




import pandas as pd

def load_sales_data(file_path: str):
    """
    Loads sales data from a CSV or JSON file.
    
    """
    try:
        if file_path.endswith('.csv'):
            data = pd.read_csv(file_path)
        elif file_path.endswith('.json'):
            data = pd.read_json(file_path)
        else:
            raise ValueError("Unsupported file format")
        return data
    except Exception as e:
        return {"error": f"Failed to load data: {str(e)}"}
