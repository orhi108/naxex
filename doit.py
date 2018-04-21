import requests
import json
from timeit import default_timer as timer
from flask import Flask
from collections import OrderedDict


app = Flask(__name__)



def call_api_gateway1():
    headers = {
        'x-api-key': 'PlexopExamAPIkey1PlexopExamAPIkey1 '
    }

    thekey="x-api-key=PlexopExamAPIkey1PlexopExamAPIkey1 "

    base_url = 'https://9zrfwd2w7a.execute-api.us-east-1.amazonaws.com'
    resource_path1 = '/dev/funnels'
    resource_path2 = '/dev/funnels/enums'
    url = '{}{}'.format(base_url, resource_path1)
    start=timer()
    r = requests.get(url, headers=headers)
    end=timer()
    print("Get1 time is {} s".format(end-start)) 
    data_item1=json.loads(r.text)
    url = '{}{}'.format(base_url, resource_path2)
    start=timer()
    r = requests.get(url, headers=headers)
    end=timer()
    print("Get2 time is {} s".format(end-start))
    data_item2=json.loads(r.text)
    updatedlist=[]
    for index, funnel in enumerate(data_item1):
        zone_type_id=funnel['extended_info']['zone_type_id']
        for zt in data_item2['zone_types']:
             if zt['id'] == zone_type_id:
                  data_item1[index]['extended_info']['zone_type_name']=zt['name']
        for index2, alerts in enumerate(funnel['alerts']):
            alert_type_id=alerts['alert_type_id']
            for at in data_item2['alert_types']:
                if at['id'] == alert_type_id:
                    data_item1[index]['alerts'][index2]['alert_name']=at['name'] 
            snooze_reason_id=alerts['snooze_reason_id']
            for sr in data_item2['snooze_reasons']:
                if sr['id'] == snooze_reason_id:
                    data_item1[index]['alerts'][index2]['snooze_reason_name']=sr['name']
            alert_category_id=alerts['alert_category_id']
            for ac in data_item2['alert_categories']:
                 if ac['id'] == alert_category_id:
                     data_item1[index]['alerts'][index2]['alert_category_name']=ac['name']
            severity_level_id=alerts['severity_level_id']
            for sl in data_item2['severity_levels']:
                 if sl['id'] == severity_level_id:
                     data_item1[index]['alerts'][index2]['severity_level_name']=sl['name'] 
    json_format=json.dumps(data_item1, sort_keys=True, indent=4, separators=(',', ': '))
    print(json_format)
    return json_format


def call_api_gateway2():
    headers = {
        'x-api-key': 'PlexopExamAPIkey1PlexopExamAPIkey1 '
    }

    thekey="x-api-key=PlexopExamAPIkey1PlexopExamAPIkey1 "

    base_url = 'https://9zrfwd2w7a.execute-api.us-east-1.amazonaws.com'
    resource_path1 = '/dev/funnels'
    url = '{}{}'.format(base_url, resource_path1)
    start=timer()
    r = requests.get(url, headers=headers)
    end=timer()
    print("Get1 time is {} s".format(end-start))
    data_item1=json.loads(r.text)
    for index, funnel in enumerate(data_item1):
        number_of_alerts=0
        number_of_snoozed_alerts=0
        exposure_sum=0
        max_exposure_alert_id=0
        max_exposure=0
        for index2, alerts in enumerate(funnel['alerts']):
            number_of_alerts+=1
            if alerts['is_snoozed'] == True:
                number_of_snoozed_alerts+=1
            exp=alerts['exposure']
            exposure_sum+=exp
            if exp >  max_exposure:
                max_exposure_alert_id=alerts['alert_id']
            data_item1[index]['number_of_alerts']=number_of_alerts
            data_item1[index]['number_of_snoozed_alerts']=number_of_snoozed_alerts
            data_item1[index]['exposure_sum']=exposure_sum
            data_item1[index]['max_exposure_alert_id']=max_exposure_alert_id
        del data_item1[index]['alerts']
        del data_item1[index]['actions_history']
        for exi_key, exi_val in data_item1[index]['extended_info'].items():
            data_item1[index][exi_key]=exi_val
        del data_item1[index]['extended_info']
#o    res = OrderedDict(sorted(data_item1.items(), key=lambda x: x[1]['exposure_sum'], reverse=True))
#    sort_on='exposure_sum'
#    sortedlist= [(dict_[sort_on], dict_) for dict_ in data_item1]
#    print (sortedlist)
#    sortedlist.sort()
#    result = [dict_ for (key, dict_) in sortedlist]
    data_sorted = sorted(data_item1, key=lambda item: item['exposure_sum'], reverse=True)
    json_format=json.dumps(data_sorted, sort_keys=True, indent=4, separators=(',', ': '))
    print(json_format)
    return json_format




@app.route("/funnels")
def funnels():
    start1=timer()
    returnmsg=call_api_gateway1()
    end1=timer()
    print("Process time is {} s".format(end1-start1))
    return returnmsg



@app.route("/funnels/summary")
def funnels_summary():
    start1=timer()
    returnmsg=call_api_gateway2()
    end1=timer()
    print("Process time is {} s".format(end1-start1))
    return returnmsg
