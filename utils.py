import json


def load_candidates_from_json():     # список всех кандидатов

    with open('candidates.json', 'r', encoding='utf-8') as file:
        candidates = json.load(file)

    return candidates


def get_candidate(candidate_id):  # поиск кандидатов по id

    candidates = load_candidates_from_json()
    for candidate in candidates:
        if candidate['id'] == candidate_id:
            return candidate


def get_candidates_by_name(candidate_name):   #поиск кандидата по имени

    candidates = load_candidates_from_json()
    candidates_matches = []
    candidate_name_lower = candidate_name.lower()
    for candidate in candidates:
        if candidate_name_lower in candidate['name'].lower():
            candidates_matches.append(candidate)


    return candidates_matches


def get_candidates_by_skill(skill_name): # поиск кандидатов по умениям

    candidates = load_candidates_from_json()
    skilled_candidates = []
    skill_lower = skill_name.lower()

    for candidate in candidates:
        candidate_skill = candidate['skills'].lower().split(', ')
        if skill_lower in candidate_skill:
            skilled_candidates.append(candidate)
    return skilled_candidates

