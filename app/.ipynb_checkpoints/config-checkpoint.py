import requests

client_id = 'tn9oskedgjzumaz7seved6dl8z642j'
client_secret = '5bbdqqsykhqu6t4fhroopms0hcvy6w'

access_code = requests.post('https://id.twitch.tv/oauth2/token?client_id='+client_id+\
                            '&client_secret='+client_secret+\
                            '&grant_type=client_credentials')


access_token = access_code.json()['access_token']
                            
headers = {
    'Client-ID' : client_id,
    'Authorization' : 'Bearer '+access_token
}

server = 'mongodb+srv://spikeymikeyy:Endoplasm1c@cluster0.hd11y.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'