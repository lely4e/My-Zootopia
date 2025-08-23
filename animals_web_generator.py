import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def read_html(file_path):
    """ Read an HTML file """
    with open(file_path, "r", encoding="utf-8") as handle:
        return handle.read()


def serialize_animal(animal_obj):
    """ Serialization of a single animal object """
    output = ''
    output += '<li class="cards__item">\n'
    output += f'<div class="card__title" style="margin: 10px;">{animal_obj["name"]}</div>\n'
    output += '<div class="card__text">\n'
    output += '<ul>\n'
    output += f'<li><strong>Genus:</strong> {animal_obj["taxonomy"].get("genus")}</li>\n'
    output += f'<li><strong>Diet:</strong> {animal_obj["characteristics"].get("diet")}</li>\n'
    output += f'<li><strong>Location:</strong> {animal_obj["locations"][0]}</li>\n'
    output += f'<li><strong>Type:</strong> {animal_obj["characteristics"].get("type")}</li>\n'
    output += f'<li><strong>Color:</strong> {animal_obj["characteristics"].get("color")}</li>\n'
    output += f'<li><strong>Skin type:</strong> {animal_obj["characteristics"].get("skin_type")}</li>\n'
    output += '</ul>'
    output += '</div>'
    output += '</li>\n'
    return output
    
    
def get_animal_info(data):
    """ Displays name, diet, location and type of the animal from the data """
    output = ""
    for animal in data:   
        output += serialize_animal(animal) 
    return output
            

def get_skin_types(data):
    """ Displays unique skin types from the data """
    skin_types = set()
    for animal in data:
        if "skin_type" in animal["characteristics"]:
            skin_types.add(animal["characteristics"]["skin_type"])
    return sorted(skin_types)


def filtered_animals(data, guess):
    filtered_animals_data = []
    for animal in data:
        if guess ==  animal["characteristics"]["skin_type"].lower():
            filtered_animals_data.append(animal)
    return filtered_animals_data


def new_html_data(file_path, filtered_animals_data):
    """ Creating a new HTML file with the necessery information """
    with open(file_path, "w", encoding="utf-8") as handle:
        html_data = read_html("animals_template.html")
        animals_info = get_animal_info(filtered_animals_data)
        new = html_data.replace("__REPLACE_ANIMALS_INFO__", animals_info)
        return handle.write(new)

    
def error_page(file_path):
    """ Renders an error page """
    with open(file_path, "w", encoding="utf-8") as handle:
        output = ''
        output += '<li class="cards__item">\n'
        output += '<div class="card__title" style="margin: 10px;">Cards are not found!</div>\n'
        output += '</div>'
        output += '</li>\n'

        html_data = read_html("animals_template.html")
        new = html_data.replace("__REPLACE_ANIMALS_INFO__", output)
        return handle.write(new)
    
    
def main():
    """ Main logic of the program """
    animals_data = load_data("animals_data.json")

    skin_types = get_skin_types(animals_data)
    if skin_types:
        print("The following skin types are available:")
        for skin_type in skin_types:
            print(f"- {skin_type}")
    else:
        print("No skin types available")

    user_choice = input("Enter skin type: ").strip().lower()

    suitable_animals = filtered_animals(animals_data, user_choice)
    if suitable_animals:
        print(new_html_data("animals.html", suitable_animals))
    else:
        print("Invalid skin type")
        print(error_page("animals.html"))


if __name__ == "__main__":
    main()
    
