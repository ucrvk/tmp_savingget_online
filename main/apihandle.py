from httpx import get, post, Cookies
import urllib.request
from wx import Image
from io import BytesIO
from datetime import datetime

cookie = Cookies()
WEB_URL = "https://api.wenwen12305.top"


def get_activity():
    url = f"{WEB_URL}/activity/"
    try:
        response = post(url, data={"username": "test", "password": "test"})
        if response.status_code == 403:
            return str(response.content)
        elif response.status_code != 200:
            return "未知服务器端错误"
        else:
            global cookie
            cookie = response.cookies
            return response.json()
    except Exception as e:
        return f"请求出错: {e}"


def get_saving():
    url = f"{WEB_URL}/download_saving/"
    try:
        response = get(url, cookies=cookie)
        if response.status_code == 403:
            return str(response.content)
        elif response.status_code != 200:
            return response.content
        else:
            with open("saving.zip", "wb") as fi:
                fi.write(response.content)
            return True
    except Exception as e:
        return f"请求出错: {e}"


def photoFileGet(url: str):
    image_data = BytesIO(urllib.request.urlopen(url).read())
    image = Image(image_data)
    return image


def compare_to_datetime(target_datetime_tuple: tuple):
    # 比较时间是否在目标时间范围内,输入为(开始时间,结束时间)
    start_datetime = datetime.strptime(target_datetime_tuple[0], "%Y-%m-%d %H:%M:%S")
    end_datetime = datetime.strptime(target_datetime_tuple[1], "%Y-%m-%d %H:%M:%S")
    current_datetime = datetime.now()
    if current_datetime >= start_datetime and current_datetime <= end_datetime:
        return True
    else:
        return False


if __name__ == "__main__":
    print(get_activity())
