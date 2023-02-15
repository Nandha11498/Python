# import required packages

import pandas as pd
from datetime import datetime
import time
from winotify import Notification
import schedule

from plyer import notification
import pyttsx3


def Birthday():
    bdaylist = []
    today = datetime.now().strftime('%d-%m')
    # print(today)

    df = pd.read_excel(r"C:\Users\emedhub\Desktop\birthday_excel.xlsx")

    for i in range(len(df)):

        dt = datetime.strftime(df.loc[i,"Birthday"], "%d-%m")

        if today == dt : 
            # print(dt)
            Name = df.loc[i,'Name']
            # print(Name)
            bdaylist.append(Name)
            

    toast = Notification(app_id = "BIRTHDAY REMAINDER",
        title = "Birthday Wishes 🥳🥳🥳",
        msg = "Happy Birthday {}".format(bdaylist),
        icon = r"C:\Users\emedhub\Desktop\icon_bday.jpg",
        duration= "long",
    )

    toast.show()


Birthday()


# schedule.every().day.at("10:00").do(Birthday)

schedule.every().monday.at("10:00").do(Birthday)
schedule.every().tuesday.at("18:44").do(Birthday)
schedule.every().wednesday.at("10:00").do(Birthday)
schedule.every().thursday.at("10:00").do(Birthday)
schedule.every().friday.at("10:00").do(Birthday)
schedule.every().saturday.at("10:00").do(Birthday)

while True:
    schedule.run_pending()
    time.sleep(1)





# toast = Notification(app_id = "BIRTHDAY WISHES",
#         title = "Birthday Wishes 🥳🥳🥳",
#         msg = "Happy Birthday to you!",
#         icon = r"C:\Users\emedhub\Desktop\icon_bday.jpg",
#         duration= "long",
#         launch= " asdfghgfdsa"
#     )

# toast.show()