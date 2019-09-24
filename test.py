a = '1232....flow_cts_source_groupe_tag'
b = a.replace('..', '.').replace('..','.').replace('.','\':\'')
c = b.split('\n')
for line in c:
    line = '\'' + line +'\','
    print(line)
