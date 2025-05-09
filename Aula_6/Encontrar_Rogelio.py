
import requests
from datetime import datetime


timestamp_inicio = int(datetime(2025, 5, 12).timestamp())
timestamp_fim = int(datetime(2025, 5, 16).timestamp())

 
identificadores = range(9500, 10000)

for id in identificadores:
    print(f"A verificar ID: {id}")
    
    url = ("https://trainingserver.atec.pt/TrainingServer/Mulberry/JSON/Controls/Calendar/getCalendarDataSource.ashx"
        f"?command=_SelectAllSchedulesDataSetGivenByUserId&oId={id}"
        f"&idField=DataValueField&titleField=DataTextField&startDateField=DataStartField"
        f"&endDateField=DataEndField&backgroundColorField=&textColorField=textcolor"
        f"&eventColorField=color&description=description&picField=pic&urlField=url"
        f"&start={timestamp_inicio}&end={timestamp_fim}")
    
    try:
        resposta = requests.get(url)
        conteudo = resposta.json()
    except Exception as erro:
        print(f"Erro ao consultar o ID {id}: {erro}")
        continue


    for evento in conteudo:
        texto = str(evento).lower()
        if "sessão como formador" in texto and "rogélio" in texto:
            print("\n>> Formador Rogélio identificado!")
            print(f"ID do utilizador: {id}")
            print("Detalhes:", evento)
            quit()

print("\nNenhum registo correspondente foi localizado no intervalo dado.")

