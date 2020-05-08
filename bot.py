import dataset
import headers
import json
import re
import requests

# Realiza o login e obtém a resposta.
login_response = requests.post(dataset.login_url, headers = headers.login, json = dataset.login_data)

# Verifica se o login foi realizado com sucesso.
if not login_response.ok:
    input(" Something is wrong =/")
    quit()
    
# Obtém o token de acesso.
token = json.loads(login_response.content.decode())
print(" %s has been connected." % token["data"]["name"])

# Coloca o token nos headers da requisição de envio de vídeo.
headers.send["x-access-token"] = token["token"]
count = 0

print("\n Bot is running...")

while True:
    
    # Envia o vídeo e o contabiliza caso o envio esteja OK.
    send_response = requests.post(dataset.send_url, headers = headers.send, json = dataset.send_data)
    if send_response.ok: count += 1
    
    # Obtém a mensagem e o tempo de espera até que o próximo vídeo seja enviado
    message = json.loads(send_response.content.decode())["message"]
    result = re.findall("\d+", message)
    waiting_time = int(result[0]) if result else 0
    
    # Mostra o número de vídeo enviados e o tempo de espera até enviar o próximo vídeo.
    info = f"%i video{'s' if count > 1 else ''} shared in this session. Waiting %02d seconds." % (count, waiting_time)
    print("\r Status: ", end = info)


