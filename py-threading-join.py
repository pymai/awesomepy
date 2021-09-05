import threading
import requests


def http_head(url):
    resp = requests.head(url)
    # return url, resp.status_code
    print(threading.current_thread().getName(), url, resp.status_code)


def http_head_m(url, name):
    resp = requests.head(url)
    # return url, resp.status_code
    print(threading.current_thread().getName(), name, url, resp.status_code)


if __name__ == "__main__":
    # 1. 顺序请求 url 地址（单个参数）
    print("1. 顺序请求 url 地址（单个参数）")
    url_list = ["https://www.baidu.com", "https://www.qq.com", "https://www.163.com"]
    for x in url_list:
        print(http_head(x))

    # 2. 并发请求 url 地址（单个参数）
    print("2. 并发请求 url 地址（单个参数）")
    url_list = ["https://www.baidu.com", "https://www.qq.com", "https://www.163.com"]
    for x in url_list:
        # 2021.09.05 http_head 函数使用 return 时，怎么获取返回结果呢？
        # 2021.09.05 如何传入单个参数？--> args=(x,) 指定为元组可以传入单个参数
        thread = threading.Thread(target=http_head, args=(x,))
        thread.start()
        # thread.join([timeout]) 的功能是在程序指定位置，优先让该方法的调用者使用 CPU 资源
        # 如果不指定 timeout，则必须先执行完 thread 线程，程序才会继续往下执行
        thread.join()

    # 3. 并发请求 url 地址（多个参数）
    print("3. 并发请求 url 地址（多个参数）")
    url_name_dict = {"baidu": "https://www.baidu.com", "qq": "https://www.qq.com", "netease": "https://www.163.com"}
    for key, value in url_name_dict.items():
        # 2021.09.05 http_head_m 函数使用 return 时，怎么获取返回结果呢？
        # 2021.09.05 如何传入多个参数？--> args=(value, key) 指定为元组时，可以传入多个参数
        thread = threading.Thread(target=http_head_m, args=(value, key))
        thread.start()
        # thread.join([timeout]) 的功能是在程序指定位置，优先让该方法的调用者使用 CPU 资源
        # 如果不指定 timeout，则必须先执行完 thread 线程，程序才会继续往下执行
        thread.join()

# 输出的结果示例：
"""
1. 顺序请求 url 地址（单个参数）
MainThread https://www.baidu.com 200
None
MainThread https://www.qq.com 200
None
MainThread https://www.163.com 200
None
2. 并发请求 url 地址（单个参数）
Thread-1 https://www.baidu.com 200
Thread-2 https://www.qq.com 200
Thread-3 https://www.163.com 200
3. 并发请求 url 地址（多个参数）
Thread-4 baidu https://www.baidu.com 200
Thread-5 qq https://www.qq.com 200
Thread-6 netease https://www.163.com 200
"""
