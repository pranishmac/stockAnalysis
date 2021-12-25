from nsepython import *   
import time,sys

while True:              ### running infinte loop at interval of 5 second "time.sleep(5)" at last
    curr_time = time.localtime()  ## getting current time
    curr_clock = time.strftime("%H%M%S", curr_time)  ## current time in format HHMMSS
        # print(curr_clock)


    breakout_low=0
    breakout_high=0
    day_high=0
    day_low=sys.maxsize       ## this is maximum int value 
    sell=False
    buy=False


    curr_price=nse_fno("BANKNIFTY")['underlyingValue']  ##current price of bank nifty stock


    if (int(curr_clock)>91500) and (int(curr_clock)<93000): ## betweem 9:15am and 9:30am determining breakout range
        if curr_price>breakout_high:
            breakout_high=curr_price
        if curr_price<breakout_low:
            breakout_low=curr_price

## code to buy or sell(1st time)
    if (int(curr_clock)>93000) and (int(curr_clock)<153000):
        if (curr_price>breakout_high) and (sell==False):
            buy=True
            buy_price=curr_price
    
    if (curr_price<breakout_low) and (buy==False):
        sell=True
        sell_price=curr_price


## code to reverse the transaction after hitting 0.5% stop loss
    if (buy==True) and (((buy_price-curr_price)/buy_price)==0.5) and curr_clock<151500:
        print("Stock sold at loss of: "+buy_price-curr_price)
        sys.exit("Program Terminated due to Stop Loss")    

    if (sell==True) and (((curr_price-sell_price)/sell_price)==0.5) and curr_clock<151500:
        print("Stock bought at loss of: "+curr_price-sell_price)
        sys.exit("Program Terminated due to Stop Loss")    


##code to square off the position if stop loss is not hit till 3:15pm
    if(curr_time>151500):
        if buy==True:
            print("Stock sold at profit of: "+curr_price-buy_price)
            sys.exit()
        if sell==True:
            print("Stock bought at profit of: "+sell_price-curr_time)
            sys.exit()  #program terminates after executing sys.exit()
    time.sleep(5)     ## loop re-run every 5 seconds







