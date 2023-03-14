adb wait-for-device
adb root
adb remount
adb shell setprop persist.sys.setupwizard FINISH
adb shell pm disable com.sec.android.app.SecSetupWizard
adb shell pm disable com.google.android.setupwizard
adb shell content insert --uri content://settings/secure --bind name:s:user_setup_complete --bind value:i:1
adb shell content insert --uri content://settings/global --bind name:s:device_provisioned --bind value:i:1

