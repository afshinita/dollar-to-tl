import ssl, time
from datetime import datetime
#import urllib.request, urllib.error
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

#ctx = ssl.create_default_context()
#ctx.check_hostname = False
#ctx.verify_mode = ssl.CERT_NONE

my_list=list(); dollar_list=list(); euro_list=list(); str1=list(); str2=list()

class My_Data:
    def my_show_data(self,dt):
        count = 0; x = None
        for i in dt:
            if x == None:
                x = i.strip()
            elif (count % 2 == 0):
                str2.append(i.strip())
            else: str1.append(i.strip())
            count += 1
        print('last seen: ', x, '\n1 Dollar: ', str1[0], '\t\t', str2[0], '\n1 Euro: ', str1[1],
              '\t\t', str2[1], '\n1 Bitcoin: ', str1[2], '\t\t', str2[2])

    def my_save_data(self,dollar,dollar_pe,euro,euro_pe,bitcoin,bitcoin_pe):
        self.outfile = open('my_data_dollar.txt','w+')
        for i in (self.save_time,'\n',dollar,"\n",dollar_pe,'\n',euro,'\n',euro_pe,"\n",
                  bitcoin,"\n",bitcoin_pe):
            my_list.append(i)

        for line in my_list:
            self.outfile.write(str(line))
        self.outfile.close()

    def my_save_time(self, savetime = 'First_time'):
        global save_time
        self.save_time = savetime
#------------ read and write csv files -----------------
    def my_csv_save(self, df):
        df.to_csv('my_dollar_csv.csv')
    def my_csv_show(self, df):
        print(df.head(10))
    def __init__(self):
        print('\n\t\t\t\tWellcome Afshin\n')
def main():
    myObj = My_Data()
    try:
        infile_data = open('my_data_dollar.txt',"r")
        myObj.my_show_data(infile_data)
    except:
        print("can't find any file.txt")
        input("?")
    # --------------------------------------------------------
    while True:
        try:
            #my_data = urllib.request.urlopen('https://dolar.tlkur.com/',context=ctx)
            my_data = requests.get('https://dolar.tlkur.com/')
            data = BeautifulSoup(my_data.text,'html.parser')
            bf = data.find('div')('span')
            Lis = list()
            for line in bf:
                xl = line.text
                Lis.append(xl)
            dollar = Lis[3]; euro = Lis[9]; bitcoin = Lis[15]
            dollar_pe = Lis[4]; euro_pe = Lis[10]; bitcoin_pe = Lis[16]
        except:
            print('internet is not Available')
            input("?")
        try:
            in_txt_data = open("my_data_dollar.txt","r")
        except:
            print("can't find file.txt")
            input("?")
        try:
            save_my_time = datetime.today()
            save_mytime2 = str(save_my_time.time())
            save_my_final = save_mytime2[:5]
            dollar_series = pd.Series({0:save_my_time.date(),1:save_my_final,2:dollar,
                                       3:dollar_pe,4:euro,5:euro_pe,6:bitcoin,7:bitcoin_pe})
            df = pd.DataFrame([dollar_series])
            df.rename(columns={0:"Data",1:"Time",2:"Dollar",3:"%D",4:"Euro",
                               5:"%E",6:"Bitcoin",7:"%B"},inplace=True)
        except:
            print("Error for csv in while...")
            input("?")
        try:
            print()
            print('Today ',datetime.today())
            print('1 Dollar: {} t\t\t{}\n1 Euro: {} t\t\t{}\n1 Bitcoin {} t\t\t{}\n'.
                  format(dollar,dollar_pe,euro,euro_pe,bitcoin,bitcoin_pe))
            df.set_index('Data',append=False,inplace=True,verify_integrity=False)
        except:
            print('Please try again')
            input("?")
        try:
            infile_csv = pd.read_csv('my_dollar_csv.csv')
            _df = pd.DataFrame(infile_csv)
            _df.set_index('Data',inplace=True)
            data = df.append(_df)
            myObj.my_csv_show(data)
        except:
            myObj.my_csv_save(df)
            print('first time you seen')
            input("?")
    #     try:
    #         data.reset_index(inplace=True)
    #         data['Data'].sort_index(ascending=False,inplace=True,sort_remaining=False)
    #         _df['Dollar'].sort_index(ascending=False,inplace=True,sort_remaining=False)
    #         _df['Euro'].sort_index(ascending=False,inplace=True,sort_remaining=False)
    #
    #         d = list(data['Data'])
    #         t = list(data['Time'])
    #         dol = list(_df['Dollar'])
    #         eur = list(_df['Euro'])
    #         l = np.arange(len(d))
    #         my_d = d[-36:]
    # #-----------------------------------Dollar---------------------------------------
    #         do = list(df['Dollar'])
    #         for i in do:
    #             dd = float(i)
    #         dol.insert(0,dd)
    #         my_dol = dol[-36:]
    #         my_dol.reverse()
    #
    #         my_l = l[-36:]
    #
    # #-----------------------------------Euro---------------------------------------
    #         eu = list(df['Euro'])
    #         for i in eu:
    #             ee = float(i)
    #         eur.insert(0,ee)
    #         my_eur = eur[-36:]
    #         my_eur.reverse()
    #
    #         data['Data'].sort_index(ascending=True,inplace=True,sort_remaining=False)
    #         _df['Dollar'].sort_index(ascending=True,inplace=True,sort_remaining=False)
    #         _df['Euro'].sort_index(ascending=True,inplace=True,sort_remaining=False)
    #         data.set_index(['Data'],inplace=True)
    #     except:
    #         print('error matplot...')
        try:
            e =input('\nWrite e to exit or press enter to refresh:')
            if e == 'e': break 
            else:
                c = 3
                for i in range(3):
                    print('\t\t\tRefresh for {} seconds...'.format(c))
                    time.sleep(1)
                    c -= 1
        except:
            print("Error input your type!")
            input("?")
    try:
        savetime = datetime.today()
        myObj.my_save_time(savetime)
        myObj.my_save_data(dollar,dollar_pe,euro,euro_pe,bitcoin,bitcoin_pe)
    except:
        print("Error time")
        input()
    try:
        time_in = open('my_time.txt','r')
        my_time_old = time_in.read()[:2]
        data_save_csv = data[:35]
    except:
        print("can't open the file.txt")
        input("?")
    try:
        my_time_now = savetime.time()
        time_now = str(my_time_now)
        my_time_final = time_now[:2]
        my_df = _df.reset_index()
        myd = list(my_df["Data"])
        my_d = myd[0]
        my_dd = str(my_d).split("-")
        my_old_final = my_dd[1] + my_dd[2]
        mydf = df.reset_index()
        myd2 = list(mydf["Data"])
        my_d2 = myd2[0]
        my_dd2 = str(my_d2).split("-")
        my_now_final = my_dd2[1] + my_dd2[2]
        if (my_time_final > my_time_old) or (my_now_final > my_old_final):
            try:
                myObj.my_csv_save(data_save_csv)
                time_out = open('my_time.txt','w')
                time_out.write(str(savetime.time()))
                time_out.close()
                print('time and data saved...')
            except:
                myObj.my_csv_save(df)
                input("?")
    except:
        print('error write and read csv....')
        input("?")
    print("--------------------")
    infile_data.close()
    in_txt_data.close()
    time_in.close()
    print('\t\t\t\tThankYou Afshin')
    time.sleep(2)
if __name__ == "__main__": main()
