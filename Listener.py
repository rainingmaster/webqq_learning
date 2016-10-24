from Queue import Queue
import httplib2, json, urllib, threading, time

class Listner(threading.Thread):
    def __init__(self, c_name, queue, setting):
        threading.Thread.__init__(self, name = c_name)
        self.data = queue
        self.psessionid = setting.psessionid
        self.headers = setting.headers
        self.url = "https://d1.web2.qq.com/channel/poll2"
    def poll_msg():
        args = {
            "ptwebqq" : "ff57cb0c1a3de2c4822fb0af2c3f50f0fc82fc50aaeb6fcb7ddf19831ebf137b",
            "clientid": 53999199,
            "psessionid" : self.psessionid,
            "key":""
        }
        args = urllib.parse.quote(json.dumps(args))
        body = 'r=' + args
        h = httplib2.Http(".cache")
        (resp, content) = h.request(self.url, "POST", body = body, headers = self.headers)
        content = json.loads(bytes.decode(content))
        if content["retcode"] == 0:
            return content["result"]["value"]["content"][0][1]
        else:
            return false
    def run(self):
        while 1:
            try:
                str = poll_msg()
                if str:
                    self.data.put(str)
                time.sleep(2)
            except:
                print "%s: %s finished!" % (time.ctime(), self.getName())
            break