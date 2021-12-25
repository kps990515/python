import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from crawl import updateLp
import time
import schedule

if __name__ == '__main__':
    chat_id = '-776768050'
    token = '5013330145:AAE0WDeo1k0AbCuHO56AgMTk-Aryqi2JGf0'
    bot = telegram.Bot(token=token)

    def crawlLp():
        updateLpList = updateLp()
        updateLpNum = len(updateLpList)
        
        bot.sendMessage(chat_id=chat_id, text= "작동중") 
        
        if updateLpNum > 0 :
            for lp in updateLpList:
                bot.sendMessage(chat_id=chat_id, text= str(lp) + " 추가됨") 
                
    schedule.every(5).seconds.do(crawlLp)

    while True:
        schedule.run_pending()
        time.sleep(1)
    