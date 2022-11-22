swear = [    "patron", "durak", "puzan", "pomidor", "gorila", "kotleta",
    "v pope bita", "hochu schastya", "sidor", "gnida", "viza",
    "sliva", "dinya", "glina", "prima", "vkusiliy",
    "vagina", "parasha", "sralya", "v pope pulya",
    "bugor", "senior", "sosiska", "lubit fey", "zhopa",
    "kiska", "pipiska", "chlen", "poloniy", "hren",
    "penis", "holera", "mraz", "hernya", "stakan",
    "divan", "vax", "pena", "govniil", "lubitel raket", "hrusha"
    ]
print ("\n")
name = input("Say your name, and this programm will hurt you (maybe): ")
print ("\n")
a = len(name) - 3
rif = name[a:]
for i in swear:
    k=1
    g = len(i) - 3
    if i[g:] == rif:
        print (name.title() + " - " + i + "\n")
print ("\n")
