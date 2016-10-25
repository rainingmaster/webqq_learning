from multiprocessing import Queue
import httplib2, json, urllib, threading, time

class Listener(threading.Thread):
    def __init__(self, c_name, queue, setting):
        threading.Thread.__init__(self, name = c_name)
        self.data = queue
        self.psessionid = setting["psessionid"]
        self.headers = setting["headers"]
        self.ptwebqq = setting["ptwebqq"]
        self.url = "https://d1.web2.qq.com/channel/poll2"
    def poll_msg(self):
        args = {
            "ptwebqq" : self.ptwebqq,
            "clientid": 53999199,
            "psessionid" : self.psessionid,
            "key":""
        }
        args = urllib.parse.quote(json.dumps(args))
        body = 'r=' + args
        h = httplib2.Http(".cache")
        (resp, content) = h.request(self.url, "POST", body = body, headers = self.headers)

        if int(resp["status"]) != 200:
            print("return status is " + resp["status"])
            return False
            
        content = json.loads(bytes.decode(content))
        if int(content["retcode"]) == 0:
            return content["result"][0]["value"]["content"][1]
        else:
            print("return retcode is " + str(content["retcode"]))
            return False
    def run(self):
        while 1:
            print("begin poll")
            str = self.poll_msg()
            if str:
                print("push it:" + str)
                self.data.put(str)