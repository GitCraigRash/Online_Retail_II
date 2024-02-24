import pandas as pd

class Retail_df(pd.DataFrame):
    def total_spending(self):
        return kndf = kndf.loc[kndf["totalspending"]>0].reset_index(drop=True)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

  
