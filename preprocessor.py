import pandas as pd
import re

def preprocess(data):
    # Fix narrow no-break space \u202f if present
    data = data.replace('\u202f', ' ')
    
    pattern = r'\[(\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}:\d{2}\s[AP]M)\]'
    # Split messages by the date pattern
    messages = re.split(pattern, data)[1:]  # split returns list starting with empty, so skip first
    
    # dates are at odd indexes: 0,2,4,... after splitting
    dates = messages[::2]
    user_msgs = messages[1::2]
    
    df = pd.DataFrame({'date': dates, 'user_message': user_msgs})
    
    # Convert to datetime
    df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y, %I:%M:%S %p')
    
    users = []
    messages = []
    for message in df['user_message']:
        entry = re.split(r'([\w\W]+?):\s', message, maxsplit=1)
        if len(entry) >= 3:
            users.append(entry[1])
            messages.append(entry[2])
        else:
            users.append('group_notification')
            messages.append(entry[0])

    df['user'] = users
    df['message'] = messages
    df.drop(columns=['user_message'], inplace=True)
    
    # Extract datetime features
    df['only_date']=df['date'].dt.date
    df['year'] = df['date'].dt.year
    df['month_num']=df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name']=df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    return df
