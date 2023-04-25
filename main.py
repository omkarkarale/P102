import webbrowser
import csv
import datetime
 
while True:
    #set your time in data.csv in 24hr format with day about next class
    df = csv.reader(open('data.csv', 'r'))

    day = datetime.datetime.now().strftime('%A').lower()
    hour = datetime.datetime.now().hour
    mint = datetime.datetime.now().minute
    
    #if day and time is same as your class it will start your whitehat class
    for row in df:
        try:
            if day == row[0].lower():
                # print(day)
                if hour == int(row[1]):
                    # print(hour)
                    if mint == int(row[2]):
                        webbrowser.open('https://code.whitehatjr.com/joinClass')                        
                        exit()
                    else:
                        class_is_there = False
                        # print("No class")
                        continue
        except Exception:
            break

