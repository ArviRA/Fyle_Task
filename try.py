import psycopg2



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
        conn = psycopg2.connect(" dbname ='bdiwtqgl1vkip8zcuux5' user='u66vht9deo5ggcgnjz73'  host='bdiwtqgl1vkip8zcuux5-postgresql.services.clever-cloud.com' password='gS7mhQjhtu0MM2yAn0w7'")
        return conn
    except Exception as e:
        print (e)
def getRecord(conn):
    cur = conn.cursor()
    cur.execute("SELECT * from bank limit 5")
    records = cur.fetchall()
    conn.close()
    return RecordTodict(records)
