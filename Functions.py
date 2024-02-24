import pandas as pd

class Retail_df(pd.DataFrame):
    def total_spending(self):
        return kndf = kndf.loc[kndf["totalspending"]>0].reset_index(drop=True)

    def total_spending_rank(self):
        return country_totals = (kndf.groupby("country")
                                ["totalspending"]
                                .sum().reset_index()
                                .sort_values(by="totalspending",ascending=False)
                                .reset_index(drop=True))
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

  
