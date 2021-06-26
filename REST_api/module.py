import psycopg2

conn = None

def RecordTodict(records):
    dummy_list = []
    key_list = ['ifsc','bank_id','branch','address','city','district','state','bank_name','favourites']

    for i in range(len(records)):
            index = 0
            bank_dict = {}
            for j in records[i]:
                print(j)
                bank_dict[key_list[index]] = j
                index = index + 1
            dummy_list.append(bank_dict)
    return dummy_list
def getConnection():
    try:
        global conn
        conn = psycopg2.connect(" dbname ='bdiwtqgl1vkip8zcuux5' user='u66vht9deo5ggcgnjz73'  host='bdiwtqgl1vkip8zcuux5-postgresql.services.clever-cloud.com' password='gS7mhQjhtu0MM2yAn0w7'")
        
        cur = conn.cursor()
        return {'status':200,'data':cur}
    except Exception as e:
        return {'status':500,'data':str(e)} 
def getRecord(cur,code):
    
    cur.execute(code)
    records = cur.fetchall()
    return RecordTodict(records)

def closeConn():
    global conn
    conn.close()
    return 200


def setFav(ifsc,cur):
    print("got in")
    try:
        res = cur.execute("select favourites from bank where bank.ifsc = '{}' ".format(ifsc))
        res = cur.fetchall()
        res = res[0]
    
        if  not(res[0]):
            print("if")
            cur.execute("UPDATE bank SET favourites = true WHERE ifsc = '{}'".format(ifsc))
            conn.commit()
        else:
            cur.execute("UPDATE bank SET favourites = false WHERE ifsc = '{}'".format(ifsc))
            conn.commit()
        return "DOne"



    except Exception as e:
        return {'status':500,'data':str(e)}
    