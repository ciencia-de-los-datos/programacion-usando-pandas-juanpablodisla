"""
Laboratorio - Manipulación de Datos usando Pandas
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

Utilice los archivos `tbl0.tsv`, `tbl1.tsv` y `tbl2.tsv`, para resolver las preguntas.

"""
import pandas as pd

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")


def pregunta_01():
    """
    ¿Cuál es la cantidad de filas en la tabla `tbl0.tsv`?

    Rta/
    40

    """
    rows = len(tbl0.axes[0])
    response = rows
    return response


def pregunta_02():
    """
    ¿Cuál es la cantidad de columnas en la tabla `tbl0.tsv`?

    Rta/
    4

    """
    columns = len(tbl0.axes[1])
    response = columns
    return response 


def pregunta_03():
    """
    ¿Cuál es la cantidad de registros por cada letra de la columna _c1 del archivo
    `tbl0.tsv`?

    Rta/
    A     8
    B     7
    C     5
    D     6
    E    14
    Name: _c1, dtype: int64

    """
    account = tbl0["_c1"].value_counts()
    response = account.sort_index()

    return response


def pregunta_04():
    """
    Calcule el promedio de _c2 por cada letra de la _c1 del archivo `tbl0.tsv`.

    Rta/
    A    4.625000
    B    5.142857
    C    5.400000
    D    3.833333
    E    4.785714
    Name: _c2, dtype: float64
    """
    mean_df = tbl0.groupby(by="_c1").mean()
    response = mean_df["_c2"]
    return response


def pregunta_05():
    """
    Calcule el valor máximo de _c2 por cada letra en la columna _c1 del archivo
    `tbl0.tsv`.

    Rta/
    _c1
    A    9
    B    9
    C    9
    D    7
    E    9
    Name: _c2, dtype: int64
    """
    max_df = tbl0.groupby(by="_c1").max()
    response = max_df["_c2"]
    return response 


def pregunta_06():
    """
    Retorne una lista con los valores unicos de la columna _c4 de del archivo `tbl1.csv`
    en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """
    account = tbl1["_c4"].value_counts()
    indexes_list = list(account.index)
    response = []
    for element in indexes_list:
        response.append(element.upper())
    response = sorted(response)
    return response


def pregunta_07():
    """
    Calcule la suma de la _c2 por cada letra de la _c1 del archivo `tbl0.tsv`.

    Rta/
    _c1
    A    37
    B    36
    C    27
    D    23
    E    67
    Name: _c2, dtype: int64
    """
    max_df = tbl0.groupby(by="_c1").sum()
    response = max_df["_c2"]
    return response 


def pregunta_08():
    """
    Agregue una columna llamada `suma` con la suma de _c0 y _c2 al archivo `tbl0.tsv`.

    Rta/
        _c0 _c1  _c2         _c3  suma
    0     0   E    1  1999-02-28     1
    1     1   A    2  1999-10-28     3
    2     2   B    5  1998-05-02     7
    ...
    37   37   C    9  1997-07-22    46
    38   38   E    1  1999-09-28    39
    39   39   E    5  1998-01-26    44

    """
    tbl0["suma"] = tbl0[["_c0","_c2"]].sum(axis=1)
    return tbl0


def pregunta_09():
    """
    Agregue el año como una columna al archivo `tbl0.tsv`.

    Rta/
        _c0 _c1  _c2         _c3  year
    0     0   E    1  1999-02-28  1999
    1     1   A    2  1999-10-28  1999
    2     2   B    5  1998-05-02  1998
    ...
    37   37   C    9  1997-07-22  1997
    38   38   E    1  1999-09-28  1999
    39   39   E    5  1998-01-26  1998

    """
    tbl0["year"] = tbl0["_c3"].str.slice(stop=4)
    return tbl0


def pregunta_10():
    """
    Construya una tabla que contenga _c1 y una lista separada por ':' de los valores de
    la columna _c2 para el archivo `tbl0.tsv`.

    Rta/
                                   _c1
      _c0
    0   A              1:1:2:3:6:7:8:9
    1   B                1:3:4:5:6:8:9
    2   C                    0:5:6:7:9
    3   D                  1:2:3:5:5:7
    4   E  1:1:2:3:3:4:5:5:5:6:7:8:8:9
    """
    column_c1 = []
    column_c2 = []
    for index, row in tbl0.iterrows():
        column_c1.append(row["_c1"])
        column_c2.append(row["_c2"])

    column_c1_ordered = list(set(column_c1))
    column_c1_ordered = sorted(column_c1_ordered)    
    join_c2_list = []
    for element in column_c1_ordered:
        value_list = []
        for sub_element_1, sub_element_2 in zip(column_c1, column_c2):
            if sub_element_1==element:
                value_list.append(str(sub_element_2))
                value_list.sort()      
        join_element = ":".join(value_list)
        join_c2_list.append(str(join_element))
    df_1 = pd.DataFrame()
    df_1["_c1"] = column_c1_ordered
    df_1["_c2"] = join_c2_list
    return df_1.set_index("_c1")


def pregunta_11():
    """
    Construya una tabla que contenga _c0 y una lista separada por ',' de los valores de
    la columna _c4 del archivo `tbl1.tsv`.

    Rta/
        _c0      _c4
    0     0    b,f,g
    1     1    a,c,f
    2     2  a,c,e,f
    3     3      a,b
    ...
    37   37  a,c,e,f
    38   38      d,e
    39   39    a,d,f
    """
    column_c0 = []
    column_c4 = []
    for index, row in tbl1.iterrows():
        column_c0.append(row["_c0"])
        column_c4.append(row["_c4"])
    column_c0_ordered = list(set(column_c0))
    column_c0_ordered = sorted(column_c0_ordered)    
    join_c4_list = [] 
    for element in column_c0_ordered:
        value_list = []
        for sub_element_1, sub_element_2 in zip(column_c0, column_c4):
            if sub_element_1==element:
                value_list.append(str(sub_element_2))
                value_list.sort()      
        join_element = ",".join(value_list)
        join_c4_list.append(join_element)
    df_1 = pd.DataFrame()
    df_1["_c0"] = column_c0_ordered
    df_1["_c4"] = join_c4_list        
    return df_1


def pregunta_12():
    """
    Construya una tabla que contenga _c0 y una lista separada por ',' de los valores de
    la columna _c5a y _c5b (unidos por ':') de la tabla `tbl2.tsv`.

    Rta/
        _c0                                  _c5
    0     0        bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
    1     1              aaa:3,ccc:2,ddd:0,hhh:9
    2     2              ccc:6,ddd:2,ggg:5,jjj:1
    ...
    37   37                    eee:0,fff:2,hhh:6
    38   38                    eee:0,fff:9,iii:2
    39   39                    ggg:3,hhh:8,jjj:5
    """
    column_c0 = []
    column_c5a = []
    column_c5b = []
    for index, row in tbl2.iterrows():
        column_c0.append(row["_c0"])
        column_c5a.append(row["_c5a"])
        column_c5b.append(row["_c5b"])
    column_c0_ordered = list(set(column_c0))
    column_c0_ordered = sorted(column_c0_ordered)    
    join_c5a_c5b_list = [] 
    for element in column_c0_ordered:
        value_list = []
        for sub_element_1, sub_element_2, sub_element_3 in zip(column_c0, column_c5a, column_c5b):
            if sub_element_1==element:
                join_value = str(sub_element_2) + ":" + str(sub_element_3)
                value_list.append(str(join_value))
                value_list.sort()      
        join_element = ",".join(value_list)
        join_c5a_c5b_list.append(join_element)
    df_1 = pd.DataFrame()
    df_1["_c0"] = column_c0_ordered
    df_1["_c5"] = join_c5a_c5b_list        
    return df_1


def pregunta_13():
    """
    Si la columna _c0 es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`, compute la
    suma de tbl2._c5b por cada valor en tbl0._c1.

    Rta/
    _c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: _c5b, dtype: int64
    """
    series_tbl0 = tbl0.groupby("_c0")._c1.sum()
    series_tbl2 = tbl2.groupby("_c0")._c5b.sum()

    df_1 = pd.DataFrame()
    df_1 = series_tbl0


    df_2 = pd.DataFrame()
    df_2 = series_tbl2

    df_concat = pd.merge(df_1,df_2,on="_c0")

    series_concat = df_concat.groupby("_c1")._c5b.sum()
  
    return series_concat
