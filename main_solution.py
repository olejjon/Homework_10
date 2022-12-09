import json


def load_candidates():
    """которая загрузит данные из файла"""
    with open("candidates.json","r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def get_all():
    """которая покажет всех кандидатов"""
    data = load_candidates()
    let = ""
    for data in data:
        let += f"<pre>Имя кандидата - {data['name']}\nПозиция кандидата: {data['pk']}\nНавыки: {data['skills']}</pre>"
    return let


def get_by_pk(pk):
    """которая вернет кандидата по pk"""
    data = load_candidates()
    for data in data:
        if data['pk'] == pk:
            return data


def get_by_skill(skill_name):
    """которая вернет кандидатов по навыку"""
    data = load_candidates()
    list_skills = []
    for data in data:
        for skill in data['skills'].split(", "):
            if skill_name.lower() == skill.lower() and data not in list_skills:
                list_skills.append(data)

    return list_skills
