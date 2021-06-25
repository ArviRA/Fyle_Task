import psycopg2

conn = None

def RecordTodict(records):
    dummy_list = []
    key_list = ['ifsc','bank_id','branch','address','city','district','state','bank_name']

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
        return {'status':500,'data':e} 
def getRecord(cur,code):
    
    cur.execute(code)
    records = cur.fetchall()
    return RecordTodict(records)

def closeConn():
    global conn
    conn.close()
    return 200
