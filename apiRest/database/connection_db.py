import psycopg2
def frequencyFile(file_name,word):

    conn = psycopg2.connect(database="prueba_meli", user="root", password="root")
    cursor1=conn.cursor()
    consulta ="select frequency from frequency_word INNER JOIN payment ON archivo.id = frequency_word.id_file WHERE where frequency_word.word = %s and archivo.name_file = %s"
    cursor1.execute(consulta, (word, file_name))
    result = 0
    for fila in cursor1:
        result = fila + result
        print(fila)
    return fila
            
def frequencyWord(word):

    conn = psycopg2.connect(database="prueba_meli", user="root", password="root")
    cursor1=conn.cursor()
    consulta ="select frequency from frequency_word where word = %s"
    cursor1.execute(consulta, (word))
    result = cursor1
    conn.close()
    return result
    