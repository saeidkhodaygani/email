import os
from django.http import HttpResponse

def wifi(requst):
    # os.system("nmcli connection add type wifi ifname '*' con-name my-hotspot autoconnect no ssid my-local-hotspot")
    # os.system("nmcli connection modify my-hotspot 802-11-wireless.mode ap 802-11-wireless.band bg ipv4.method shared")
    # os.system("nmcli connection modify my-hotspot 802-11-wireless-security.key-mgmt wpa-psk 802-11-wireless-security.psk myhardpassword")
    # os.system("nmcli connection up my-hotspot")
    os.system("echo 'Running...'")
    return HttpResponse("اسکریپت با موفقیت انجام شد.")