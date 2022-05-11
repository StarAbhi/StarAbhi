def get_potential_cases(patients,diagnostic_symptoms,min_symptom_count):
    #make this list to store the patients name 
    patients_list = []
    #check all key and value from dictionary and perform intersection between dictionary value and diagnostic_symptoms
    #after this check the len of resulting if the len is greater of equal than add dictionary key in patients_list 
    for key ,values in patients.items():
        if len(set(values) & set(diagnostic_symptoms))>=min_symptom_count:
            patients_list.append(key)
    #return the patients_list
    return patients_list

if __name__ == "__main__":
    all_patients = {
        "Mary":["cough","tired","swollen lymph nodes"],
        "Abdoulaye":["headache"],
        "Amir":["tired","cough","fever"],
        "Maya":[],
        "Yana":["breast lump","swollen lymph nodes","cough"]
    }
    covid_symptoms = ["cough","fever","tired"]
    covid_candidates_2 = get_potential_cases(all_patients,covid_symptoms,2)
    print(covid_candidates_2)

    covid_candidates_3 = get_potential_cases(all_patients,covid_symptoms,3)
    print(covid_candidates_3)

    breast_cancer_symptoms = ["tired","swollen lymph nodes","breast lump"]
    breast_cancer_candidates = get_potential_cases(all_patients,breast_cancer_symptoms,2)
    print(breast_cancer_candidates) 