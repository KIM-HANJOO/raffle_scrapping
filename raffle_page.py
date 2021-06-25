import schedule
import time
import webbrowser

def job():
    
    url2= "https://store.musinsa.com/app/raffle/lists?raffle_state_gb=S"
    url1= "https://www.shoeprize.com/"
    url3= "https://www.luck-d.com/"

    webbrowser.open(url1) 
    webbrowser.open(url2)
    webbrowser.open(url3)

schedule.every().day.at("12:30").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)