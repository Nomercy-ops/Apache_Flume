# Apache_Flume
# Storing real time user stock data from alpha vantage API to HDFS using Apache Flume

* Step 1: get the api key by visiting the site https://www.alphavantage.co/support/#api-key

* Step 2:  go through the documentation of stock api and get the python code for Time Series Stock APIs

* Step 3: write the python code on a stock.py file and add the api key using the .env  file.

* Step 4: if all the steps are gone well the we can see the output of the stock data While running this program.

* Step 5: Now we have to to go inside our flume directory like in my case from terminal cd Apache/flume-1.9.0/conf and after that create a conf file i.e
* $ touch stock.conf  and add the flume configuration like source,channel and sink details there.

* Step 6: Now if the conf file is ready then we can execute the below command by going inside flume directory from terminal:
* $ Apache/flume-1.9.0
* Command : bin/flume-ng agent –conf ./conf/ -f conf/stock.conf -n agent1 -Dflume.root.logger=INFO

* Step 7: now we can see our output or file is successfully written by sink in our hdfs  as stock_data

* Video link for this task is : https://youtu.be/Ziu1ap6GLro



