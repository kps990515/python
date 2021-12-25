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

    #step2.Updater(유저의 입력을 계속 모니터링하는 역할), Dispatcher
    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher

    #step3./start 명령어가 입력되었을 때의 함수 정의
    def s(update, context):
        context.bot.send_message(chat_id=chat_id, text="작동중!")

    #step4.위에서 정의한 함수를 실행할 CommandHandler 정의
    start_handler = CommandHandler('s', s) #('명렁어',명령 함수)

    #step5.Dispatcher에 Handler를 추가
    dispatcher.add_handler(start_handler)

    #step6.Updater 실시간 입력 모니터링 시작(polling 개념)
    updater.start_polling()

    def crawlLp():
        updateLpList = updateLp()
        updateLpNum = len(updateLpList)
                
        if updateLpNum > 0 :
            for lp in updateLpList:
                bot.sendMessage(chat_id=chat_id, text= str(lp) + " 추가됨") 
                
    schedule.every(1).minutes.do(crawlLp)

    while True:
        schedule.run_pending()
        time.sleep(1)
    