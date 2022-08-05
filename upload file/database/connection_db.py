import psycopg2
from model.file import File
def read_file(newFile: File, path_file):

    print('path: ' + path_file)
    file = open(path_file, 'r',encoding="utf8")
    stringWords = file.read() 
    file.close()
    listword = stringWords.split()
    frecuenciaPalab = []
    for w in listword:
        frecuenciaPalab.append(listword.count(w))
    write_blob(newFile,path_file )
    idFile = read_id_file(newFile)
    write_word(frecuenciaPalab,listword, idFile)   

def write_blob(newFile:File, path_file):
    
    conn = None
    try:
        drawing = open(path_file, 'rb').read()
        conn = psycopg2.connect(database="prueba_meli", user="root", password="root")
        cur = conn.cursor()
        cur.execute("INSERT INTO archivo(data_file,name_file,extension_file) " +
                    "VALUES(%s,%s,%s)",
                    (psycopg2.Binary(drawing), newFile.getNameFile(), newFile.getExtentionFile()))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            
def write_word(frecuenciaPalab,listword,idFile):
    
    conn = None
    try:
        conn = psycopg2.connect(database="prueba_meli", user="root", password="root")
        for u in range(0,len(listword)):
            cur = conn.cursor()
            cur.execute("INSERT INTO frequency_word(id_file,word,frequency) " +
                        "VALUES(%s,%s,%s)",
                        (idFile, listword[u], frecuenciaPalab[u]))
            conn.commit()
            cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def read_id_file(newFile:File):
    conn = psycopg2.connect(database="prueba_meli", user="root", password="root")
    cursor1=conn.cursor()
    consulta ="select id from archivo where name_file = %s and extension_file = %s limit 1;"
    cursor1.execute(consulta, (newFile.getNameFile(), newFile.getExtentionFile()))
    result = cursor1
    for fila in cursor1:
        result = fila
    conn.close()
    return result