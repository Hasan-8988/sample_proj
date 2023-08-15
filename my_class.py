# Create a class that can be called to fix the formatting of the csv in this dir (sample.csv) and return it as a df.
# BONUS: Return the data grouped in the best manner you see fit.
import pandas as pd

class CsvFormatting:
    """This class have multiple functions
    1. To read the csv
    2. To display unformmated data for comparison
    3. To format the csv and show that in data frame
    4. To group data and show results according to that group
    """
    def __init__(self, csv_path):
        self.csv_path = csv_path

    def read_csv(self):
        df = pd.read_csv(self.csv_path)
        return df

    def unformated_df(self):
        print("This is Unformatted Data Frame:")
        print(self.read_csv())

    def formatted_df(self):
        df = self.read_csv()
        df.replace('   ', "$0", inplace=True)
        null_col = df.columns[df.isna().any()].tolist()
        for data in null_col:
            df[data].fillna(value='$0', inplace=True)
        all_columns = df.columns.tolist()
        for data in all_columns[2:]:
            df[data] = df[data].str.replace('$', '')
            df[data] = df[data].apply(lambda x: f'${x}' if isinstance(x, str) else x)
        df = df.sort_values(by='Master')
        print("This is the Foramatted Data Frame:")
        print(df)
        return df

    def group_data_frame(self):
        df = self.formatted_df()
        all_columns = df.columns.tolist()
        for data in all_columns[2:]:
            df[data] = df[data].str.replace('$', '').astype(float)

        df = df.groupby('Master').agg({
            'Revenue': 'sum',
            'Profit': 'sum',
            'Cost': 'sum',
            'Expense': 'sum',
            'Income': 'sum',
            'Price': 'sum',
            'Salary': 'sum',
            'Investment': 'sum'
        }).reset_index()
        for data in all_columns[2:]:
            df[data] = df[data].apply(lambda x: f'${x}' if isinstance(x, float) else x)
        print("These are the results of grouped data frame and are grouped by Master column")
        print(df)


if __name__ == "__main__":
    csv_path = "./sample.csv"

    obj = CsvFormatting(csv_path)
    obj.unformated_df()
    obj.formatted_df()
    obj.group_data_frame()