import pandas as pd

def  lambda_handler(event,context):
    d= {'ceil':[5,6],'ceil2': [3,4]}
    df = pd.DataFrame(data=d)
    print(df)
    print('Done x1.1')
