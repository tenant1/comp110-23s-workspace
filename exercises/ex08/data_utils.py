from csv import DictReader 

def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read csv file and return as a list of dicts with header keys"""
    result: list[dict[str,str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result

def column_values(table: list[dict[str,str]], header: str) -> list[str]: 
    """Return values in a table column under a specific header"""
    result: list[str] = []
    #step through table
    for row in table:
        #save every value under key "header"
        result.append(row[header])
    return result

def columnar(table: list[dict[str,str]]) -> dict[str,list[str]]: 
    """Reformats data so that it's a dictionary with column header"""
    result: dict[str, list[str]] = {}
    # loop through keys of one row of table
    first_row: dict[str,str] = table[0]
    for key in first_row:
        # for each key, make a dictionary entry with all column values
        result[key] = column_values(table, key)
    return result

def head(table: dict[str, list[str]], N: int) -> dict[str,list[str]]: 
    """Produce a new column-based (e.g. `dict[str, list[str]]`) table with only the first `N` (a parameter) rows of data for each column."""
    result: dict[str, list[str]] = {}

    if (N >= len(list(table.items())[0][1])):
        return table
    
    for column in table:
        firstN = []
        current = table.get(column)
        for i in range(N):
            firstN.append(current[i])
        result[column] = firstN
    return result

def select(table: dict[str, list[str]], selected: list[str]) -> dict[str, list[str]]: 
    """Produce a new column-based (e.g. `dict[str, list[str]]`) table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}

    for column in table:
        if (column in selected):
            current = table.get(column)
            result[column] = current 
    return result 

def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based (e.g. `dict[str, list[str]]`) table with two column-based tables combined."""
    result: dict[str, list[str]] ={}

    for column in table_1:
        current = table_1.get(column)
        result[column] = current

    for column in table_2:
        current = table_2.get(column)

        if (column in result.keys()):
            resultCol = result.get(column)          
            for val in current:
                resultCol.append(val)
            result[column] = resultCol
            
        else:
            result[column] = current
        
    return result

def count(list_1: list[str]) -> dict[str, int]:
    """Given a `list[str]`, this function will produce a `dict[str, int]` where each key is a unique value in the given list and each value associated is the _count_ of the number of times that value appeared in the input list."""
    result: dict[str, int] = {}

    for val in list_1:
        if (val in result.keys()):
                resultKey = result.get(val)
                resultKey = resultKey + 1
                result[val] = resultKey

        else:
            result[val] = 1
    
    return result
