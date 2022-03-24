import winreg

connect_registry = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)

RealTime = winreg.OpenKey(connect_registry, "SOFTWARE\Microsoft\Windows Defender\Real-Time Protection")
TamperProtection = winreg.OpenKey(connect_registry, "SOFTWARE\Microsoft\Windows Defender\Features")
AntiSV = winreg.OpenKey(connect_registry, "SOFTWARE\Microsoft\Windows Defender")
Exclusion = winreg.OpenKey(connect_registry, "SOFTWARE\Microsoft\Windows Defender\Exclusions\Paths")

print("----------------Real-Time Protection----------------")
for n in range(winreg.QueryInfoKey(RealTime)[1]):
    x = winreg.EnumValue(RealTime, n)
    if(x[0] == "DisableRealtimeMonitoring"):
        print(x[0], x[1])

print("----------------TamperProtection----------------")
for n in range(winreg.QueryInfoKey(TamperProtection)[1]):
    x = winreg.EnumValue(TamperProtection, n)
    if(x[0] == "TamperProtection"):
        print(x[0], x[1])

print("----------------DisableAntiSpyware\AntiVirus----------------")
for n in range(winreg.QueryInfoKey(AntiSV)[1]):
    x = winreg.EnumValue(AntiSV, n)
    if(x[0] == "DisableAntiSpyware"):
        print(x[0], x[1])
    elif(x[0] == "DisableAntiVirus"):
        print(x[0], x[1])

print("----------------Exclusion----------------")
for n in range(winreg.QueryInfoKey(Exclusion)[1]):
    x = winreg.EnumValue(Exclusion, n)
    print(x[0], x[1])




