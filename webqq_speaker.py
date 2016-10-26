from multiprocessing import Queue
from webqq_rob import Robot
import httplib2, json, urllib, threading, time

class Speaker(threading.Thread):
    def __init__(self, c_name, queue, setting, sendinfo):
        threading.Thread.__init__(self, name = c_name)
        self.data = queue
        self.psessionid = setting["psessionid"]
        self.headers = setting["headers"]
        self.url = "https://d1.web2.qq.com/channel/send_buddy_msg2"

        self.user = sendinfo["user"]
        self.msg_id = sendinfo["msg_id"]
    def send_msg(self, user, msg):
        args = {
            "to" : user,
            "content" : '[\"' + msg + '\",[\"font\",{\"name\":\"宋体\",\"size\":10,\"style\":[0,0,0],\"color\":\"000000\"}]]"',
            "face" : 0,
            "clientid" : 53999199,
            "msg_id" : self.msg_id,
            "psessionid" : self.psessionid
        }
        self.msg_id += 1
        args = urllib.parse.quote(json.dumps(args))
        body = 'r=' + args
        h = httplib2.Http(".cache")
        (resp, content) = h.request(self.url, "POST", body = body, headers = self.headers)
        
        if int(resp["status"]) != 200:
            print("return status is " + resp["status"])
            return False

        content = json.loads(bytes.decode(content))
        if ("errCode" in content) and int(content["errCode"]) == 0:
            return True
        else:
            print(content)
            return False

    def run(self):
        while 1:
            robot = Robot()
            str = self.data.get()
            ctn = robot.ask(str)
            ret = False
            while ctn and (not ret):
                ret = self.send_msg(self.user, ctn)
                time.sleep(2)