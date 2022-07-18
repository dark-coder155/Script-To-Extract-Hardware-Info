import platform
import psutil
import cpuinfo
import wmi





print(f"Architecture: {platform.architecture()}")
print(f"Netork Name: {platform.node()}")
print(f"Operating System: {platform.platform()}")
print(f"Processor: {platform.processor()}")
my_cpuinfo = cpuinfo.get_cpu_info()
print(f"Full CPU name: {my_cpuinfo['brand_raw']}")
print(f"CPU Frequency: {my_cpuinfo['hz_actual_friendly']}")
print(f"Full CPU name: {my_cpuinfo['hz_advertised_friendly']}")
print(f"Total Ram:{psutil.virtual_memory().total /1024/1024/1024 :.2f} GB")


pc =wmi.WMI()
os_info =pc.Win32_OperatingSystem()[0]
print(os_info)

print(pc.Win32_processor()[0])
print(pc.win32_networkadapterconfiguration()[0])
print(pc.Win32_logicaldisk()[0])
    
#print(my_cpuinfo)