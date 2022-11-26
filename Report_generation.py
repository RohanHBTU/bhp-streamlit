import pandas as pd
import pandas as pd
from pandas_profiling import ProfileReport
df=pd.read_csv('Bengaluru_House_Data.csv')
profile=ProfileReport(df)
profile.to_file(output_file='Report.html')