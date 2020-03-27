from urllib3 import encode_multipart_formdata
import requests

# host = "http://bond-dev.tongdun.cn:8089/api/data/temp"
def upload():
    host = 'http://10.57.211.26:8098/getdata/fetch/upload'
    header = {
        "content-type": "application/json"
    }
    filename = "C17_key2.csv"
    file_path = "/Users/zipee/Downloads/C17_key2.csv"
    data = {
        'file': (filename, open(file_path,'rb').read()),
        'indicatrix':'a,b,c'
    }

    # data['file']= (filename, open(file_path,'rb').read())
    encode_data = encode_multipart_formdata(data)
    data = encode_data[0]
    header['Content-Type'] = encode_data[1]
    r = requests.post(url=host, headers=header, data=data)
    print(r)
    print("返回值：" + r.text)

def status():
    host = 'http://10.57.211.26:8098/getdata/status'
    r = requests.get(host, {"task_id":"1585280229716000Y1829F34A6155001"})
    print(r)
    print("返回值：" + r.text)

def download():
    host = 'http://10.57.211.26:8098/getdata/download'
    r = requests.get(host, {"task_id":"1585280229716000Y1829F34A6155001"})
    print(r)
    print("返回值：" + r.text)

if __name__ == "__main__":
    upload()
    # status()
    # download()