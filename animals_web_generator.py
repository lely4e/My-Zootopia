import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def read_html(file_path):
    """ Read an HTML file """
    with open(file_path, "r") as handle:
        return handle.read()


def get_animal_info(data):
    """ Displays name, diet, location and type of the animal from the data """
    output = ""
    for animal in data:
        output += '<li class="cards__item">'
        output += f"Name: {animal["name"]}<br/>\n" 
        output += f"Diet: {animal["characteristics"]["diet"]}<br/>\n"
        output += f"Location: {animal["locations"][0]}<br/>\n"
        if "type" in animal["characteristics"]:
            output += f"Type: {animal["characteristics"]["type"]}<br/>\n"         
    return output
            

def new_html_data(file_path):
    """ Creating a new HTML file with the necessery information """
    with open(file_path, "w") as handle:
        html_data = read_html("animals_template.html")  
        animals_info = get_animal_info(animals_data)
        new = html_data.replace("__REPLACE_ANIMALS_INFO__", animals_info)
        return handle.write(new)

    
animals_data = load_data("animals_data.json")
print(new_html_data("animals.html"))

