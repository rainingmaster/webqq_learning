from Queue import Queue
import httplib2
import json
import urllib
import thread

psessionid = '8368046764001d636f6e6e7365727665725f77656271714031302e3133332e34312e383400001ad00000066b026e040015808a206d0000000a406172314338344a69526d0000002859185d94e66218548d1ecb1a12513c86126b3afb97a3c2955b1070324790733ddb059ab166de6857'
headers = {
    'Host' : 'd1.web2.qq.com',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language' : 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding' : 'deflate',
    'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8',
    'Referer' : 'https://d1.web2.qq.com/cfproxy.html?v=20151105001&callback=1',
    'Cookie' : 'pt2gguin=o0312841925; ptcz=bcef226e6f39d4ec01852f1c2723c69411648c3d858b8e4ab871548fade8bfd8; pgv_pvid=7429962020; o_cookie=312841925; pac_uid=1_312841925; _gscu_661903259=66058774n4si8j18; tvfe_boss_uuid=4bc70f02a1708e3c; _ga=GA1.2.2101278655.1467976938; h_uid=H1906082591e; ts_refer=www.baidu.com/link; ts_uid=2493411700; pgv_pvi=1368670208; ts_last=web2.qq.com/; RK=EWGanm3nG1; p_uin=o0312841925; p_skey=ayr8RfyxdIrYj-hoLvTrrTjj3siuDdb2m05NmG*5GcM_; pt4_token=bZvae1zp4oafXgaAaXlm7BLjHT4sXki0uAUnqk-oBwE_; uin=o0312841925; ptisp=ctc; pgv_info=ssid=s5760458008; qz_gdt=x5zqswbfaaab7sjpxfyq; skey=@QkNejiupj; ptwebqq=ff57cb0c1a3de2c4822fb0af2c3f50f0fc82fc50aaeb6fcb7ddf19831ebf137b; pgv_si=s2391059456',
    'Connection' : 'keep-alive',
    'Pragma' : 'no-cache',
    'Cache-Control' : 'no-cache',
}

def send_msg(user, msg):
    url = "https://d1.web2.qq.com/channel/send_buddy_msg2"
    global psessionid
    global headers
    args = {
        "to" : user,
        "content" : '[\"' + msg + '\",[\"font\",{\"name\":\"宋体\",\"size\":10,\"style\":[0,0,0],\"color\":\"000000\"}]]"',
        "face" : 0,
        "clientid" : 53999199,
        "msg_id" : 18460002,
        "psessionid" : psessionid
    }
    args = urllib.parse.quote(json.dumps(args))
    body = 'r=' + args
    print(args)
    h = httplib2.Http(".cache")
    (resp, content) = h.request(url, "POST", body = body, headers = headers)
    print("content is:", content)
    #content = json.loads(bytes.decode(content))
    #print("content is:", content["msg"])
    
def poll_msg():
    url = "https://d1.web2.qq.com/channel/poll2"
    global psessionid
    global headers

    args = {
        "ptwebqq" : "ff57cb0c1a3de2c4822fb0af2c3f50f0fc82fc50aaeb6fcb7ddf19831ebf137b",
        "clientid": 53999199,
        "psessionid" : psessionid,
        "key":""
    }
    args = urllib.parse.quote(json.dumps(args))
    body = 'r=' + args
    h = httplib2.Http(".cache")
    (resp, content) = h.request(url, "POST", body = body, headers = headers)
    print("content is:", content)
    #content = json.loads(bytes.decode(content))
    #print("content is:", content["msg"])

#Main thread
def main():
  queue = Queue()
  producer = Producer('Pro.', queue)
  consumer_even = Consumer_even('Con_even.', queue)
  consumer_odd = Consumer_odd('Con_odd.',queue)
  producer.start()
  consumer_even.start()
  consumer_odd.start()
  producer.join()
  consumer_even.join()
  consumer_odd.join()
  print 'All threads terminate!'
 
if __name__ == '__main__':
  main()
#send_msg(3333748746, "1奉还正茂")
#poll_msg()