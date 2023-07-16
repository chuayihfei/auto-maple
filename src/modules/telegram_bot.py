#Change this only
API_KEY     = '6257440796:AAEE9etmkpQ6Ppbxfusr1ANKzZ0IJJbrG8Y'
CHAT_ID     = '-999078772'

receive_info    = True
receive_warning = True

#Do not touch the rest below
BASE_URL    = 'https://api.telegram.org/bot' + API_KEY + '/sendMessage?chat_id='+ CHAT_ID

def send_info_msg(message):
    if receive_info:
        import requests
        final_message =  BASE_URL + '&text=' + '[Info] ' + message
        requests.get(final_message)

def send_warning_msg(message):
    if receive_warning:
        import requests
        final_message =  BASE_URL + '&text=' + '[Warning] ' + message
        requests.get(final_message)
