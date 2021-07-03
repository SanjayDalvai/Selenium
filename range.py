import pickle

#Pickling_of_object_into_a_string_and_dumping_it_into_a_File
def pickle_data():
    data = {
        'name': 'Prashant',
        'profession': 'Software Engineer',
        'country': 'India'
    }
    filename = 'PersonalInfo'
    outfile = open("sample.txt", 'wb')
    pickle.dump(data, outfile)
    outfile.close()

#Gettin_the_object_into_original_form_from_string
pickle_data()

def unpickling_data():
    file = open('sample.txt','rb')
    new_data = pickle.load(file)
    file.close()
    return new_data


print(unpickling_data())