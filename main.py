from flask import Flask
from main_solution import  get_all, get_by_skill, get_by_pk

main = Flask(__name__)


@main.route("/")
def page_index():
    return get_all()


@main.route('/candidates/<int:pk>')
def profile(pk):
    data_pk = get_by_pk(pk)
    return f"<img src = {data_pk['picture']}>\n\n<pre>Имя кандидата - {data_pk['name'] }\nПозиция кандидата {data_pk['pk']}\nНавыки:{data_pk['skills']}"


@main.route('/skills/<skill>')
def qq(skill):
    data_skill = get_by_skill(skill)
    page_skills = ""
    for skill_pk in data_skill:
        page_skills += f"<pre>Имя кандидата - {skill_pk['name'] }\nПозиция кандидата {skill_pk['pk']}\nНавыки:{skill_pk['skills']}"
    return page_skills




main.run(host='0.0.0.0', port=4000)
