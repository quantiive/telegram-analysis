#importing pandas package
import pandas as pd
import re

# reading JSON file
df = pd.read_json('channel_messages.json')

# displaying sample output
pd.set_option('display.max_columns', None)
#print(df.keys())
#print(df['date'][0],df['message'][0])

#message = df['message'][0]


def trade_extract(message):
    message_split = re.split(' ', message)
    for index, value in enumerate(message_split):
        try:
            if value.isdigit():
                message_split[index] = int(value)

            else:
                message_split[index] = float(value)
        except ValueError:
            continue
    print(message_split)

#print(message)
#print(message_split)


#for i in range(0,50):
#    message_string = df['message'][i]
#    trade_extract(message_string)




###########  transform to readable csv format
data_message = []
data_date = []
for i in range(0,50):
    message_string = df['message'][i]
    date = df['date'][i]

    data_date.append(data_date)
    data_message.append(message_string)





df_ext = df[["date","message"]]

df_ext.to_csv('telegram_messages_version3.csv')


