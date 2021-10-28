import speedtest
import time
import datetime


start_process_time = time.time()                      # ---------------------- Time of Transactions
moment = datetime.datetime.now()
date = datetime.datetime.strftime(moment, '%c')       # ---------------------- Showing Date



def speedtest_():

    st = speedtest.Speedtest()

    for i in range(3):

        print("Getting best server..." )
        time.sleep(0.3)

    st.get_servers()    # ---------------------- List of Servers
    best_server = st.get_best_server()       # ---------- to get best server
    print("\n" + f" ------------- Server Information: {best_server['host']} located in {best_server['country']} -------------" + "\n") # ----------------------  Best Server Informations



    # Download Speed Test

    for i in range(3):

        print("Measuring download speed...")
        time.sleep(0.3)

    print( "\n" + f" ------------- Download Test: {st.download() / 1024 / 1024:.2f} Mbit/s -------------" + "\n")   # ---------------------- st.download() method measures download speed of internet



    # Upload Speed Test

    for i in range(3):

        print("Measuring upload speed...")
        time.sleep(0.3)

    print("\n" + f" ------------- Upload Test: {st.upload() / 1024 / 1024:.2f} Mbit/s -------------")  # ---------------------- st.upload() method measures upload speed of internet



    # Ping Test

    print("\n" + f" ------------- Ping Test: {st.results.ping} ms -------------")   # ---------------------- st.results.ping() method measures ping value


    end_process_time = time.time()
    print( "\n" + f"""
    Completion time of transactions: {end_process_time -start_process_time} sec
                                                                                  {date}""")



speedtest_()


