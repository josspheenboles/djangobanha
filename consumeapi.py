#pip install requests
import requests
#endpoint
endpoint='http://localhost:8000/Track/all/'

#add php track
d={'name':'php'}
res=requests.post(endpoint,data=d)
print(res.status_code)

#method get


respon=requests.get(endpoint)
print(respon.status_code,type(respon.status_code))
if(respon.status_code==200):
    for track in respon.json()['tracks']:
        print(track)
        # print(f'ID:{{track["id"}},Name:{{track["name"]}}')
else:
    print('invalid endijtn')

