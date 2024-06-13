import pandas as pd

def  lambda_handler(event,context):
    d= {'ceil':[1,2],'ceil2': [3,4]}
    df = pd.DataFrame(data=d)
    print(df)
    print('Done x1.0')
