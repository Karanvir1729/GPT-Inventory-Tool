import csv
import pandas as pd
import openai
import os

openai.api_key = 'OPEN-AI-KEY'

def read_csv_file(str):
    data = {}
    lst = str.split(b'\r\n')
    for i in lst:
        lst_i = i.split(b',')
        for j in range(len(lst_i)):
            data.setdefault(j, []).append(lst_i[j].decode('UTF-8'))
    return data

def detectDuplicates(str):
  csv_data = read_csv_file(str)
  
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt= f'''Words = ['AMRKII', 'BSAAX', 'BZKYUL', 'DLHRPDUMPJ', 'DTYRSLGSCTKW', 'DWLBKSN', 'EEIUAREFCIHZ', 'EHFFVBDUEA', 'ELGYPKRT', 'FCDPDTNIA', 'GFUJPBEAYCM', 'GRQPP', 'HDY', 'HKHOWNSY', 'HWPWZOJZQCKR', 'IWJJPFOV', 'JPAUAQE', 'JXGMV', 'KDCMNSC', 'KGCVYEU', 'KOFGVWXVB', 'KRCI', 'KVS', 'LYSWNKIGSTQZ', 'MEIL', 'NFRLTMGZXMX', 'NPW', 'NSE', 'NVJAPNHATVY', 'OSQX', 'OUBHWNPSDWLY', 'PYKIM', 'QOPCJOEVFM', 'QTMVIJHAY', 'RFOZFZQEHY', 'RJEDRZ', 'RTIIBLPFS', 'STGZLDI', 'UOJY', 'UYVXMHGD', 'VPWUAO', 'VYHJPZWGBB', 'WWXUIC', 'XCFWYWBQMNB', 'XGG', 'XLDECHYOYRR', 'YDDIRCBX', 'YEXN', 'YNYNNQLDD', 'ZRHHV']
    
  Similar words = [('NPW', 'NSE')]

  Words('IG', 'Instagram', 'FB', 'Facebook']

  Similar words =[('IG', 'Instagram'), ('FB', 'Facebook')]

  words = {csv_data[0]} 

  Similar words = ''',
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
  duplicates = eval(response['choices'][0]["text"])

  if duplicates:
    # check for None case
    for i in duplicates:
        csv_data[0].remove(i[0])

  while len(csv_data[1]) != len(csv_data[0]):
      csv_data[1].append('')

  filename = 'output.csv'
  root = os.path.dirname(os.path.abspath(__file__))
  fileoutput = os.path.join(root, "output", filename)

  df = pd.DataFrame(csv_data)
  df.to_csv(fileoutput, index=False)
