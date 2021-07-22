import schedule
import time
import webbrowser

time_raffle = ["09:00", "19:00"]
time_mail = ["09:00", "12:30", "15:00"]

####################################################

def job1():
    
    # url2= "https://store.musinsa.com/app/raffle/lists?raffle_state_gb=S"
    url1= "https://www.shoeprize.com/"
    # url3= "https://www.luck-d.com/"

    webbrowser.open(url1) 
    # webbrowser.open(url2)
    # webbrowser.open(url3)

def job2():
    
    url2= "https://store.musinsa.com/app/raffle/lists?raffle_state_gb=S"
    # url1= "https://www.shoeprize.com/"
    # url3= "https://www.luck-d.com/"

    # webbrowser.open(url1) 
    webbrowser.open(url2)
    # webbrowser.open(url3)


def job3():
    
    # url2= "https://store.musinsa.com/app/raffle/lists?raffle_state_gb=S"
    # url1= "https://www.shoeprize.com/"
    url3= "https://www.luck-d.com/"

    # webbrowser.open(url1) 
    # webbrowser.open(url2)
    webbrowser.open(url3)


def mail():

    url_mail = "https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox"

    webbrowser.open(url_mail)


for times in time_mail:
    schedule.every().day.at(times).do(mail)

for times_2 in time_raffle:
    schedule.every().day.at(times_2).do(job1)
    schedule.every().day.at(times_2).do(job2)
    schedule.every().day.at(times_2).do(job3)


while True:
    schedule.run_pending()
    time.sleep(1)

    



#cd C:\Users\Stephen Kim\Documents\GitHub\raffle_scrapping
#pyinstaller --noconsole --onefile raffle_page.py



