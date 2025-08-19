import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)
    

animals_data = load_data("animals_data.json")
#print(animals_data)


def get_animal_info(data):
    """ Displays name, diet, location and type of the animal from the data """
    for animal in data:
        print("\nName:", animal["name"]) 
        print("Diet:", animal["characteristics"]["diet"])
        print("Location:", animal["locations"][0])
        if "type" in animal["characteristics"]:
            print("Type:", animal["characteristics"]["type"])
            
            
get_animal_info(animals_data)