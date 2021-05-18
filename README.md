# MINIFS-Decompression
The Decompressoin tool for Vxworks MINIFS.

## USAGE

```bash
python minifs_decompression.py [target_firmware]
```

example:

```bash
$ python minifs_decompress.py ./MW305R.BIN
1173+0 records in
1173+0 records out
1173 bytes transferred in 0.006129 secs (191392 bytes/sec)
58+0 records in
58+0 records out
58 bytes transferred in 0.000298 secs (194616 bytes/sec)
2464+0 records in
2464+0 records out
2464 bytes transferred in 0.012085 secs (203890 bytes/sec)
127+0 records in
127+0 records out
127 bytes transferred in 0.000661 secs (192163 bytes/sec)
419+0 records in
419+0 records out
419 bytes transferred in 0.002342 secs (178908 bytes/sec)
1483+0 records in
1483+0 records out
1483 bytes transferred in 0.007509 secs (197497 bytes/sec)
10316+0 records in
10316+0 records out
```

The result of decompress:

```bash
$ tree
.
├── conf
│   ├── mcbDesc.bin
│   ├── modelDesc.bin
│   ├── oem.txt
│   ├── priv-key.pem
│   └── server-cert.pem
├── minifs_decompress.py
└── web
    ├── common
    │   ├── AccessCtrl.htm
    │   ├── Advance.htm
    │   ├── Basic.htm
    │   ├── BasicDynamicIp.htm
    │   ├── BasicEptManagement.htm
    │   ├── BasicHead.htm
    │   ├── BasicMenu.htm
    │   ├── BasicNetWork.htm
    │   ├── BasicPPPoE.htm
    │   ├── BasicStaticIp.htm
    │   ├── BasicWireless.htm
    │   ├── Content.htm
    │   ├── DHCPServer.htm
    │   ├── DMZCfg.htm
    │   ├── DateTimeCfg.htm
    │   ├── DdnsCfg.htm
    │   ├── Diagnostic.htm
    │   ├── DynamicIp.htm
    │   ├── Foot.htm
    │   ├── Help.htm
    │   ├── IPMACBind.htm
    │   ├── Index.htm
    │   ├── LanCfg.htm
    │   ├── Login.htm
    │   ├── LoginChgPwd.htm
    │   ├── MacClone.htm
    │   ├── ManageSettingUp.htm
    │   ├── PPPoE.htm
    │   ├── ParentControl.htm
    │   ├── PhoneBasicNetWork.htm
    │   ├── PhoneBasicWireless.htm
    │   ├── PhoneDynamicIp.htm
    │   ├── PhoneEquipManage.htm
    │   ├── PhoneEquipManageDetail.htm
    │   ├── PhoneIndex.htm
    │   ├── PhoneLogin.htm
    │   ├── PhoneLoginChgPwd.htm
    │   ├── PhoneMenu.htm
    │   ├── PhoneOtherSet.htm
    │   ├── PhoneOtherSetChgPwd.htm
    │   ├── PhonePPPoE.htm
    │   ├── PhoneStaticIp.htm
    │   ├── PhoneWizard.htm
    │   ├── PhoneWizardDynamicIp.htm
    │   ├── PhoneWizardEnd.htm
    │   ├── PhoneWizardPPPoE.htm
    │   ├── PhoneWizardStaticIp.htm
    │   ├── PhoneWizardWireless.htm
    │   ├── RouteTable.htm
    │   ├── StaticIp.htm
    │   ├── SysBakNRestore.htm
    │   ├── SysChangeLgPwd.htm
    │   ├── SysReboot.htm
    │   ├── SysReset.htm
    │   ├── SysUpgrade.htm
    │   ├── SystemLog.htm
    │   ├── UpnpCfg.htm
    │   ├── VirtualServerCfg.htm
    │   ├── WanCfg.htm
    │   ├── Wizard.htm
    │   ├── WizardDynamicIp.htm
    │   ├── WizardEnd.htm
    │   ├── WizardPPPoE.htm
    │   ├── WizardStaticIp.htm
    │   ├── WizardWireless.htm
    │   ├── WlanGuestNetWorkCfg.htm
    │   ├── WlanNetwork.htm
    │   ├── WlanWDSCfg.htm
    │   ├── WlanWDSCfgEnd.htm
    │   ├── WlanWDSCfgFirst.htm
    │   ├── WlanWDSCfgFive.htm
    │   ├── WlanWDSCfgFour.htm
    │   ├── WlanWDSCfgSecond.htm
    │   └── WlanWDSCfgThird.htm
    ├── dynaform
    │   ├── DataGrid.css
    │   ├── DataGrid.js
    │   ├── class.css
    │   ├── class.js
    │   ├── macFactory.js
    │   ├── menu.css
    │   ├── menu.js
    │   ├── phoneClass.css
    │   └── phoneClass.js
    ├── images
    │   ├── QRcode_me.png
    │   ├── advance_me.png
    │   ├── backwardBtn_me.png
    │   ├── basic_me.png
    │   ├── circleLeft_me.png
    │   ├── circleRight_me.png
    │   ├── detailArrow_me.png
    │   ├── equipMng_me.png
    │   ├── errorPic_me.png
    │   ├── icon_me.ico
    │   ├── icon_wifi_me.png
    │   ├── logo_me.png
    │   ├── mngPwd_me.png
    │   ├── netSet_me.png
    │   ├── otherSet_me.png
    │   ├── rightIcon_me.png
    │   ├── wanDetecting_me.gif
    │   ├── wdsDetect_me.gif
    │   ├── wifiSet_me.png
    │   ├── wzdWarningWhite_me.png
    │   └── wzd_me.png
    ├── language
    │   └── cn
    │       ├── error.js
    │       └── str.js
    ├── lib
    │   ├── DM.js
    │   ├── Quary.js
    │   ├── ajax.js
    │   ├── jquery-1.10.1.min.js
    │   ├── model.js
    │   └── verify.js
    └── upnp
        ├── ifc.xml
        ├── igd.xml
        ├── ipc.xml
        ├── l3f.xml
        ├── wfa.xml
        └── wps.xml

9 directories, 124 files
```

## Reference

1. http://patentlib.net/mnt/sipo/A/20200818/5/CN102020000408790CN00001115525110AFULZH20200818CN00V/
