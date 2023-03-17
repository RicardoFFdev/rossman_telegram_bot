import os
import json
import requests
import pandas    as pd
from   flask     import request, Flask, Response

#constants 6159590353:AAFHyHeAe1cVU8XIe1Gh-DeRFump5VB5Ico
TOKEN = '6159590353:AAFHyHeAe1cVU8XIe1Gh-DeRFump5VB5Ico'

# # Bot info
# https://api.telegram.org/bot6159590353:AAFHyHeAe1cVU8XIe1Gh-DeRFump5VB5Ico/getMe

# # Get updates
# https://api.telegram.org/bot6159590353:AAFHyHeAe1cVU8XIe1Gh-DeRFump5VB5Ico/getUpdates

# Webhook
# https://api.telegram.org/bot6159590353:AAFHyHeAe1cVU8XIe1Gh-DeRFump5VB5Ico/setWebhook?url=https://rossmann-bot-0sne.onrender.com

# sendMessage
# https://api.telegram.org/bot6159590353:AAFHyHeAe1cVU8XIe1Gh-DeRFump5VB5Ico/sendMessage?chat_id=1543189891&text=Testando123!

def send_message(chat_id, text):
    url = 'https://api.telegram.org/bot{}/'.format(TOKEN)
    url = url + 'sendMessage?chat_id={}'.format(chat_id)
    r = requests.post(url, json={'text': text})
    print('Status Code {}'.format(r.status_code))

    return None


def load_dataset(store_id):
    # Test dataset
    df10 = pd.read_csv('csv_files/test.csv')
    df_store_raw = pd.read_csv('csv_files/store.csv')

    # Merging test + store dataset
    df_test = pd.merge(df10, df_store_raw, how='left', on='Store')
    
    # Choosing only one store for prediction test
    df_test = df_test[df_test['Store'] == store_id]
    
    if not df_test.empty:
        # Removing closed days
        df_test = df_test[df_test['Open'] != 0]
        df_test = df_test[~df_test['Open'].isnull()]
        df_test = df_test.drop('Id', axis=1)
        
        # Converting dataframe to json
        data = json.dumps(df_test.to_dict(orient='records'))

    else: 
        data = 'error'

    return data

def predict(data):
    # API Call
    #url = 'https://ricardoffdev-webapp-rossmann-handler-hyn9f6.streamlit.app/rossmann/predict'
    url = 'https://webapp-rossmann-q99w.onrender.com/rossmann/predict'
    header = {'Content-type': 'application/json'}
    data = data
    r = requests.post(url, data=data, headers=header)
    print('Status Code {}'.format(r.status_code))
    d1 = pd.DataFrame(r.json(), columns=r.json()[0].keys())

    return d1


def parse_message(message):
    chat_id = message['message']['chat']['id']
    store_id = message['message']['text']
    store_id = store_id.replace('/', '')

    try:
        store_id = int(store_id)

    except ValueError:
        store_id = 'error'

    return chat_id, store_id

# API Initialize
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        message = request.get_json()

        chat_id, store_id = parse_message(message)

        if store_id != 'error':
            # Loading data
            data = load_dataset(store_id)
        
            if data != 'error':
                # Prediction
                d1 = predict(data)

                # Calculation
                d2 = d1[['store', 'prediction']].groupby('store').sum().reset_index()

                # Send Message
                msg = 'Store number {} will sell ${:,.2f} in the next 6 weeks.'.format(
                            d2['store'].values[0],
                            d2['prediction'].values[0])

                send_message (chat_id, msg)
                return Response('Ok', status=200)

            else:
                send_message(chat_id, 'Store not available')
                return Response('Ok', status=200)
    
        else: 
            send_message(chat_id, 'Store ID is wrong')
            return Response('Ok', status=200)
           
    else:
        return '<h1> Rossmann Telegram BOT </h1>'

if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    app.run(host='0.0.0.0', port=port)