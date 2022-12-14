import asyncio
import json
import aiohttp as aiohttp
import os
from dotenv import load_dotenv

load_dotenv()

my_token = os.getenv('TOKEN')
incorrect_msgs = []


async def send_msg(session, data):
    headers = {'accept': 'application/json',
               'Authorization': f'Bearer {my_token}',
               'Content-Type': 'application/json'
               }

    url = f"https://probe.fbrq.cloud/v1/send/{data['id']}"

    async with session.post(url=url, headers=headers, data=json.dumps(data)) as response:
        response_status = await response.text()
        if response.ok:
            pass
        else:
            incorrect_msgs.append(data)


async def sending_msgs():
    # timeout = aiohttp.ClientTimeout(sock_read=None)
    # sending_list = []
    # clients_list = []
    data_list = []
    async with aiohttp.ClientSession() as session:
        headers = {'Content-Type': 'application/json'}
        sending_url = f"http://127.0.0.1:8000/api/sending/active/"
        async with session.get(url=sending_url, headers=headers) as response:
            response = await response.text()
            sending_list = json.loads(response)
        for sending in sending_list:
            clients_url = f"http://127.0.0.1:8000/api/sending/{sending['id']}/clients/"
            async with session.get(url=clients_url, headers=headers) as response:
                response = await response.text()
                clients_list = json.loads(response)
                data_list.append()

        tasks = []
        for data in data_list:
            task = asyncio.create_task(send_msg(session, data))
            tasks.append(task)

        await asyncio.gather(*tasks)


# async def send_status(session, data):
#     headers = {
#                'Content-Type': 'application/json'
#                }
#
#     url = f"http://127.0.0.1:8000/api/message/{data['id']}"
#
#     async with session.post(url=url, headers=headers, data=json.dumps(data)) as response:
#         response_status = await response.text()
#         print(f'{data["id"]}:\n{response_status}\n{response.status}')
#         if response.ok:
#             pass
#         else:
#             incorrect_msgs.append(data)


# async def sending_status(data_list):
#     async with aiohttp.ClientSession() as session:
#         tasks = []
#         for data in data_list:
#             task = asyncio.create_task(send_msg(session, data))
#             tasks.append(task)
#
#         await asyncio.gather(*tasks)


def main():
    """
    id = models.BigIntegerField(primary_key=True)
    sending_start = models.DateTimeField()
    text = models.TextField()
    sending_end
    """
    incoming_data = [{"id": x, "phone": 0, "text": "string"} for x in range(1, 50)]
    data_list = incoming_data
    while data_list:
        asyncio.run(sending_msgs())
        if incorrect_msgs:
            data_list = incorrect_msgs
        else:
            print('???????????? ??????????')
            break


if __name__ == "__main__":
    main()
