from multiprocessing import Queue
from webqq_listener import Listener
from webqq_speaker import Speaker
import httplib2
import json
import urllib

#Main thread
def main():
    cookies = 'pt2gguin=o0312841925; ptcz=bcef226e6f39d4ec01852f1c2723c69411648c3d858b8e4ab871548fade8bfd8; pgv_pvid=7429962020; o_cookie=312841925; pac_uid=1_312841925; _gscu_661903259=66058774n4si8j18; tvfe_boss_uuid=4bc70f02a1708e3c; _ga=GA1.2.2101278655.1467976938; h_uid=H1906082591e; ts_refer=www.baidu.com/link; ts_uid=2493411700; pgv_pvi=1368670208; RK=EWGanm3nG1; p_uin=o0312841925; p_skey=zVZnBKckgGWoBnnmTSCPaEjQl5NEBBUAsoHa*MUv7QU_; pt4_token=kIt3EhgN25xKMNLWD2tRsOwCpY472XmkbUcxAKu2FLw_; uin=o0312841925; ptisp=ctc; pgv_info=ssid=s5760458008; qz_gdt=h4grawahbqacn3sdrliq; skey=@ZTwdToW5R; ptwebqq=6ff92ebfb9478a7e06fd3dcb01062c6ad1c9117920684e5bb5e5aff6893a1629; pgv_si=s2391059456; verifysession=h0103c5ca5ae9a1d3c5be40ac105b01b0b55fdcbfecbba50769c97c6245d7d88f26e6d2b2bbc5b73120015f15928aa45e19; _gscbrs_661903259=1; ts_last=web2.qq.com/'
    psessionid = '8368046764001d636f6e6e7365727665725f77656271714031302e3133332e34312e383400001ad00000066b026e040015808a206d0000000a406172314338344a69526d0000002859185d94e66218548d1ecb1a12513c86126b3afb97a3c2955b1070324790733ddb059ab166de6857'
    ptwebqq = "6ff92ebfb9478a7e06fd3dcb01062c6ad1c9117920684e5bb5e5aff6893a1629"
    headers = {
        'Host' : 'd1.web2.qq.com',
        'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language' : 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding' : 'deflate',
        'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8',
        'Referer' : 'https://d1.web2.qq.com/cfproxy.html?v=20151105001&callback=1',
        'Cookie' : cookies,
        'Connection' : 'keep-alive',
        'Pragma' : 'no-cache',
        'Cache-Control' : 'no-cache',
    }
    setting = {
        "psessionid" : psessionid,
        "headers" : headers,
        "ptwebqq" : ptwebqq
    }
    sendinfo = {
        "msg_id" : 66960001,
        "user" : 1394305870
    }

    queue = Queue()
    speaker = Speaker('Spk.', queue, setting, sendinfo)
    listener = Listener('Lst.', queue, setting)
    speaker.start()
    listener.start()
    speaker.join()
    listener.join()
    print('All threads terminate!')
 
if __name__ == '__main__':
   main()
#send_msg(3333748746, "1奉还正茂")
#poll_msg()