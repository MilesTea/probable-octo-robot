import requests
import time
from pprint import pprint


class StackOverflow:    # класс был сделан для возможного расширения программы (по примеру 2 задачи)

    def get_questions(self, tag):
        questions_title = dict()
        questions_link = dict()
        time_now = int(time.time())
        time_two_days_ago = time_now - 172800
        has_more = True
        page = 1
        questions_number = 1

        while has_more:
            params = {
                'fromdate': time_two_days_ago,
                'todate': time_now,
                'order': 'desc',
                'sort': 'creation',
                'site': 'stackoverflow',
                'tagged': tag,
                'pagesize': 100,
                'page': page
            }

            page += 1
            response = requests.get(url='https://api.stackexchange.com/2.3/questions', params=params)
            has_more = response.json()['has_more']

            if len(response.json()['items']) == 0:
                print('Not Found')
                break

            max_title_length = 0
            for question in response.json()['items']:
                link = question['link']
                title = question['title']
                questions_title[questions_number] = title
                questions_link[questions_number] = link
                questions_number += 1
                if max_title_length < len(title):
                    max_title_length = len(title)

        for question in questions_title:
            print(questions_title[question].ljust(max_title_length+1), questions_link[question])


if __name__ == '__main__':
    test = StackOverflow()
    test.get_questions('python')
