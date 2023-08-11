#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import re #for REGEX
import shutil
#global variable

#regular expression = REGEX
#BRE - POSIX
#ERE - POSIX
#etc - PERL...

#REGEX
p1 = re.compile('.*REGISTER.*NetworkRequest \[ REQUEST id=.*')
p2 = re.compile('.*RELEASE.*NetworkRequest \[ REQUEST id=.*')
p3 = re.compile('.*NetworkRequest \[ REQUEST id=.*')
p4 = re.compile('.*logcat.*radio.*')
p5 = re.compile('.*logcat.*main.*')
p6 = re.compile('.*main_log.*')
p7 = re.compile('.*radio_log.*')
#200702_15-11-45.log
p8 = re.compile('^\d{6}.*-\d{2}.*-\d{2}')
p9 = re.compile('.*onEnableApn:.*so return')
p10 = re.compile('.*onEnableApn:.*apnType=.*')
p11 = re.compile('.*AndroidRuntime.*android.*.*phone.*')
#p5 = re.compile('.*mAllApnSettings\[')
                  #mAllApnSettings size=5

#Setting, rild message
def autoAnalyzer_for_setting(given_name):
    if ('png' in given_name) : return
    if ('dumpstate_debug_history.lst' in given_name) : return
    if ('dumpstate_log.txt' in given_name) : return
    if ('dumpstate-stats.txt' in given_name) : return

    f_analysis_setting = open(given_name + "_wg_setting" , 'w')
    f_ori = open("./" + given_name, 'r')
    while True:
        line = f_ori.readline()
        if not line: break
       #if ('PhoneInterfaceManager: setUserDataEnabled' in line):
       #    f_analysis_setting.write(line.strip() + '\n')
        if ('- setDataRoamingEnabled change' in line):
            f_analysis_setting.write(line.strip() + '\n')
        if ('onUserMobileDataStateChanged' in line):
            f_analysis_setting.write(line.strip() + '\n')
        if ('- InternalDataEnabled change' in line):
            f_analysis_setting.write(line.strip() + '\n')
    f_analysis_setting.close()
    print("autoAnalyzer_for_setting done!")
#EPDG
def autoAnalyzer_for_epdg(given_name):
    if ('png' in given_name) : return
    if ('dumpstate_debug_history.lst' in given_name) : return
    if ('dumpstate_log.txt' in given_name) : return
    if ('dumpstate-stats.txt' in given_name) : return

    f_analysis_epdg = open(given_name + "_wg_epdg" , 'w')
    f_ori = open("./" + given_name, 'r')
    while True:
        line = f_ori.readline()
        if not line: break
        if ('EPDG --' in line):
            f_analysis_epdg.write(line.strip() + '\n')
        if ('ro.telephony.iwlan_operation_mode' in line):
            f_analysis_epdg.write(line.strip() + '\n')
    print("autoAnalyzer_for_epdg done!")
#json
def autoAnalyzer_for_json(given_name):
    if ('png' in given_name) : return
    if ('dumpstate_debug_history.lst' in given_name) : return
    if ('dumpstate_log.txt' in given_name) : return
    if ('dumpstate-stats.txt' in given_name) : return

    f_analysis_json = open(given_name + "_wg_json" , 'w')
    f_ori = open("./" + given_name, 'r')
    while True:
        line = f_ori.readline()
        if not line: break
        if ('IsSupportJsonCmd()' in line):
            f_analysis_json.write(line.strip() + '\n')
        if ('IpcProtocol41JsonData' in line):
            f_analysis_json.write(line.strip() + '\n')
    f_analysis_json.close()
    print("autoAnalyzer_for_json done!")
#FC
def autoAnalyzer_for_fc(given_name):
    if ('png' in given_name) : return
    if ('dumpstate_debug_history.lst' in given_name) : return
    if ('dumpstate_log.txt' in given_name) : return
    if ('dumpstate-stats.txt' in given_name) : return

    f_analysis_fc = open(given_name + "_wg_fc" , 'w')
    f_ori = open("./" + given_name, 'r')
    while True:
        line = f_ori.readline()
        if not line: break
        if ('AndroidRuntime:' in line):
            f_analysis_fc.write(line.strip() + '\n')
        if ('java.lang.SecurityException' in line):
            f_analysis_fc.write(line.strip() + '\n')
    f_analysis_fc.close()
    print("autoAnalyzer_for_fc done!")

#attach
def autoAnalyzer_for_attach(given_name):
    if ('png' in given_name) : return
    if ('dumpstate_debug_history.lst' in given_name) : return
    if ('dumpstate_log.txt' in given_name) : return
    if ('dumpstate-stats.txt' in given_name) : return

    f_analysis_attach= open(given_name + "_wg_attach" , 'w')
    f_ori = open("./" + given_name, 'r')
    while True:
        line = f_ori.readline()
        if not line: break
        if (': setInitialApn:' in line):
            f_analysis_attach.write(line.strip() + '\n')
        if (': processOnEmptyAttachApn:' in line):
            f_analysis_attach.write(line.strip() + '\n')
        if ('RIL_REQUEST_SET_INITIAL_ATTACH_' in line):
            f_analysis_attach.write(line.strip() + '\n')
        if (': IsRegisteredNetworkType():' in line):
            f_analysis_attach.write(line.strip() + '\n')
        if (': networkTypeBitmask:' in line):
            f_analysis_attach.write(line.strip() + '\n')
        if (': setInitialApn:' in line):
            f_analysis_attach.write(line.strip() + '\n')
        if (': IsPcscfNeeded(): pcscf' in line):
            f_analysis_attach.write(line.strip() + '\n')
        if (': IsEsmFlagZeroNetwork' in line):
            f_analysis_attach.write(line.strip() + '\n')
        if (': IA DataCallSetup -' in line):
            f_analysis_attach.write(line.strip() + '\n')
        if (': DoSetInitialAttachApn()' in line):
            f_analysis_attach.write(line.strip() + '\n')
        if (': SetLteAttachProfile: Attach Profile' in line):
            f_analysis_attach.write(line.strip() + '\n')
        if ('(M)GPRS_CMD (S)GPRS_SYNC_PROFILE_INFO' in line):
            f_analysis_attach.write(line.strip() + '\n')
        if ('[ril.attach.apn] ' in line):
            f_analysis_attach.write(line.strip() + '\n')
        if ('- setInitialAttachApn: X selected Apn' in line):
            f_analysis_attach.write(line.strip() + '\n')

    f_analysis_attach.close()
    print("autoAnalyzer_for_attach done!")

#booting time
def autoAnalyzer_for_booting(given_name):
    if ('png' in given_name) : return
    if ('dumpstate_debug_history.lst' in given_name) : return
    if ('dumpstate_log.txt' in given_name) : return
    if ('dumpstate-stats.txt' in given_name) : return

    f_analysis_booting= open(given_name + "_wg_booting" , 'w')
    f_ori = open("./" + given_name, 'r')
    while True:
        line = f_ori.readline()
        if not line: break
        if ('!@Boot' in line):
            f_analysis_booting.write(line.strip() + '\n')

    f_analysis_booting.write('vimgrep /!@Boot_SVC : PhoneApp OnCrate\|!@Boot_SVC : CS Registered\|!@Boot: Voice SVC is acquired\|!@Boot_SVC : SIM onAllRecordsLoaded\|!@Boot_SVC : setupDataCall\|!@Boot: Data SVC is acquired\|!@Boot: bootcomplete/ % | cw' + '\n')
    f_analysis_booting.close()
    print("autoAnalyzer_for_booting done!")


#simmanager
def autoAnalyzer_for_simmanager(given_name):
    if ('png' in given_name) : return
    if ('dumpstate_debug_history.lst' in given_name) : return
    if ('dumpstate_log.txt' in given_name) : return
    if ('dumpstate-stats.txt' in given_name) : return

    f_analysis_simmanager= open(given_name + "_wg_simmanager" , 'w')
    f_ori = open("./" + given_name, 'r')

    f_analysis_simmanager.write('SubscriptionController:' + '\n')
    f_analysis_simmanager.write('ActiveSubInfoList:' + '\n')
    while True:
        line = f_ori.readline()
        if not line: break
        if ('SimManager' in line):
            f_analysis_simmanager.write(line.strip() + '\n')
        elif ('android.telephony.action.SIM_CARD_STATE_CHANGED' in line):
            f_analysis_simmanager.write(line.strip() + '\n')
        elif ('onSimStateUpdated:' in line):
            f_analysis_simmanager.write(line.strip() + '\n')
        elif ('onDataConnectionStateChanged: state=' in line):
            f_analysis_simmanager.write(line.strip() + '\n')
        elif ('isMultiSimModel :' in line):
            f_analysis_simmanager.write(line.strip() + '\n')
    f_analysis_simmanager.close()
    print("autoAnalyzer_for_simmanager done!")

#"pdn open"
def autoAnalyzer_for_pdn_open(given_name):
    if ('png' in given_name) : return
    if ('dumpstate_debug_history.lst' in given_name) : return
    if ('dumpstate_log.txt' in given_name) : return
    if ('dumpstate-stats.txt' in given_name) : return

    f_analysis_pdn_open= open(given_name + "_wg_pdn_open" , 'w')
    f_ori = open("./" + given_name, 'r')

    f_analysis_pdn_open.write('PdnController<0>: onPreciseDataConnectionStateChanged' + '\n')
    f_analysis_pdn_open.write('PdnController<0>: onDataConnectionStateChanged:' + '\n')
    f_analysis_pdn_open.write('IndicatorLog: [NetworkController.MobileSignalController(0/1)]' + '\n')
    while True:
        line = f_ori.readline()
        if not line: break

        if ('- requestNetwork for NetworkRequest [ REQUEST id=' in line):
            f_analysis_pdn_open.write(line.strip() + '\n')
        elif ('- onEnableApn: apnType=' in line):
            f_analysis_pdn_open.write(line.strip() + '\n')
        elif ('DCT-C   : trySetupData for APN type' in line):
            f_analysis_pdn_open.write(line.strip() + '\n')
        elif ('> SETUP_DATA_CALL,accessNetworkType=' in line):
            f_analysis_pdn_open.write(line.strip() + '\n')
        elif ('< SETUP_DATA_CALL DataCallResponse: {' in line):
            f_analysis_pdn_open.write(line.strip() + '\n')
        elif ('DCT-C   : onDataSetupComplete: success apn=' in line):
            f_analysis_pdn_open.write(line.strip() + '\n')
        elif ('- onSetupConnectionCompleted result=' in line):
            f_analysis_pdn_open.write(line.strip() + '\n')
        elif ('SET_MOBILE_DATA_SETTING with mobile data setting' in line):
            f_analysis_pdn_open.write(line.strip() + '\n')
    f_analysis_pdn_open.close()
    print("autoAnalyzer_for_pdn_open done!")


#"Broadcasting ServiceState : "
def autoAnalyzer_for_broadcasting_from_sst(given_name):
    if ('png' in given_name) : return
    if ('dumpstate_debug_history.lst' in given_name) : return
    if ('dumpstate_log.txt' in given_name) : return
    if ('dumpstate-stats.txt' in given_name) : return

    f_analysis_broadcasting_from_sst= open(given_name + "_wg_broadcasting_from_sst" , 'w')
    f_ori = open("./" + given_name, 'r')
    while True:
        line = f_ori.readline()
        if not line: break

        if ('Broadcasting ServiceState :' in line):
            f_analysis_broadcasting_from_sst.write(line.strip() + '\n')

    f_analysis_broadcasting_from_sst.close()
    print("autoAnalyzer_for_broadcasting_from_sst done!")



def autoAnalyzer_for_signalcontroller(given_name):
    if ('png' in given_name) : return
    if ('dumpstate_debug_history.lst' in given_name) : return
    if ('dumpstate_log.txt' in given_name) : return
    if ('dumpstate-stats.txt' in given_name) : return

    f_analysis_signal= open(given_name + "_wg_signalcontroller" , 'w')
    f_ori = open("./" + given_name, 'r')
    while True:
        line = f_ori.readline()
        if not line: break

        if ('- notifyServiceStateForSubscriber' in line):
            f_analysis_signal.write(line.strip() + '\n')
        elif ('onDisplayInfoChanged: displayInfo=TelephonyDisplayInfo' in line):
            f_analysis_signal.write(line.strip() + '\n')

    f_analysis_signal.close()
    print("autoAnalyzer_for_signalcontroller done!")


def autoAnalyzer_for_request_dct_cs(given_name):
    if ('png' in given_name) : return
    if ('dumpstate_debug_history.lst' in given_name) : return
    if ('dumpstate_log.txt' in given_name) : return
    if ('dumpstate-stats.txt' in given_name) : return

    f_analysis_request_dct_cs= open(given_name + "_wg_request_dct_cs" , 'w')
    f_ori = open("./" + given_name, 'r')
    while True:
        line = f_ori.readline()
        if not line: break

        if ('completeConnection: successful, notify the world' in line):
            f_analysis_request_dct_cs.write(line.strip() + '\n')
        elif (p9.match(line)):
            f_analysis_request_dct_cs.write(line.strip() + '\n')
        elif (p10.match(line)):
            f_analysis_request_dct_cs.write(line.strip() + '\n')
        elif ('ConnectivityService: requestNetwork for' in line):
            f_analysis_request_dct_cs.write(line.strip() + '\n')
    f_analysis_request_dct_cs.close()
    print("autoAnalyzer_for_request_dct_cs done!")

def autoAnalyzer_for_switch_sim(given_name):
    if ('png' in given_name) : return
    if ('dumpstate_debug_history.lst' in given_name) : return
    if ('dumpstate_log.txt' in given_name) : return
    if ('dumpstate-stats.txt' in given_name) : return

    f_analysis_switch_sim= open(given_name + "_wg_switch_sim" , 'w')
    f_ori = open("./" + given_name, 'r')
    while True:
        line = f_ori.readline()
        if not line: break
        if (': Intent.getAction() : android.intent.action.ACTION_DEFAULT_DATA_SUBSCRIPTION_CHANGED' in line):
            f_analysis_switch_sim.write(line.strip() + '\n')
        elif (': ACTION_DEFAULT_DATA_SUBSCRIPTION_CHANGED, subId:' in line):
            f_analysis_switch_sim.write(line.strip() + '\n')
        elif ('DDS-SemPhoneSwitcher: broadcastDdsChangeResult' in line):
            f_analysis_switch_sim.write(line.strip() + '\n')
        elif ('DDS-SemPhoneSwitcher: auto dds is' in line):
            f_analysis_switch_sim.write(line.strip() + '\n')
        elif ('DDS Already was set to slot' in line):
            f_analysis_switch_sim.write(line.strip() + '\n')
        elif ('SubscriptionController: [setDefaultDataSubId] called by' in line):
            f_analysis_switch_sim.write(line.strip() + '\n')
        elif ('SubscriptionController: [broadcastDefaultDataSubIdChanged] subId' in line):
            f_analysis_switch_sim.write(line.strip() + '\n')
        elif ('QMI_DSD_GET_CURRENT_DDS_REQ' in line):
            f_analysis_switch_sim.write(line.strip() + '\n')
        elif ('QMI_DSD_SWITCH_DDS_REQ' in line):
            f_analysis_switch_sim.write(line.strip() + '\n')
        elif ('RxGetDualStandbyPref: current dds =' in line):
            f_analysis_switch_sim.write(line.strip() + '\n')
        elif ('OnGetDualStandbyPrefModemDone(): currentDds =' in line):
            f_analysis_switch_sim.write(line.strip() + '\n')
        elif ('Set SWITCH_PARAM_TEMPORARY owe to ims calling with non dds' in line):
            f_analysis_switch_sim.write(line.strip() + '\n')
        elif ('SET_PREFERRED_DATA_MODEM' in line):
            f_analysis_switch_sim.write(line.strip() + '\n')
        elif ('SettingsProvider: isChangeAllowed()' in line):
            f_analysis_switch_sim.write(line.strip() + '\n')
        elif ('called by com.samsung.telephonyui.callsettings.SamsungTuiCallFunctions' in line):
            f_analysis_switch_sim.write(line.strip() + '\n')
        elif ('DDS change success, PhoneId' in line):
            f_analysis_switch_sim.write(line.strip() + '\n')
        elif ('sendDefaultChangedBroadcast' in line):
            f_analysis_switch_sim.write(line.strip() + '\n')
        elif ('setDefaultDataSubId' in line):
            f_analysis_switch_sim.write(line.strip() + '\n')
        elif ('ALLOW_DATA allowed' in line):
            f_analysis_switch_sim.write(line.strip() + '\n')
        elif ('getRequestOverride : RequestOverride(mState = OVERRIDE' in line):
            f_analysis_switch_sim.write(line.strip() + '\n')
        elif ('getRequestOverride : RequestOverride(mState = RESTORE' in line):
            f_analysis_switch_sim.write(line.strip() + '\n')
    f_analysis_switch_sim.close()
    print("autoAnalyzer_for_switch_sim done!")



#ConnectivityService:
def autoAnalyzer_for_cs(given_name):
    if ('png' in given_name) : return
    if ('dumpstate_debug_history.lst' in given_name) : return
    if ('dumpstate_log.txt' in given_name) : return
    if ('dumpstate-stats.txt' in given_name) : return

    f_analysis_cs= open(given_name + "_wg_cs" , 'w')
    f_ori = open("./" + given_name, 'r')
    while True:
        line = f_ori.readline()
        if not line: break

        if ('ConnectivityService:' in line):
            f_analysis_cs.write(line.strip() + '\n')
    f_analysis_cs.close()
    print("autoAnalyzer_for_cs done!")


#(M)GPRS_CMD, (M)GEN_CMD
def autoAnalyzer_for_gprs(given_name):
    if ('png' in given_name) : return
    if ('dumpstate_debug_history.lst' in given_name) : return
    if ('dumpstate_log.txt' in given_name) : return
    if ('dumpstate-stats.txt' in given_name) : return

    f_analysis_gprs= open(given_name + "_wg_gprs" , 'w')
    f_ori = open("./" + given_name, 'r')
    while True:
        line = f_ori.readline()
        if not line: break

        if ('(M)GPRS_CMD' in line):
            f_analysis_gprs.write(line.strip() + '\n')
        elif ('(M)GEN_CMD' in line):
            f_analysis_gprs.write(line.strip() + '\n')
    f_analysis_gprs.close()
    print("autoAnalyzer_for_gprs done!")


#E RILD    :
def autoAnalyzer_for_rild(given_name):
    if ('png' in given_name) : return
    if ('dumpstate_debug_history.lst' in given_name) : return
    if ('dumpstate_log.txt' in given_name) : return
    if ('dumpstate-stats.txt' in given_name) : return

    f_analysis_rild= open(given_name + "_wg_rild" , 'w')
    f_ori = open("./" + given_name, 'r')
    while True:
        line = f_ori.readline()
        if not line: break

        if ('RILD' in line):
            f_analysis_rild.write(line.strip() + '\n')
        elif ('RilMonitor:' in line):
            f_analysis_rild.write(line.strip() + '\n')
        elif ('RILJ    :' in line):
            f_analysis_rild.write(line.strip() + '\n')
        elif ('SEM_RILJ' in line):
            f_analysis_rild.write(line.strip() + '\n')
        elif ('ril daemon' in line):
            f_analysis_rild.write(line.strip() + '\n')
        elif ('DEBUG   : Cmdline: /vendor/bin/hw/rild' in line):
            f_analysis_rild.write(line.strip() + '\n')
    print("autoAnalyzer_for_rild done!")

#D DCT-C
def autoAnalyzer_for_dct(given_name):
    if ('png' in given_name) : return
    if ('dumpstate_debug_history.lst' in given_name) : return
    if ('dumpstate_log.txt' in given_name) : return
    if ('dumpstate-stats.txt' in given_name) : return

    f_analysis_dct= open(given_name + "_wg_dct" , 'w')
    f_ori = open("./" + given_name, 'r')
    while True:
        line = f_ori.readline()
        if not line: break

        if ('D DCT-C' in line):
            f_analysis_dct.write(line.strip() + '\n')
        elif ('D DCT-I' in line) : 
            f_analysis_dct.write(line.strip() + '\n')
    f_analysis_dct.close()
    print("autoAnalyzer_for_dct done2!")

#D DNC-
def autoAnalyzer_for_dnc(given_name):
    if ('png' in given_name) : return
    if ('dumpstate_debug_history.lst' in given_name) : return
    if ('dumpstate_log.txt' in given_name) : return
    if ('dumpstate-stats.txt' in given_name) : return

    f_analysis_dnc= open(given_name + "_wg_dnc" , 'w')
    f_ori = open("./" + given_name, 'r')
    while True:
        line = f_ori.readline()
        if not line: break

        if ('DNC-' in line):
            f_analysis_dnc.write(line.strip() + '\n')
    f_analysis_dnc.close()
    print("autoAnalyzer_for_dnc done2!")


#cp reset
def autoAnalyzer_for_cpreset(given_name):
    if ('png' in given_name) : return
    if ('dumpstate_debug_history.lst' in given_name) : return
    if ('dumpstate_log.txt' in given_name) : return
    if ('dumpstate-stats.txt' in given_name) : return

    f_analysis_cpreset= open(given_name + "_wg_cpreset" , 'w')
    f_ori = open("./" + given_name, 'r')
    while True:
        line = f_ori.readline()
        if not line: break

        if ('persist.radio.silent-reset' in line):
            f_analysis_cpreset.write(line.strip() + '\n')
        elif ('DoModemSilentReset' in line):
            f_analysis_cpreset.write(line.strip() + '\n')
        elif ('unexpected reset external modem' in line):
            f_analysis_cpreset.write(line.strip() + '\n')
        elif ('mdm_errfatal: mdm sent errfatal interrupt' in line):
            f_analysis_cpreset.write(line.strip() + '\n')
    f_analysis_cpreset.close()
    print("autoAnalyzer_for_cpreset done!")


#block
def autoAnalyzer_for_block(given_name):
    if ('png' in given_name) : return
    if ('dumpstate_debug_history.lst' in given_name) : return
    if ('dumpstate_log.txt' in given_name) : return
    if ('dumpstate-stats.txt' in given_name) : return

    f_analysis_block= open(given_name + "_wg_block" , 'w')
    f_ori = open("./" + given_name, 'r')
    while True:
        line = f_ori.readline()
        if not line: break

        if ('firewallSetUidRule(3,' in line): #powersaver
            f_analysis_block.write(line.strip() + '\n')
        if ('firewallSetUidRule(4,' in line):
            f_analysis_block.write(line.strip() + '\n')
        elif ('-blocked by power restrictions' in line):
            f_analysis_block.write(line.strip() + '\n')


    f_analysis_block.write('백그라운드 동작을 하는 앱이 power save에 의해 blocked 되고 있습니다' + '\n')
    f_analysis_block.write('*설정 -> 찾기(돋보기아이콘)배터리 사용량 최적화 -> 최적화하지 않은 앱 선택해서 전체로 변경 -> WeChat등 white list처리 원하는 app선택(파란색 -> 그레이 변경) 고객님께 가이드 부탁 드립니다.' + '\n')


    f_analysis_block.close()
    print("autoAnalyzer_for_block done!")

#mms
def autoAnalyzer_for_mms(given_name):
    if ('png' in given_name) : return
    if ('dumpstate_debug_history.lst' in given_name) : return
    if ('dumpstate_log.txt' in given_name) : return
    if ('dumpstate-stats.txt' in given_name) : return

    f_analysis_mms = open(given_name + "_wg_mms" , 'w')
    f_ori = open("./" + given_name, 'r')
    while True:
        line = f_ori.readline()
        if not line: break

#trySetupData for APN type mms
#setupData: apnContext={mApnType=mms
#bringUp: apnContext={mApnType=mms
#setupData: initing!
#notifyConnectCompleted at

        if ('MmsNetworkManager: start new network request' in line):
            f_analysis_mms.write(line.strip() + '\n')
        elif ('MmsHttpClient:' in line):
            f_analysis_mms.write(line.strip() + '\n')
        elif ('MmsNetworkManager' in line):
            f_analysis_mms.write(line.strip() + '\n')
        elif ('MmsRequest:' in line):
            f_analysis_mms.write(line.strip() + '\n')
        elif ('trySetupData for APN type mms' in line):
            f_analysis_mms.write(line.strip() + '\n')
        elif ('setupData: apnContext={mApnType=mms' in line):
            f_analysis_mms.write(line.strip() + '\n')
        elif ('bringUp: apnContext={mApnType=mms ' in line):
            f_analysis_mms.write(line.strip() + '\n')
        elif ('setupData: initing!' in line):
            f_analysis_mms.write(line.strip() + '\n')
        elif ('notifyConnectCompleted at' in line):
            f_analysis_mms.write(line.strip() + '\n')
        elif ('completeConnection: successful, notify the world apnContext' in line):
            f_analysis_mms.write(line.strip() + '\n')
        elif ('CALLBACK_AVAILABLE' in line):
            f_analysis_mms.write(line.strip() + '\n')
        elif ('NetworkCallbackListener.onAvailable' in line):
            f_analysis_mms.write(line.strip() + '\n')
    f_analysis_mms.close()
    print("autoAnalyzer_for_mms done!")


#setup_data_call
def autoAnalyzer_for_setup_data_call(given_name):
    if ('png' in given_name) : return
    if ('dumpstate_debug_history.lst' in given_name) : return
    if ('dumpstate_log.txt' in given_name) : return
    if ('dumpstate-stats.txt' in given_name) : return

    f_analysis_setup_data_call = open(given_name + "_wg_setup_data_call" , 'w')
    f_ori = open("./" + given_name, 'r')
    f_analysis_setup_data_call.write('I PdnController' + '\n')
    while True:
        line = f_ori.readline()
        if not line: break

#ePDN setup failed
#ConnectivityManager: requestNetwork; Calling
#DDS-DcTracker.requestNetwork for NetworkRequest

        if ('DDS-DcTracker.requestNetwork for NetworkRequest' in line):
            f_analysis_setup_data_call.write(line.strip() + '\n')
        elif ('ConnectivityManager: requestNetwork; Calling' in line):
            f_analysis_setup_data_call.write(line.strip() + '\n')
        elif ('ConnectivityManager: sendRequestForNetwork CallingUid' in line):
            f_analysis_setup_data_call.write(line.strip() + '\n')
        elif ('SETUP_DATA_CALL,accessN' in line):
            f_analysis_setup_data_call.write(line.strip() + '\n')
        elif ('SETUP_DATA_CALL DataCal' in line):
            f_analysis_setup_data_call.write(line.strip() + '\n')
        elif ('setPreferredDataModem: modemId=' in line):
            f_analysis_setup_data_call.write(line.strip() + '\n')
        elif ('RIL-QMI : FailCause(' in line):
            f_analysis_setup_data_call.write(line.strip() + '\n')
        elif ('GPRS_CMD (S)GPRS_IP_CONFIGURATION' in line):
            f_analysis_setup_data_call.write(line.strip() + '\n')
        elif ('(S)GPRS_CALL_STATUS (T)NOTI' in line):
            f_analysis_setup_data_call.write(line.strip() + '\n')
        elif ('trySetupData for APN type' in line):
            f_analysis_setup_data_call.write(line.strip() + '\n')
        elif ('trySetupData failed. apnContext' in line):
            f_analysis_setup_data_call.write(line.strip() + '\n')
        elif ('onTrySetupData: apnContext' in line):
            f_analysis_setup_data_call.write(line.strip() + '\n')
        elif ('trySetupData for type' in line):
            f_analysis_setup_data_call.write(line.strip() + '\n')
        elif ('SETUP_DATA_CALL' in line):
            f_analysis_setup_data_call.write(line.strip() + '\n')
        elif ('SETUP_DATA_CALL' in line):
            f_analysis_setup_data_call.write(line.strip() + '\n')
        elif ('throttle APN' in line):
            f_analysis_setup_data_call.write(line.strip() + '\n')
        elif ('Use longer throttled time' in line):
            f_analysis_setup_data_call.write(line.strip() + '\n')
        elif ('ePDN setup failed' in line):
            f_analysis_setup_data_call.write(line.strip() + '\n')
        elif ('DCT-C   : onDataSetupComplete:' in line):
            f_analysis_setup_data_call.write(line.strip() + '\n')
        elif ('DCT-C   : cause =' in line):
            f_analysis_setup_data_call.write(line.strip() + '\n')
        elif ('OnIpv6ConfigurationFailure:' in line):
            f_analysis_setup_data_call.write(line.strip() + '\n')
        elif ('OnIpv4ConfigurationFailure:' in line):
            f_analysis_setup_data_call.write(line.strip() + '\n')
        elif ('Transaction timeout' in line):
            f_analysis_setup_data_call.write(line.strip() + '\n')
        elif ('startPdnConnectivity:' in line):
            f_analysis_setup_data_call.write(line.strip() + '\n')
        elif ('SET_PREFERRED_NETWORK_TYPE' in line):
            f_analysis_setup_data_call.write(line.strip() + '\n')
        elif ('setUserPreferredNetworkType' in line):
            f_analysis_setup_data_call.write(line.strip() + '\n')
        elif ('setPreferredNetworkMode' in line): #5G 우선, 4G우선 한국향
            f_analysis_setup_data_call.write(line.strip() + '\n')

    f_analysis_setup_data_call.close()
    print("autoAnalyzer_for_setup_data_call done!")

#regi
#ImsRegistrationState - registered
def autoAnalyzer_for_regi(given_name):
    if ('png' in given_name) : return
    if ('dumpstate_debug_history.lst' in given_name) : return
    if ('dumpstate_log.txt' in given_name) : return
    if ('dumpstate-stats.txt' in given_name) : return

    f_analysis_regi = open(given_name + "_wg_regi" , 'w')
    f_ori = open("./" + given_name, 'r')
    while True:
        line = f_ori.readline()
        if not line: break

        if ('DATA_REGISTRATION_STATE' in line):
            f_analysis_regi .write(line.strip() + '\n')
        elif ('ImsRegistrationState - registered' in line):
            f_analysis_regi .write(line.strip() + '\n')

    f_analysis_regi.close()
    print("autoAnalyzer_for_regi done!")

#ground
def autoAnalyzer_for_ground(given_name):
    if ('png' in given_name) : return
    if ('dumpstate_debug_history.lst' in given_name) : return
    if ('dumpstate_log.txt' in given_name) : return
    if ('dumpstate-stats.txt' in given_name) : return

    wifi_set = 0
    telephonyfeature = 0

    f_analysis_ground = open(given_name + "_wg_ground" , 'w')
    f_ori = open("./" + given_name, 'r')
    while True:
        line = f_ori.readline()
        if not line: break

        if ('[gsm.sim.' in line):
            f_analysis_ground.write(line.strip() + '\n')
        elif ('mMaxActivePhones : ' in line):
            f_analysis_ground.write(line.strip() + '\n')
        elif ('vendor.gsm.sim' in line):
            f_analysis_ground.write(line)
        elif ('[TelephonyFeatures]' in line):
            if telephonyfeature  == 0:
                f_analysis_ground.write('\n')
                telephonyfeature += 1
            f_analysis_ground.write(line.strip() + '\n')
        elif ('name:mobile_data' in line):
            f_analysis_ground.write('\n')
            f_analysis_ground.write(line.strip() + '\n')
        elif ('mDataEnabledSettings=[mInternalDataEnabled' in line):
            f_analysis_ground.write(line.strip() + '\n')
        elif ('name:data_roaming name:mobile_data' in line):
            f_analysis_ground.write(line.strip() + '\n')
        elif ('name:data_roaming' in line):
            f_analysis_ground.write(line.strip() + '\n')
        elif ('Build Date is' in line):
            f_analysis_ground.write('\n')
            f_analysis_ground.write(line.strip() + '\n')
        elif ('DefaultNetworkEvent(netId=' in line):
            f_analysis_ground.write(line.strip() + '\n')
        elif ('WifiManager.setWifiEnabled(' in line): #
            if wifi_set == 0:
                f_analysis_ground.write('\n')
                wifi_set += 1
            f_analysis_ground.write(line.strip() + '\n')
        elif ('getRequestOverride : mPrimaryDataSubId(-1) is not valid!' in line):
            f_analysis_ground.write(line.strip() + '\n')
        elif ('setPreferredNetworkType - networkType:' in line):
            f_analysis_ground.write(line.strip() + '\n')
        elif ('chipname=' in line):
            f_analysis_ground.write(line.strip() + '\n')
        elif ('[GNSS_CHIPSET]' in line):
            f_analysis_ground.write(line.strip() + '\n')
        elif ('[MOBILE_DATA] Connection' in line):
            f_analysis_ground.write(line.strip() + '\n')
        elif ('[WIFI] Connection=' in line):
            f_analysis_ground.write(line.strip() + '\n')
        elif ('name:device_name pkg' in line):
            f_analysis_ground.write(line.strip() + '\n')
        elif ('ro.build.version.sdk' in line):
            f_analysis_ground.write(line.strip() + '\n')
        elif ('Kernel: Linux version' in line):
            f_analysis_ground.write(line.strip() + '\n')
        elif ('GsmNetworkManager radio off' in line):
            f_analysis_ground.write(line.strip() + '\n')
        elif ('getCurrentParam: mobile_data_on' in line):
            f_analysis_ground.write(line.strip() + '\n')
        elif ('mUserDataEnabled :' in line):
            f_analysis_ground.write('\n')
            f_analysis_ground.write(line.strip() + '\n')
            while True:
                line = f_ori.readline()
                if '*' not in  line :
                    f_analysis_ground.write(line.strip() + '\n')
                else:
                    f_analysis_ground.write('\n')
                    break
        elif ('QuickBuild ID' in line):
            f_analysis_ground.write(line.strip() + '\n')
        elif ('QB link :' in line):
            f_analysis_ground.write('build info1\n')
            f_analysis_ground.write(line.strip() + '\n')
            f_analysis_ground.write('\n')
        elif ('Samsung S-Boot' in line):
            f_analysis_ground.write('build info2\n')
            f_analysis_ground.write(line.strip() + '\n')
            f_analysis_ground.write('\n')
        elif ('ro.omc.build.id' in line):
            f_analysis_ground.write('build info3\n')
            f_analysis_ground.write(line.strip() + '\n')
            f_analysis_ground.write('\n')
        elif ('|  REBOOT  |       | REASON' in line):
            f_analysis_ground.write(line.strip() + '\n')
        elif ('== dumpstate:' in line):
            f_analysis_ground.write(line.strip() + '\n')
        elif ('IntentBroadcaster: Broadcasting and adding intent for rebroadcast: android.intent.action.SIM_STATE_CHANGED' in line):
            f_analysis_ground.write(line.strip() + '\n')
        elif ('ro.csc.omcnw_code' in line):
            f_analysis_ground.write(line.strip() + '\n')
        elif ('ro.csc.sales_code' in line):
            f_analysis_ground.write(line.strip() + '\n')
        elif ('ro.csc.sales_code' in line):
            f_analysis_ground.write(line.strip() + '\n')
        elif ('ro.csc.country_code' in line):
            f_analysis_ground.write(line.strip() + '\n')
        elif ('ro.hardware' in line):
            f_analysis_ground.write(line.strip() + '\n')
        elif ('buildId' in line):
            f_analysis_ground.write(line.strip() + '\n')
        elif ('Switching to new default network for' in line):
            f_analysis_ground.write(line.strip() + '\n')
        elif ('QuickBuild ID' in line):
            f_analysis_ground.write(line.strip() + '\n')
        elif ('sec_debug_level,' in line):
            f_analysis_ground.write(line.strip() + '\n')
        elif ('callList didn\'t initialized' in line):
            f_analysis_ground.write(line.strip() + '\n')
        elif ('- setDataRoamingEnabled change to' in line):
            f_analysis_ground.write(line.strip() + '\n')
        elif ('- UserDataEnabled change to' in line):
            f_analysis_ground.write(line.strip() + '\n')
        elif ('data_preferred_mode_during_calling' in line):
            f_analysis_ground.write(line.strip() + '\n')
        elif ('ro.boot.debug_level' in line):
            f_analysis_ground.write(line.strip() + '\n')
        elif ('name:data_preferred_mode_during_calling' in line):
            f_analysis_ground.write(line.strip() + '\n')
        elif ('carrier_metered_apn_types_strings = ' in line):
            f_analysis_ground.write(line.strip() + '\n')
        elif ('ro.boot.hardware' in line):
            f_analysis_ground.write(line.strip() + '\n')
        elif ('setMobileDataSetting: enabled ' in line):
            f_analysis_ground.write(line.strip() + '\n')
        elif ('sys.smf.mnoname' in line):
            f_analysis_ground.write(line.strip() + '\n')
        elif ('Modem Reset' in line):
            f_analysis_ground.write(line.strip() + '\n')
        elif ('mGid1=' in line):
            f_analysis_ground.write(line.strip() + '\n')
        elif ('mGid2=' in line):
            f_analysis_ground.write(line.strip() + '\n')
        elif ('D SDMConfig:   ' in line):
            f_analysis_ground.write(line.strip() + '\n')
        elif ('setMobileDataEnabled' in line):
            f_analysis_ground.write(line.strip() + '\n')
        elif ('DUMP OF SERVICE netpolicy:' in line):
            f_analysis_ground.write(line.strip() + '\n')
        elif ('SaveImageInBackgroundTask: mImageFilePath' in line):
            f_analysis_ground.write(line.strip() + '\n')
        elif ('FreecessTrigger: doze state changed' in line):
            f_analysis_ground.write(line.strip() + '\n')
        elif ('Returning BLOCKED NetworkInfo to uid' in line):
            f_analysis_ground.write(line.strip() + '\n')
        elif ('setDataEnabledForReason' in line):
            f_analysis_ground.write(line.strip() + '\n')
    f_analysis_ground.close()
    print("autoAnalyzer_for_ground done!")

        
#stall
def autoAnalyzer_for_stall(given_name):
    if ('png' in given_name) : return
    if ('dumpstate_debug_history.lst' in given_name) : return
    if ('dumpstate_log.txt' in given_name) : return
    if ('dumpstate-stats.txt' in given_name) : return
    f_analysis_stall=  open(given_name + "_wg_stall", 'w')

    f_ori = open("./" + given_name, 'r')
    while True:
        line = f_ori.readline()
        if not line: break

        if ('trigger data stall recovery' in line):
            f_analysis_stall.write(line.strip() + '\n')
        elif ('putRecoveryAction:' in line):
            f_analysis_stall.write(line.strip() + '\n')
        elif ('skip back to back data stall recovery' in line):
            f_analysis_stall.write(line.strip() + '\n')
        elif ('skip data stall recovery : state = ' in line):
            f_analysis_stall.write(line.strip() + '\n')

    f_analysis_stall.close()
    print("autoAnalyzer_for_stall done!")

#roaming
def autoAnalyzer_for_roaming(given_name):
    if ('png' in given_name) : return
    if ('dumpstate_debug_history.lst' in given_name) : return
    if ('dumpstate_log.txt' in given_name) : return
    if ('dumpstate-stats.txt' in given_name) : return
    f_analysis_roaming = open(given_name + "_wg_roaming", 'w')

    f_ori = open("./" + given_name, 'r')
    while True:
        line = f_ori.readline()
        if not line: break

        if ('setDefaultDataRoamingEnable' in line):
            f_analysis_roaming.write(line.strip() + '\n')

    f_analysis_roaming.close()
    print("autoAnalyzer_for_roaming done!")

#dns
def autoAnalyzer_for_dns(given_name):
    if ('png' in given_name) : return
    if ('dumpstate_debug_history.lst' in given_name) : return
    if ('dumpstate_log.txt' in given_name) : return
    if ('dumpstate-stats.txt' in given_name) : return

    f_analysis_dns= open(given_name + "_wg_dns", 'w')

    f_ori = open("./" + given_name, 'r')
    while True:
        line = f_ori.readline()
        if not line: break

        if ('DnsProxyListener: DNS' in line):
            f_analysis_dns.write(line.strip() + '\n')
        elif ('tcp sent-ack_diff' in line):
            f_analysis_dns.write(line.strip() + '\n')
        elif ('ConnectivityMetricsEvent(' in line):
            f_analysis_dns.write(line.strip() + '\n')
        elif ('resolv  :' in line):
            f_analysis_dns.write(line.strip() + '\n')
        elif ('NetdEventListenerService: DNS Requested by : ' in line):
            f_analysis_dns.write(line.strip() + '\n')
        elif (': DNS failed' in line):
            f_analysis_dns.write(line.strip() + '\n')
    f_analysis_dns.close()
    print("autoAnalyzer_for_dns done!")

#newtwork_request
def autoAnalyzer_for_network_request(given_name):
    if ('png' in given_name) : return
    if ('dumpstate_debug_history.lst' in given_name) : return
    if ('dumpstate_log.txt' in given_name) : return
    if ('dumpstate-stats.txt' in given_name) : return

    f_analysis_network_request = open(given_name + "_wg_network_request", 'w')

    f_ori = open("./" + given_name, 'r')
    while True:
        line = f_ori.readline()
        if not line: break

        if ('NetworkRequestInfoLogs - system (most recent first):' in line): # NetworkRequestInfoLogs - system (most recent first):
            f_analysis_network_request.write('\n\n\n')
            f_analysis_network_request.write(line.strip() + '\n')
            while True:
                line = f_ori.readline()
                if not line == '\n':
                    f_analysis_network_request.write(line.strip() + '\n')
                else:
                    break
        elif (p1.match(line)):
            f_analysis_network_request.write(line.strip() + '\n')
        elif (p2.match(line)):
            f_analysis_network_request.write(line.strip() + '\n')
        elif (p3.match(line)):
            f_analysis_network_request.write(line.strip() + '\n')
        elif ('requestNetwork for NetworkRequest' in line):
            f_analysis_network_request.write(line.strip() + '\n')
        elif ('releaseNetwork for NetworkRequest' in line):
            f_analysis_network_request.write(line.strip() + '\n')

    f_analysis_network_request.close()
    print("autoAnalyzer_for_network_request done!")

#data_activity
def autoAnalyzer_for_data_activity(given_name):
    if ('png' in given_name) : return
    if ('dumpstate_log.txt' in given_name) : return
    if ('dumpstate-stats.txt' in given_name) : return
'''
    if ('dumpstate_debug_history.lst' in given_name) : return

    f_analysis_data_activity = open(given_name + "_wg_data_activity", 'w')

    f_ori = open("./" + given_name, 'r')
    while True:
        line = f_ori.readline()
        if not line: break

        if ('onDataActivity: direction=' in line):
            f_analysis_data_activity.write(line.strip() + '\n')
        elif ('!@Screen__On' in line):
            f_analysis_data_activity.write(line.strip() + '\n')
        elif ('!@Screen__Off' in line):
            f_analysis_data_activity.write(line.strip() + '\n')

    f_analysis_data_activity.close()
'''
    #print("autoAnalyzer_for_data_activity done!")

# secril

#/.*androidruntime.*android.*/
def autoAnalyzer_for_secril(given_name):
    if ('png' in given_name) : return
    if ('dumpstate_log.txt' in given_name) : return
    if ('dumpstate-stats.txt' in given_name) : return
    if ('dumpstate_debug_history.lst' in given_name) : return

    f_analysis_secril = open(given_name + "_wg_secril", 'w')

    f_ori = open("./" + given_name, 'r')
    while True:
        line = f_ori.readline()
        if not line: break

        if ('due to RILD restart' in line):
            f_analysis_secril.write(line.strip() + '\n')
        elif ('LEDC-MGR(' in line):
            f_analysis_secril.write(line.strip() + '\n')

#p11 = re.compile('.*androidruntime.*android.*.*phone.*')
        #elif (p11.search(line)):
        #    f_analysis_secril.write(line.strip() + '\n')

    f_analysis_secril.close()
    print("autoAnalyzer_for_secril done!")

#monitor
def autoAnalyzer_for_monitor(given_name):
    if ('png' in given_name) : return
    if ('dumpstate_debug_history.lst' in given_name) : return
    if ('dumpstate_log.txt' in given_name) : return
    if ('dumpstate-stats.txt' in given_name) : return
    monitor_set = 0

    f_analysis_monitor = open(given_name + "_wg_monitor", 'w')

    f_ori = open("./" + given_name, 'r')
    while True:
        line = f_ori.readline()
        if not line: break

        if ('NetworkMonitor' in line):
            if monitor_set== 0:
                f_analysis_monitor.write('vimgrep /wm_on_top_resumed_lost_called\|wm_on_top_resumed_gained_called/ % | cw' + '\n')
                f_analysis_monitor.write('vimgrep /NetworkEvent(NETWORK_CONNECTED\|NetworkEvent(NETWORK_DISCONNECTED/ % | cw' + '\n')
                f_analysis_monitor.write('vimgrep /> SETUP_DATA_CALL,ac\|getRetryTimer: \|Screens all off\|Screen INTERNAL on\|< SETUP_DATA_CALL\|suggested retry\|throttled time\|< DATA_REGISTRATION_STATE\|Stop retrying.\|reasons: NOT_ATTACHED\|RetryManager:/ % | cw' + '\n')
                f_analysis_monitor.write(':/      {mApnType=' + '\n')
                f_analysis_monitor.write('set nowrap' + '\n')
                f_analysis_monitor.write('set ft= syn =' + '\n')
                f_analysis_monitor.write('syntax off' + '\n')
                f_analysis_monitor.write('Historical broadcasts summary [background]:' + '\n')
                f_analysis_monitor.write('Historical broadcasts summary [foreground]:' + '\n')
                f_analysis_monitor.write('--------------------------\\n      {mApnType=default' + '\n')
                f_analysis_monitor.write('History (mobile_data)' + '\n')
                monitor_set+= 1
            f_analysis_monitor.write(line.strip() + '\n')
        elif ('DUMP OF SERVICE connmetrics:' in line):
            f_analysis_monitor.write('\n')
            f_analysis_monitor.write(line.strip() + '\n')
            while True:
                line = f_ori.readline()
                if not line == '\n':
                    f_analysis_monitor.write(line.strip() + '\n')
                else:
                    break
        elif ('dns/connect events:' in line):
            f_analysis_monitor.write('\n')
            f_analysis_monitor.write(line.strip() + '\n')
            while True:
                line = f_ori.readline()
                if not line == '\n':
                    f_analysis_monitor.write(line.strip() + '\n')
                else:
                    break
        elif ('network statistics:' in line):
            f_analysis_monitor.write('\n')
            f_analysis_monitor.write(line.strip() + '\n')
            while True:
                line = f_ori.readline()
                if not line == '\n':
                    f_analysis_monitor.write(line.strip() + '\n')
                else:
                    break
    f_analysis_monitor.close()
    print("autoAnalyzer_for_monitor done!")

#monitor2
def autoAnalyzer_for_monitor2(given_name):
    if ('png' in given_name) : return
    if ('dumpstate_debug_history.lst' in given_name) : return
    if ('dumpstate_log.txt' in given_name) : return
    if ('dumpstate-stats.txt' in given_name) : return

    f_analysis_monitor2 = open(given_name + "_wg_monitor2", 'w')

    f_ori = open("./" + given_name, 'r')
    while True:
        line = f_ori.readline()
        if not line: break
        elif ('NetworkEvent(NETWORK_CONNECTED' in line):
            f_analysis_monitor2.write(line.strip() + '\n')
        elif ('NetworkEvent(NETWORK_DISCONNECTED' in line):
            f_analysis_monitor2.write(line.strip() + '\n')
        elif ('SETUP_DATA_CALL' in line):
            f_analysis_monitor2.write(line.strip() + '\n')
        elif ('NetworkAgentInfo{network{' in line):
            f_analysis_monitor2.write(line.strip() + '\n')
        elif ('DcNetworkAgent-' in line):
            f_analysis_monitor2.write(line.strip() + '\n')
    f_analysis_monitor2.close()
    print("autoAnalyzer_for_monitor2 done!")
#voice_call
def autoAnalyzer_for_voice_call(given_name):
    if ('png' in given_name) : return
    if ('dumpstate_debug_history.lst' in given_name) : return
    if ('dumpstate_log.txt' in given_name) : return
    if ('dumpstate-stats.txt' in given_name) : return

    f_analysis_voice_call =  open(given_name + "_wg_voice_call", 'w')

    f_ori = open("./" + given_name, 'r')
    while True:
        line = f_ori.readline()
        if not line: break
        elif ('onVoiceCallStarted' in line): 
            f_analysis_voice_call.write(line.strip() + '\n') 
        elif ('getDataConnectionState apnType=' in line): 
            f_analysis_voice_call.write(line.strip() + '\n') 
        elif ('stopNetStatPoll' in line): 
            f_analysis_voice_call.write(line.strip() + '\n') 
        elif ('stopDataStallAlarm' in line): 
            f_analysis_voice_call.write(line.strip() + '\n') 
        elif ('startNetStatPoll' in line): 
            f_analysis_voice_call.write(line.strip() + '\n') 
        elif ('startDataStallAlarm' in line): 
            f_analysis_voice_call.write(line.strip() + '\n') 
        elif ('startDataStallAlarm: tag' in line): 
            f_analysis_voice_call.write(line.strip() + '\n') 
        elif ('onVoiceCallEnd' in line): 
            f_analysis_voice_call.write(line.strip() + '\n') 
        elif ('GET_CURRENT_CALLS' in line): 
           f_analysis_voice_call.write(line.strip() + '\n') 
        elif ('TelephonyRegistry: notifyDataConnectionForSubscriber:' in line): 
            f_analysis_voice_call.write(line.strip() + '\n') 
        elif ('makeCall {' in line): 
            f_analysis_voice_call.write(line.strip() + '\n') 

    f_analysis_voice_call.close() 
    print("autoAnalyzer_for_voice_call done!") #current_networks
def autoAnalyzer_for_current_networks(given_name):
    if ('png' in given_name) : return
    if ('dumpstate_debug_history.lst' in given_name) : return
    if ('dumpstate_log.txt' in given_name) : return
    if ('dumpstate-stats.txt' in given_name) : return

    f_analysis_current_networks =  open(given_name + "_wg_current_networks", 'w')
    f_ori = open("./" + given_name, 'r')
    while True:
        line = f_ori.readline()
        if not line: break

        if ('Active default network' in line):
            f_analysis_current_networks.write(line.strip() + '\n')

        elif ('Current Networks:' in line):
            f_analysis_current_networks.write('\n')
            f_analysis_current_networks.write(line.strip() + '\n')
            while True:
                line = f_ori.readline()
                if not line == '\n':
                    f_analysis_current_networks.write(line.strip() + '\n')
                else:
                    break
        elif ('default network events:' in line):
            f_analysis_current_networks.write('\n')
            f_analysis_current_networks.write(line.strip() + '\n')
            while True:
                line = f_ori.readline()
                if not line == '\n':
                    f_analysis_current_networks.write(line.strip() + '\n')
                else:
                    break

    f_analysis_current_networks.close()
    print("autoAnalyzer_for_current_networks done!")

#dds
def autoAnalyzer_for_dds(given_name):
    if ('png' in given_name) : return
    if ('dumpstate_debug_history.lst' in given_name) : return
    if ('dumpstate_log.txt' in given_name) : return
    if ('dumpstate-stats.txt' in given_name) : return

    f_analysis_dds =  open(given_name + "_wg_dds", 'w')
    f_ori = open("./" + given_name, 'r')
    while True:
        line = f_ori.readline()
        if not line: break

        if ('DefaultPhoneNotifier: subId' in line):
            f_analysis_dds.write(line.strip() + '\n')
        elif ('default data subscription change ' in line):
            f_analysis_dds.write(line.strip() + '\n')
        elif ('SubscriptionController:' in line):
            f_analysis_dds.write(line.strip() + '\n')
        elif ('- DDS change success' in line):
            f_analysis_dds.write(line.strip() + '\n')

    f_analysis_dds.close()
    print("autoAnalyzer_for_dds done!")

#fatal
def autoAnalyzer_for_fatal(given_name):
    if ('png' in given_name) : return
    if ('dumpstate_debug_history.lst' in given_name) : return
    if ('dumpstate_log.txt' in given_name) : return
    if ('dumpstate-stats.txt' in given_name) : return

#java.lang.Exception
#Permission denied
#java.io.FileNotFoundException
    f_analysis_fatal=  open(given_name + "_wg_fatal", 'w')
    f_ori = open("./" + given_name, 'r')
    while True:
        line = f_ori.readline()
        if not line: break

        if ('Fatal signal' in line):
            f_analysis_fatal.write(line.strip() + '\n')
        elif ('System.err: ' in line):
            f_analysis_fatal.write(line.strip() + '\n')
        elif ('java.lang.Exception' in line):
            f_analysis_fatal.write(line.strip() + '\n')
        elif ('Permission denied' in line):
            f_analysis_fatal.write(line.strip() + '\n')
        elif ('java.io.FileNotFoundException' in line):
            f_analysis_fatal.write(line.strip() + '\n')
        elif ('FATAL EXCEPTION' in line):
            f_analysis_fatal.write(line.strip() + '\n')
        elif ('AndroidRuntime: java.lang.NullPointerException' in line):
            f_analysis_fatal.write(line.strip() + '\n')
        elif ('AndroidRuntime: Process: com.android.' in line):
            f_analysis_fatal.write(line.strip() + '\n')
        elif ('--------- beginning of crash' in line):
            f_analysis_fatal.write(line.strip() + '\n')
        elif ('AndroidRuntime: Process:' in line):
            f_analysis_fatal.write(line.strip() + '\n')
        elif ('DEBUG   : backtrace:' in line):
            f_analysis_fatal.write(line.strip() + '\n')
        elif ('DEBUG   : signal' in line):
            f_analysis_fatal.write(line.strip() + '\n')


    f_analysis_fatal.close()
    print("autoAnalyzer_for_fatal done!")

#apm
def autoAnalyzer_for_apm(given_name):
    if ('png' in given_name) : return
    if ('dumpstate_debug_history.lst' in given_name) : return
    if ('dumpstate_log.txt' in given_name) : return
    if ('dumpstate-stats.txt' in given_name) : return

    f_analysis_apm=  open(given_name + "_wg_apm", 'w')
    f_ori = open("./" + given_name, 'r')
    while True:
        line = f_ori.readline()
        if not line: break

        if ('FlightMode' in line):
            f_analysis_apm.write(line.strip() + '\n')
        elif ('setRadioPower - power:' in line):
            f_analysis_apm.write(line.strip() + '\n')
        elif ('PhoneGlobals: Turning radio' in line):
            f_analysis_apm.write(line.strip() + '\n')
        elif ('> RADIO_POWER on =' in line):
            f_analysis_apm.write(line.strip() + '\n')
        elif ('Boot_SVC : setRadioPower' in line):
            f_analysis_apm.write(line.strip() + '\n')


    f_analysis_apm.close()
    print("autoAnalyzer_for_apm done!")

#deactivate_data_call
def autoAnalyzer_for_deactivate_data_call(given_name):
    if ('png' in given_name) : return
    if ('dumpstate_debug_history.lst' in given_name) : return
    if ('dumpstate_log.txt' in given_name) : return
    if ('dumpstate-stats.txt' in given_name) : return

    #name_strings = given_name.split('_'); 
    #name = name_strings[2];

    #f_analysis_deactivate_data_call=  open(name[0:12] + "_wg_deactivate", 'w')
    f_analysis_deactivate_data_call=  open(given_name + "_wg_deactivate", 'w')
    f_ori = open("./" + given_name, 'r')
    while True:
        line = f_ori.readline()
        if not line: break

        if ('DEACTIVATE_DATA_CALL' in line):
            f_analysis_deactivate_data_call.write(line.strip() + '\n')
        elif ('OnDataCallDisconnected' in line):
            f_analysis_deactivate_data_call.write(line.strip() + '\n')
        elif ('DDS-DcTracker.releaseNetwork for NetworkRequest' in line):
            f_analysis_deactivate_data_call.write(line.strip() + '\n')
        elif ('- cleanUpConnectionInternal: detach=' in line):
            f_analysis_deactivate_data_call.write(line.strip() + '\n')
        elif ('] validation failed' in line):
            f_analysis_deactivate_data_call.write(line.strip() + '\n')
        elif ('PdnController: mDefaultNetworkListener: onLost' in line):
            f_analysis_deactivate_data_call.write(line.strip() + '\n')
        elif ('NetworkAgent channel lost' in line):
            f_analysis_deactivate_data_call.write(line.strip() + '\n')
        elif ('Data call end reason(' in line):
            f_analysis_deactivate_data_call.write(line.strip() + '\n')
        elif ('OnDataCallDisconnected:' in line):
            f_analysis_deactivate_data_call.write(line.strip() + '\n')
        elif ('onSimStateUpdated: state=' in line):
            f_analysis_deactivate_data_call.write(line.strip() + '\n')
        elif ('cleanUpAllConnectionsInternal:' in line):
            f_analysis_deactivate_data_call.write(line.strip() + '\n')
        elif ('SimManager: mSimState:ABSENT' in line):
            f_analysis_deactivate_data_call.write(line.strip() + '\n')
        elif ('onDataStateChanged: send EVENT_LOST_CONNECTION' in line):
            f_analysis_deactivate_data_call.write(line.strip() + '\n')
        elif ('DcActiveState EVENT_LOST_CONNECTION dc=' in line):
            f_analysis_deactivate_data_call.write(line.strip() + '\n')
        elif ('EVENT_DISCONNECT_DONE msg=' in line):
            f_analysis_deactivate_data_call.write(line.strip() + '\n')
        elif ('Unregister from connectivity service' in line):
            f_analysis_deactivate_data_call.write(line.strip() + '\n')
        elif ('released the ownership' in line):
            f_analysis_deactivate_data_call.write(line.strip() + '\n')
        elif ('onDataStateChanged: addr change, cleanup apns' in line):
            f_analysis_deactivate_data_call.write(line.strip() + '\n')
        elif (': tearDownData. mCid=' in line):
            f_analysis_deactivate_data_call.write(line.strip() + '\n')
        elif (': deactivateDataCall' in line):
            f_analysis_deactivate_data_call.write(line.strip() + '\n')
        elif ('updateLinkProperty old LP=' in line):
            f_analysis_deactivate_data_call.write(line.strip() + '\n')
        elif ('updateLinkProperty new LP' in line):
            f_analysis_deactivate_data_call.write(line.strip() + '\n')
        elif ('stopPdnConnectivity' in line):
            f_analysis_deactivate_data_call.write(line.strip() + '\n')
        elif ('DcActiveState EVENT_DISCONNECT' in line):
            f_analysis_deactivate_data_call.write(line.strip() + '\n')
        elif ('EVENT_LOST_CONNECTION' in line):
            f_analysis_deactivate_data_call.write(line.strip() + '\n')
    f_analysis_deactivate_data_call.close()
    print("autoAnalyzer_for_deactivate_data_call done!")

#local_log
def autoAnalyzer_for_local_log(given_name):
    if ('png' in given_name) : return
    if ('dumpstate_debug_history.lst' in given_name) : return
    if ('dumpstate_log.txt' in given_name) : return
    if ('dumpstate-stats.txt' in given_name) : return

    #Local log: count this  context
    Local_log_count = 0

    f_analysis_local_log=  open(given_name + "_wg_local_log", 'w')
    f_ori = open("./" + given_name, 'r')
    while True:
        line = f_ori.readline()
        if not line: break

        if ('Local log:' in line):
            Local_log_count += 1
            if Local_log_count == 7 :
                f_analysis_local_log.write('vimgrep /onSetupConnectionCompleted\|onEnableApn\|onDisableApn/ % | cw' + '\n')
                f_analysis_local_log.write(line.strip() + '\n')
                while True:
                    line = f_ori.readline()
                    if 'Phone Local Log:' in line:
                        break;
                    else:
                        f_analysis_local_log.write(line.strip() + '\n')

    f_analysis_local_log.close()
    print("autoAnalyzer_for_local_log done!")

#
def autoAnalyzer_for_mtu(given_name):
    if ('png' in given_name) : return
    if ('dumpstate_debug_history.lst' in given_name) : return
    if ('dumpstate_log.txt' in given_name) : return
    if ('dumpstate-stats.txt' in given_name) : return

    f_analysis_mtu=  open(given_name + "_wg_mtu", 'w')
    f_ori = open("./" + given_name, 'r')
    while True:
        line = f_ori.readline()
        if not line: break

        if ('mtu' in line):
            f_analysis_mtu.write(line.strip() + '\n')
        elif ('updatemtu' in line):
            f_analysis_mtu.write(line.strip() + '\n')

    f_analysis_mtu.close()

    print("autoAnalyzer_for_mtu done!")

#ril_request
def autoAnalyzer_for_ril_request(given_name):
    if ('png' in given_name) : return
    if ('dumpstate_debug_history.lst' in given_name) : return
    if ('dumpstate_log.txt' in given_name) : return
    if ('dumpstate-stats.txt' in given_name) : return

    f_analysis_ril_request=  open(given_name + "_wg_ril_request", 'w')
    f_ori = open("./" + given_name, 'r')
    while True:
        line = f_ori.readline()
        if not line: break

        if ('RIL_REQUEST_' in line):
            f_analysis_ril_request.write(line.strip() + '\n')
        elif ('UNSOL_' in line):
            f_analysis_ril_request.write(line.strip() + '\n')

    f_analysis_ril_request.close()
    print("autoAnalyzer_for_ril_request done!")

#applynewstate
def autoAnalyzer_for_applynewstate(given_name):
    if ('png' in given_name) : return
    if ('dumpstate_debug_history.lst' in given_name) : return
    if ('dumpstate_log.txt' in given_name) : return
    if ('dumpstate-stats.txt' in given_name) : return

    f_analysis_applynewstate = open(given_name + "_wg_applynewstate", 'w')
    f_ori = open("./" + given_name, 'r')

    while True:
        line = f_ori.readline()
        if not line: break

        if ('applyNewState(' in line):
            f_analysis_applynewstate.write(line.strip() + '\n')

    f_analysis_applynewstate.close()
    print("autoAnalyzer_for_applynewstate done!")

#firewall
def autoAnalyzer_for_firewall(given_name):
    if ('png' in given_name) : return
    if ('dumpstate_debug_history.lst' in given_name) : return
    if ('dumpstate_log.txt' in given_name) : return
    if ('dumpstate-stats.txt' in given_name) : return

    f_analysis_firewall = open(given_name + "_wg_firewall", 'w')

    f_ori = open("./" + given_name, 'r')

    while True:
        line = f_ori.readline()
        if not line: break

        elif ('firewallSetUidRule' in line):
            f_analysis_firewall.write(line.strip() + '\n')
        elif ('FreecessController: FZ' in line):
            f_analysis_firewall.write(line.strip() + '\n')
        elif ('firewallSetUidRule' in line):
            f_analysis_firewall.write(line.strip() + '\n')
        elif ('FreecessController: FZ' in line):
            f_analysis_firewall.write(line.strip() + '\n')

    f_analysis_firewall.close()

    print("autoAnalyzer_for_firewall done!")

#conn
def autoAnalyzer_for_conn(given_name):
    if ('png' in given_name) : return
    if ('dumpstate_debug_history.lst' in given_name) : return
    if ('dumpstate_log.txt' in given_name) : return
    if ('dumpstate-stats.txt' in given_name) : return

    f_analysis_conn = open(given_name + "_wg_conn", 'w')

    f_ori = open("./" + given_name, 'r')
    while True:
        line = f_ori.readline()
        if not line: break

        if ('ConnectivityService: filterNetworkStateForUid() uid:' in line):
            f_analysis_conn.write(line.strip() + '\n')

    f_analysis_conn.close()

    print("autoAnalyzer_for_conn done!")

#ril_qmi_rild_DC-C
def autoAnalyzer_for_ril_qmi_rild_dc(given_name):
    if ('png' in given_name) : return
    if ('dumpstate_debug_history.lst' in given_name) : return
    if ('dumpstate_log.txt' in given_name) : return
    if ('dumpstate-stats.txt' in given_name) : return

    f_analysis_ril_qmi_rild_dc= open(given_name + "_wg_ril_qmi_rild_dc", 'w')
    f_ori = open("./" + given_name, 'r')
    while True:
        line = f_ori.readline()
        if not line: break

        if ('RIL-QMI :' in line):
            f_analysis_ril_qmi_rild_dc.write(line.strip() + '\n')
        elif ('RILD :' in line):
            f_analysis_ril_qmi_rild_dc.write(line.strip() + '\n')
        elif ('DC-C-' in line):
            f_analysis_ril_qmi_rild_dc.write(line.strip() + '\n')

    f_analysis_ril_qmi_rild_dc.close()
    print("autoAnalyzer_for_ril_qmi_rild_dc done!")


#ril_qmi
def autoAnalyzer_for_ril_qmi(given_name):
    if ('png' in given_name) : return
    if ('dumpstate_debug_history.lst' in given_name) : return
    if ('dumpstate_log.txt' in given_name) : return
    if ('dumpstate-stats.txt' in given_name) : return

    f_analysis_ril_qmi= open(given_name + "_wg_ril_qmi", 'w')
    f_ori = open("./" + given_name, 'r')
    while True:
        line = f_ori.readline()
        if not line: break

        if ('QMI_WDS_PKT_SRVC_STATUS' in line):
            f_analysis_ril_qmi.write(line.strip() + '\n')
        elif ('Data call end reason' in line):
            f_analysis_ril_qmi.write(line.strip() + '\n')
        elif ('by network disconnect' in line):
            f_analysis_ril_qmi.write(line.strip() + '\n')
        elif ('Toast   : Text' in line):
            f_analysis_ril_qmi.write(line.strip() + '\n')
        elif (': SendMessage: svc' in line):
            f_analysis_ril_qmi.write(line.strip() + '\n')
        elif (': ReceiveMessage: svc' in line):
            f_analysis_ril_qmi.write(line.strip() + '\n')

    f_analysis_ril_qmi.close()
    print("autoAnalyzer_for_ril_qmi done!")

#mAllApnSettings
def autoAnalyzer_for_mAllApnSettings(given_name):
    if ('png' in given_name) : return
    if ('dumpstate_debug_history.lst' in given_name) : return
    if ('dumpstate_log.txt' in given_name) : return
    if ('dumpstate-stats.txt' in given_name) : return

    f_analysis_mallapnsettings = open(given_name + "_wg_mallapnsettings" , 'w')
    f_ori = open("./" + given_name, 'r')
    while True:
        line = f_ori.readline()
        if not line: break

        if ('mAllApnSettings size=' in line):
            f_analysis_mallapnsettings.write('\n')
            f_analysis_mallapnsettings.write(line.strip() + '\n')
        elif ('mAllApnSettings[' in line) :
            f_analysis_mallapnsettings.write(line.strip() + '\n')
        elif ('user_editable' in line) :
            f_analysis_mallapnsettings.write('\n')
            f_analysis_mallapnsettings.write(line.strip() + '\n')
        elif ('mAllApnSettings[' in line) :
            f_analysis_mallapnsettings.write(line.strip() + '\n')
        elif ('carrier_metered_apn_types_strings' in line) :
            f_analysis_mallapnsettings.write(line.strip() + '\n')

    f_analysis_mallapnsettings.close()

    print("autoAnalyzer_for_mAllApnSettings done!")

#Trigger all!
def autoAnalyzer(given_name):
    autoAnalyzer_for_mAllApnSettings(given_name)
    autoAnalyzer_for_setup_data_call(given_name)
    autoAnalyzer_for_regi(given_name)
    autoAnalyzer_for_ground(given_name)
    autoAnalyzer_for_stall(given_name)
    autoAnalyzer_for_roaming(given_name)
    autoAnalyzer_for_dns(given_name)
    #autoAnalyzer_for_data_activity(given_name)
    autoAnalyzer_for_monitor(given_name)
    autoAnalyzer_for_secril(given_name)
    autoAnalyzer_for_monitor2(given_name)
    #autoAnalyzer_for_voice_call(given_name)
    #autoAnalyzer_for_current_networks(given_name)
    autoAnalyzer_for_dds(given_name)
    autoAnalyzer_for_fatal(given_name)
    autoAnalyzer_for_apm(given_name)
    autoAnalyzer_for_deactivate_data_call(given_name)
    #autoAnalyzer_for_local_log(given_name)
    autoAnalyzer_for_ril_request(given_name)
    autoAnalyzer_for_applynewstate(given_name)
    autoAnalyzer_for_firewall(given_name)
    autoAnalyzer_for_conn(given_name)
    autoAnalyzer_for_ril_qmi(given_name)
    autoAnalyzer_for_network_request(given_name)
    autoAnalyzer_for_mms(given_name)
    autoAnalyzer_for_block(given_name)
    autoAnalyzer_for_cpreset(given_name)
    autoAnalyzer_for_ril_qmi_rild_dc(given_name)
    autoAnalyzer_for_dct(given_name)
    autoAnalyzer_for_dnc(given_name)
    autoAnalyzer_for_rild(given_name)
    autoAnalyzer_for_gprs(given_name)
    autoAnalyzer_for_cs(given_name)
    autoAnalyzer_for_request_dct_cs(given_name)
    autoAnalyzer_for_switch_sim(given_name)
    autoAnalyzer_for_signalcontroller(given_name)
    autoAnalyzer_for_broadcasting_from_sst(given_name)
    autoAnalyzer_for_pdn_open(given_name)
    autoAnalyzer_for_simmanager(given_name)
    autoAnalyzer_for_booting(given_name)
    autoAnalyzer_for_attach(given_name)
    autoAnalyzer_for_fc(given_name)
    autoAnalyzer_for_json(given_name)
    autoAnalyzer_for_epdg(given_name)
    autoAnalyzer_for_setting(given_name)
    autoAnalyzer_for_mtu(given_name)



    print("autoAnalyze done!")

def search(dirname):
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename) :
                search(full_filename)
            else :
                if ('dumpState' in filename and 'zip' not in filename and 'UHM' not in filename and 'FOTA' not in filename and 'Water_' not in filename and 'SAP' not in filename) :
                    if ('MP' in filename) :
                        print('mp in : ' + filename)
                        break;
                    else :
                        print('mp not in : ' + filename)
                        print(filename)
                        if ( '(' in filename) :
                            startIndex = filename.find("(")
                            endIndex = filename.find(")")
                            name_len = len(filename)
                            new_filename = filename.replace(filename, filename[0:startIndex] + filename[endIndex+1:name_len])
                            print("filename : " + filename)
                            os.rename(os.path.join(dirname, filename), os.path.join(dirname, new_filename))
                            print("rename done :" + new_filename)
                            autoAnalyzer(os.path.join(dirname, new_filename))
                        elif ('_wg_' not in filename and 'zip' not in filename) :
                            autoAnalyzer(os.path.join(dirname, filename))
                elif (p4.match(filename)) : #'.*logcat.*radio.*'
                    print(filename)
                    if ( '(' in filename) :
                        startIndex = filename.find("(")
                        endIndex = filename.find(")")
                        name_len = len(filename)
                        new_filename = filename.replace(filename, filename[0:startIndex] + filename[endIndex+1:name_len])
                        print("filename : " + filename)
                        os.rename(os.path.join(dirname, filename), os.path.join(dirname, new_filename))
                        print("rename done :" + new_filename)
                        autoAnalyzer(os.path.join(dirname, new_filename))
                    elif ('_wg_' not in filename and 'zip' not in filename) :
                        autoAnalyzer(os.path.join(dirname, filename))
                elif (p5.match(filename)) : #'.*logcat.*main.*'
                    print(filename)
                    if ( '(' in filename) :
                        startIndex = filename.find("(")
                        endIndex = filename.find(")")
                        name_len = len(filename)
                        new_filename = filename.replace(filename, filename[0:startIndex] + filename[endIndex+1:name_len])
                        print("filename : " + filename)
                        os.rename(os.path.join(dirname, filename), os.path.join(dirname, new_filename))
                        print("rename done :" + new_filename)
                        autoAnalyzer(os.path.join(dirname, new_filename))
                    elif ('_wg_' not in filename and 'zip' not in filename) :
                        autoAnalyzer(os.path.join(dirname, filename))
                elif (p6.match(filename)) : #'.*main_log.*'
                    print(filename)
                    if ( '(' in filename) :
                        startIndex = filename.find("(")
                        endIndex = filename.find(")")
                        name_len = len(filename)
                        new_filename = filename.replace(filename, filename[0:startIndex] + filename[endIndex+1:name_len])
                        print("filename : " + filename)
                        os.rename(os.path.join(dirname, filename), os.path.join(dirname, new_filename))
                        print("rename done :" + new_filename)
                        autoAnalyzer(os.path.join(dirname, new_filename))
                    elif ('_wg_' not in filename and 'zip' not in filename) :
                        autoAnalyzer(os.path.join(dirname, filename))
                elif (p7.match(filename)) : #'.*radio_log.*'
                    print(filename)
                    if ( '(' in filename) :
                        startIndex = filename.find("(")
                        endIndex = filename.find(")")
                        name_len = len(filename)
                        new_filename = filename.replace(filename, filename[0:startIndex] + filename[endIndex+1:name_len])
                        print("filename : " + filename)
                        os.rename(os.path.join(dirname, filename), os.path.join(dirname, new_filename))
                        print("rename done :" + new_filename)
                        autoAnalyzer(os.path.join(dirname, new_filename))
                    elif ('_wg_' not in filename and 'zip' not in filename) :
                        autoAnalyzer(os.path.join(dirname, filename))
                elif (p8.match(filename)) : # #200702_15-11-45.log, ('^\d{6}.*-\d{2}.*-\d{2}')
                    print(filename)
                    if ( '(' in filename) :
                        startIndex = filename.find("(")
                        endIndex = filename.find(")")
                        name_len = len(filename)
                        new_filename = filename.replace(filename, filename[0:startIndex] + filename[endIndex+1:name_len])
                        print("filename : " + filename)
                        os.rename(os.path.join(dirname, filename), os.path.join(dirname, new_filename))
                        print("rename done :" + new_filename)
                        autoAnalyzer(os.path.join(dirname, new_filename))
                    elif ('_wg_' not in filename and 'pcap' not in filename) :
                        autoAnalyzer(os.path.join(dirname, filename))
                elif ('act_dumpstate' in filename) :
                    print(filename)
                    if ( '(' in filename) :
                        startIndex = filename.find("(")
                        endIndex = filename.find(")")
                        name_len = len(filename)
                        new_filename = filename.replace(filename, filename[0:startIndex] + filename[endIndex+1:name_len])
                        print("filename : " + filename)
                        os.rename(os.path.join(dirname, filename), os.path.join(dirname, new_filename))
                        print("rename done :" + new_filename)
                        autoAnalyzer(os.path.join(dirname, new_filename))
                    elif ('_wg_' not in filename and 'zip' not in filename) :
                        autoAnalyzer(os.path.join(dirname, filename))
                elif ('dumpstate' in filename and 'MP' not in filename and 'lastkmsg' not in filename) :
                    print(filename)
                    if ( '(' in filename) :
                        startIndex = filename.find("(")
                        endIndex = filename.find(")")
                        name_len = len(filename)
                        new_filename = filename.replace(filename, filename[0:startIndex] + filename[endIndex+1:name_len])
                        print("filename : " + filename)
                        os.rename(os.path.join(dirname, filename), os.path.join(dirname, new_filename))
                        print("rename done :" + new_filename)
                        autoAnalyzer(os.path.join(dirname, new_filename))
                    elif ('_wg_' not in filename and 'zip' not in filename) :
                        autoAnalyzer(os.path.join(dirname, filename))


def deleteall(dirname):
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        if os.path.isdir(full_filename) :
            deleteall(full_filename)
        else :
            if ('_wg_' in filename) :
                os.remove(full_filename)
                print("delte pre-exist files")

def moveAll(dirname):
    filenames = os.listdir(dirname)

#main
deleteall("./")
search("./")


