import json
__data = []

#возвращает список всех кандидатов
def load_candidates_from_json(path):
    global __data
    with open(path, 'r', encoding='utf-8') as file:
        __data = json.load(file)
    return __data


#возвращает одного кандидата по его id
def get_candidate(candidate_id):
    for candidate in __data:
        if candidate['id'] == candidate_id:
            return {
                'name': candidate['name'],
                'position': candidate['position'],
                'picture': candidate['picture'],
                'skills': candidate['skills']
            }


#возвращает кандидатов по имени
def get_candidates_by_name(candidate_name):
    return [candidate for candidate in __data if candidate_name.lower() in candidate['name'].lower()]


#возвращает кандидатов по навыку
def get_candidates_by_skill(skill_name):
    candidates = []
    for candidate in __data:
        skills = candidate['skills'].lower().split(', ')
        if skill_name.lower() in skills:
            candidates.append(candidate)
    return candidates
