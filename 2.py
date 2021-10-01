import requests


class YaUploader:
    def __init__(self,token):
        self.token = token

    def get_headers(self):
        headers = {
            'Authorization': f'OAuth {self.token}'
        }
        return headers

    def get_upload_link(self, disk_file_path):
        headers = self.get_headers()
        params = {
            'path': disk_file_path,
            'overwrite': 'true'
        }
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        response = requests.get(url=url, headers=headers, params=params, timeout=5)
        return response.json()

    def upload(self, path):
        spl = path.split('/')
        if len(spl) == 1:
            spl = path.split('\\')
            path = ('/').join(spl)
        file_name = spl[-1]
        href = self.get_upload_link(disk_file_path=file_name).get('href')
        with open(path, 'rb') as file:
            response = requests.put(url=href, data=file)
        print(f'Status code: {response.status_code}')
        return response.status_code


if __name__ == '__main__':
    path_to_file = ''
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
    print(result)