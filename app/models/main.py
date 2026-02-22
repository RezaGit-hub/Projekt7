from app.models.models_query import insert_section, insert_doctor, insert_nurs, insert_medication, insert_patient, get_all_doctors, get_all_medication, get_all_patients, get_all_section

if __name__=="__main__":
    kinder_id = insert_section("Kinder")
    operation_id = insert_section("operation")
    verbrand_id = insert_section("verbrand")

    aspirin_id = insert_medication("aspirin")
    ipoberofen_id = insert_medication("ipoberofen")

    dr_Max_id = insert_doctor("max muster", kinder_id)
    dr_lucas_id =insert_doctor("lucas möller", verbrand_id)

    p_jon_id = insert_patient("jon bullton", kinder_id, aspirin_id)
    p_alex_id = insert_patient("alex sosk", operation_id, ipoberofen_id)
    p_dennis_id = insert_patient("Dennnis Steffen", verbrand_id, aspirin_id )

    print("Kinder ID:", kinder_id)
    print("Operation ID:", operation_id)
    print("verbrand ID: ", verbrand_id)

    print("patient ID : ", p_alex_id)
    print("doctor ID : ", dr_lucas_id)

print("Sections:  ")
sections = get_all_section()
for section in sections:
    print(section)

print("Patients:  ")
patines = get_all_patients()
for patien in patines:
    print(patien)




