from Queue import Queue
import httplib2, json, urllib, threading, time

class Speaker(threading.Thread):
    def __init__(self, c_name, queue, setting):
        threading.Thread.__init__(self, name = c_name)
        self.data = queue
        self.psessionid = setting.psessionid
        self.headers = setting.headers
        self.url = "https://d1.web2.qq.com/channel/send_buddy_msg2"
    def send_msg(user, msg):
        args = {
            "to" : user,
            "content" : '[\"' + msg + '\",[\"font\",{\"name\":\"宋体\",\"size\":10,\"style\":[0,0,0],\"color\":\"000000\"}]]"',
            "face" : 0,
            "clientid" : 53999199,
            "msg_id" : 18460002,
            "psessionid" : self.psessionid
        }
        args = urllib.parse.quote(json.dumps(args))
        body = 'r=' + args
        h = httplib2.Http(".cache")
        (resp, content) = h.request(url, "POST", body = body, headers = self.headers)
        print("content is:", content)
    def run(self):
        while 1:
            try:
                str = self.data.get(1, 5)
                send_msg(3333748746, "你说：" + str + "？不是吧？")
                time.sleep(2)
            except:
                print "%s: %s finished!" % (time.ctime(), self.getName())
            break