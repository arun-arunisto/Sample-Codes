def list_none_conversion(table):
    for i in range(len(table)):
        table[i] = list(table[i])

    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] == None:
                table[i][j] =" "
    return table
