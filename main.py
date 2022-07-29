welcome_prompt = "Welcome doctor, Please choose an option: \n - 1. List all patients \n - 2. Run a new diagnosis \n - q Quit program \n"

name_prompt = "What is the patient's name? \n"

appearance_prompt = "How is the patient's general appearance?\n - 1. Normal \n - 2. Irritable or Lethargic \n - m. Main Menu \n"

eye_prompt = "How are the patient's eyes?\n - 1. Eyes normal or slightly sunken \n - 2. Eyes very sunken \n - b. Back \n"

skin_prompt = "How is the patient's skin when pinched?\n - 1. Normal Skin Pinch \n - 2. Slow Skin Pinch \n - b. Back \n"

severe_dehydration = "Severe_dehydration"
some_dehydration = "Some_dehydration"
no_dehydration = "No_dehydration"
error_message = "Patient data could not be saved. Pleae check your input and try again"


patients_diagnosis = ["Mike: Some Dehydration",
"Melly: Severe Dehydration",
"Tim: No Dehydration"]



def list_patients():
    for patient in patients_diagnosis:
        print(patient)

def save_diagnosis(name, diagnosis):
    if name == "" or diagnosis == "":
        print(error_message)
        return
    final_diagnosis = name + ": " + diagnosis
    patients_diagnosis.append(final_diagnosis)
    print("Final diagnosis", final_diagnosis, "\n")
        

def ass_skin(skin):
    if skin == '1':
        return no_dehydration
    elif skin == '2':
        return severe_dehydration
    elif skin == 'b':
        appearance_diagnosis()
    else:
        return ""
    


def ass_eyes(eyes):
    if eyes == '1':
        return no_dehydration
    elif eyes == '2':
        return severe_dehydration
    elif eyes == 'b':
        appearance_diagnosis()
    else:
        return ""
        


def appearance_diagnosis():
    appearance = input(appearance_prompt)
    if appearance == '1':
        eyes = input(eye_prompt)
        return ass_eyes(eyes)
    elif appearance == '2':
        skin = input(skin_prompt)
        return ass_skin(skin)
    elif appearance == 'm':
        main()


def new_diagnosis():
    name = input(name_prompt)
    diagnosis = appearance_diagnosis()
    save_diagnosis(name, diagnosis)



def main():
    while True:
        selection = input(welcome_prompt)
        if selection == '1':
            list_patients()
        elif selection == '2':
            new_diagnosis()
        elif selection == 'q':
            return


main()
