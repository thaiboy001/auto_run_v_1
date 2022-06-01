import os, json, time
from progress.spinner import MoonSpinner

# setting function
def set_miner():
    pool = None
    wallet = None
    password = None
    cpu = None
    try:
        print("ตัวอย่าง: \033[93mstratum+tcp://ap.luckpool.net:3956\033[00m")
        pool = input("Pool[-o]: ")

        print("ตัวอย่าง: \033[93mRQpWNdNZ4LQ5yHUM3VAVuhUmMMiMuGLUhT.OMG-MINER\033[00m")
        wallet = input("Wallet[-u]: ")

        print("ตัวอย่าง: \033[93mx หรือ ( hybrid เฉพาะ luckpool )\033[00m")
        password = input("Password[-p]: ")

        print("\033[93m 0 ขึ้นไป หรือ เท่ากับจำนวณเธรด CPU เช็ค 'lscpu'\033[00m")
        cpu = int(input("CPU[-t]: "))
        
        if pool == "" or wallet == "":
            raise Exception()
        if password == "":
            password = "x"
        if cpu == "":
            cpu = 1
    except:
        print("\nเกิดข้อผิดพลาด มีบางอย่างไม่ถุูกต้อง!")
        time.sleep(2)
        set_miner()
    puts = {
        'Pool': pool,
        'Wallet': wallet,
        'Pass': password,
        'Cpu': cpu
    }
    with open("set-miner/miner.json", "w") as set:
        json.dump(puts, set, indent=4)

# check path & main process
os.system("clear")
with MoonSpinner("กําลังเปิดตัวเปลี่ยนพูลและกระเป๋า...") as bar:
        for i in range(100):
            time.sleep(0.05)
             bar.next()
          bar.finish()
if os.path.exists("set-miner") == True:
    set_miner()
else:
    os.system("mkdir set-miner")
    
