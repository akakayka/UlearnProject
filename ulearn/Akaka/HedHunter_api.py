import re
import requests

class HH_api:

    @staticmethod
    def get_full_vacancies(date, count_vac):
        url = 'https://api.hh.ru/vacancies'
        data = requests.get(url, dict(text="1С",
                                      specialization=1,
                                      date_from=f"{date}T00:00:00",
                                      date_to=f"{date}T23:00:00",
                                      per_page=count_vac,
                                      page=1)).json()["items"]
        result_list = []
        for vac in data:
            url_vac = f'https://api.hh.ru/vacancies/{vac["id"]}'
            response = requests.get(url_vac).json()
            if response['salary']:
                description = ' '.join(re.sub(re.compile('<.*?>'), '', response['description'])
                                       .strip()
                                       .split())
                salary = ""
                if response['salary']['from'] and response['salary']['to']:
                    salary = f"{response['salary']['from'] or ''} - {response['salary']['to'] or ''} {response['salary']['currency']}"
                if response['salary']['from'] and not response['salary']['to']:
                    salary = f"{response['salary']['from'] or ''} {response['salary']['currency']}"
                if response['salary']['to'] and not response['salary']['from']:
                    salary = f"{response['salary']['to'] or ''} {response['salary']['currency']}"
                description = description[:1000] + '...' if len(description) >= 1000 else description
                result_list.append({'name': response['name'],
                                    'description': description,
                                    'skills': (map(lambda x: x['name'], response['key_skills'])),
                                    'employer': response['employer']['name'],
                                    'salary': salary,
                                    'area': response['area']['name'],
                                    'published_at': response['published_at'][:10]})

        return result_list



