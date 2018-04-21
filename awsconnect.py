import requests
import json
import pprint
from timeit import default_timer as timer


def call_api_gateway():
    data = {
    }

    headers = {
        'x-api-key': 'PlexopExamAPIkey1PlexopExamAPIkey1 '
    }

    thekey="x-api-key=PlexopExamAPIkey1PlexopExamAPIkey1 "

    base_url = 'https://9zrfwd2w7a.execute-api.us-east-1.amazonaws.com'
    resource_path1 = '/dev/funnels'
    resource_path2 = '/dev/funnels/enums'
    url = '{}{}'.format(base_url, resource_path1)
    #print(url)
    start=timer()
    r = requests.get(url, headers=headers)
    end=timer()
    print("Get time is {}:".format(end-start))
    data_item1=json.loads(r.text.decode("utf-8"))
    #print(data_item1)
    for aha in data_item1:
	print(aha['funnel_id'])
    print("==================================================")
    url = '{}{}'.format(base_url, resource_path2)
    print(url)
    r = requests.get(url, headers=headers)
    data_item2=json.loads(r.text.decode("utf-8"))
    print(data_item2)
    print(data_item2['severity_levels'][1]['name'])


if __name__ == '__main__':
    call_api_gateway()
