import TGCHandler
import csv
import random
import time
#from sound import Sound
# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import db

fieldnames = ["itr", "att1", "med1", "att2", "med2"]

with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

try:

    # CONNECTING THINKGEAR
    handler = TGCHandler.TGCHandler(host='127.0.0.1')
    handler.connect()
    handler.configure()
    handler.startMeasuring()

    # FIREBASE
    #cred = credentials.Certificate("pythontest.json")
    # firebase_admin.initialize_app(
    # cred, {'databaseURL': 'https://eggtest-74078-default-rtdb.firebaseio.com/'})

    i = 0
    stat = 'none'
    connect = 'online'
    while True:
        plevel = handler.get('poorSignalLevel')
        raw = handler.get('rawEeg')
        att = handler.get('attention')
        med = handler.get('meditation')
        delt = handler.get('delta')
        the = handler.get('theta')
        la = handler.get('lowAlpha')
        ha = handler.get('highAlpha')
        lb = handler.get('lowBeta')
        hb = handler.get('highBeta')
        lg = handler.get('lowGamma')
        hg = handler.get('highGamma')
        bl = handler.get('blinkStrength')
        if att != None and plevel != None and bl != None:
            print("Serial No:" + str(i) + " Raw-EEG:" + str(raw) + " Att:" +
                  str(att) + " Sig:" + str(plevel) + " Med:" + str(med) + " Bli:" + str(bl))
            # ref = db.reference('/')
            # ref.set({'EEG': {
            #     'serialno': i,
            #     'signallevel': plevel,
            #     'raweeg': raw,
            #     'attention': att,
            #     'meditation': med,
            #     'delta': delt,
            #     'theta': the,
            #     'lowalpha': la,
            #     'highalpha': ha,
            #     'lowbeta': lb,
            #     'highbeta': hb,
            #     'lowgamma': lg,
            #     'highgamma': hg,
            #     'blinkstrength': bl,
            #     'executedaction': stat,
            #     'connection': connect,
            # }})
            i += 1
            # if att > 70:
            #     # Sound.volume_up()
            #     print('volume up')
            #     stat = 'Volume Up'
            # if med > 60 and att < 70:
            #     # Sound.volume_down()
            #     print('volume down')
            #     stat = 'Volume Down'
            # if bl > 140:
            #     # Sound.mute()
            #     print('volume mute')
            #     stat = 'Volume Mute'

            with open('data.csv', 'a') as csv_file:
                csv_writer = csv.DictWriter(
                    csv_file, fieldnames=fieldnames)

                info = {
                    "itr": i,
                    "att1": hb,
                    "med1": ha,
                    "att2": lb,
                    "med2": la,
                }

                csv_writer.writerow(info)
                print(i, hb, ha, lb, la)
            time.sleep(1)

except KeyboardInterrupt:
    print('exit exit')
    # ref = db.reference('/')
    # ref.set({'EEG': {'serialno': 0,
    #                  'signallevel': 0,
    #                  'raweeg': 0,
    #                  'attention': 0,
    #                  'meditation': 0,
    #                  'delta': 0,
    #                  'theta': 0,
    #                  'lowalpha': 0,
    #                  'highalpha': 0,
    #                  'lowbeta': 0,
    #                  'highbeta': 0,
    #                  'lowgamma': 0,
    #                  'highgamma': 0,
    #                  'blinkstrength': 0,
    #                  'executedaction': 'none',
    #                  'connection': 'offline', }})
