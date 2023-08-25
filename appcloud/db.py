import ibm_db
from flask import *

conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=ea286ace-86c7-4d5b-8580-3fbfa46b1c66.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;security=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=bkj98440;PWD=16uDoxylBc9G3a6F",'','')
print(conn)


app = Flask(__name__)