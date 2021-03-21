voti = {"Mario": {"Matematica": 6, "Italiano": 6, "Scienze": 7, "Inglese": 4},
"Giovanni": {"Matematica": 4, "Italiano": 6, "Scienze": 5, "Inglese": 7},
"Paola": {"Matematica": 9, "Italiano": 6, "Scienze": 8, "Inglese": 8}}
n_voti = len(voti["Mario"])
media_Mario = ((voti["Mario"]["Matematica"]) + (voti["Mario"]["Italiano"]) + (voti["Mario"]["Scienze"]) + (voti["Mario"]["Inglese"])) / int(n_voti)
print("Media Mario: ", media_Mario)
media_Giovanni = ((voti["Giovanni"]["Matematica"]) + (voti["Giovanni"]["Italiano"]) + (voti["Giovanni"]["Scienze"]) + (voti["Giovanni"]["Inglese"])) / int(n_voti)
print("Media Giovanni: ", media_Giovanni)
media_Paola = ((voti["Paola"]["Matematica"]) + (voti["Paola"]["Italiano"]) + (voti["Paola"]["Scienze"]) + (voti["Paola"]["Inglese"])) / int(n_voti)
print("Media Paola: ", media_Paola)