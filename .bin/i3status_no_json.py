#!/usr/bin/python3

import time
import subprocess
import psutil

class mystatus:
    def __init__(self, i3_enable=False, i3_config="~/.config/i3status/i3status.conf"):
        self.modules = []
        self.i3 = False
        if i3_enable:
            process = subprocess.Popen(['i3status', '-c',  i3_config], stdout=subprocess.PIPE,  stderr=subprocess.PIPE, text=True)
            self.i3 =  lambda: process.stdout.readline().strip()

    def register(self, module, front=True):
        # module is a lambda
        if front:
            self.modules.insert(0, module)
        else:
            self.modules.append(module)

    def status(self):
        current = ""
        for module in self.modules:
            current += f' [{module()}] |'
        if self.i3:
            current += self.i3()
        return current


def get_wifi_name():
    try:
        # 使用 `nmcli` 获取当前连接的 WiFi 名称
        wifi_name = subprocess.check_output(["nmcli", "-t", "-f", "active,ssid", "dev", "wifi"], text=True)
        for line in wifi_name.splitlines():
            if line.startswith("yes:"):
                return line.split(":")[1]
        return "未连接到 WiFi"
    except Exception as e:
        return f"无法获取 WiFi 名称: {e}"

def get_ethernet_speed():
    try:
        # 遍历网络接口以获取有线连接的速度
        for interface, stats in psutil.net_if_stats().items():
            if stats.isup and "eth" in interface:  # 通常有线连接是 "eth" 开头
                return f"{interface}: {stats.speed} Mbps"
        return "未检测到有线连接"
    except Exception as e:
        return f"无法获取有线连接速度: {e}"

if __name__ == '__main__':
    mybar = mystatus(i3_enable=True)
    mybar.register( lambda: subprocess.run(['/home/owmaker/.bin/get_window_class.sh'], text=True, capture_output=True).stdout.strip())

    while True:
        current = mybar.status()
        print( current, flush=True)
        time.sleep(2)
