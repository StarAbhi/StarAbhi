#import pandas python module as pd
import pandas as pd
#now create a pandas Series from given  data and name idSeries
idSeries = pd.Series([66666 , 99999, 00000])
#now create a pandas Series from given  data and name genderSeries
genderSeries =pd.Series(['Female', 'Male', 'Female'])
#now we have to create a dataframe from idSeries and genderSeries 
#with col name id and gender so make a dict key is col name and values is Series  
frame = { 'Id': idSeries, 'Gender': genderSeries } 
#now create dataframe by frame and store it in result 
result = pd.DataFrame(frame)
#now print first 5 observations from result by using head() 
print(result.head(5))
