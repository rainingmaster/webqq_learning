from multiprocessing import Queue
import httplib2, json, urllib, time

class Robot():
    def __init__(self):
        self.url = "http://www.tuling123.com/openapi/api"
    def ask(self, info):
        args = {
            "key" : "afc3b5fda95c466c8ca31dd6e17f87ee",
            "info": info,
            "userid" : 312841925
        }
        #args = urllib.parse.quote(json.dumps(args))
        body = json.dumps(args)
        h = httplib2.Http(".cache")
        (resp, content) = h.request(self.url, "POST", body = body)

        if int(resp["status"]) != 200:
            print("return status is " + resp["status"])
            return False
            
        content = json.loads(bytes.decode(content))
        if int(content["code"]) == 100000:
            return content["text"]
        else:
            print(content)
            return False