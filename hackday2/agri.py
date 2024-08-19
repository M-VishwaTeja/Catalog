# main.py

# Importing data from data.py
from data import crop_data, soil_data, disease_data

def display_options(options):
    print("\nAvailable options:")
    for option in options:
        print(f"- {option}")

def get_normalized_input(prompt, valid_options, display_help=True):
    while True:
        input_value = input(f"{prompt} (or type 'help' for suggestions): ")
        if input_value.lower() == 'help' and display_help:
            display_options(valid_options)
            continue
        if input_value.lower() in map(str.lower, valid_options):
            return next(option for option in valid_options if option.lower() == input_value.lower())
        print(f"Invalid input: {input_value}. Please choose from {', '.join(valid_options)}.")

def get_symptoms_input(prompt, valid_options):
    while True:
        input_value = input(f"{prompt} (or type 'help' for suggestions): ")
        if input_value.lower() == 'help':
            display_options(valid_options)
            continue
        symptoms = input_value.split(", ")
        if all(symptom.lower() in map(str.lower, valid_options) for symptom in symptoms):
            return [next(option for option in valid_options if option.lower() == symptom.lower()) for symptom in symptoms]
        print(f"Invalid input: {input_value}. Please ensure all symptoms are valid options.")

def select_crop(soil_type, climate):
    print("\nCrop Selection Recommendations:")
    recommended_crops = [crop for crop, info in crop_data.items() if info["soil_type"].lower() == soil_type.lower() and info["climate"].lower() == climate.lower()]
    if recommended_crops:
        for crop in recommended_crops:
            print(f"- {crop} is suitable for your soil and climate conditions.")
    else:
        print("No suitable crops found for the provided soil type and climate.")

def analyze_soil(soil_type):
    normalized_soil_type = next(key for key in soil_data.keys() if key.lower() == soil_type.lower())
    print(f"\nSoil Analysis for {normalized_soil_type}:")
    print(f"pH Level: {soil_data[normalized_soil_type]['pH']}")
    print(f"Nutrient Content: {soil_data[normalized_soil_type]['nutrients']}")
    print(f"Drainage: {soil_data[normalized_soil_type]['drainage']}")

def identify_disease(crops, symptoms):
    print("\nDisease Identification:")
    for crop in crops:
        normalized_crop = next(option for option in crop_data.keys() if option.lower() == crop.lower())
        possible_diseases = []
        for disease, info in disease_data.items():
            if normalized_crop.lower() in map(str.lower, info["crops_affected"]):
                matched_symptoms = [symptom for symptom in symptoms if symptom.lower() in info["symptoms"].lower()]
                if matched_symptoms:
                    possible_diseases.append((disease, matched_symptoms, info["control"]))
        
        if possible_diseases:
            print(f"\nFor crop: {normalized_crop}")
            for disease, matched_symptoms, control in possible_diseases:
                print(f"- Possible disease: {disease}")
                print(f"  Matched Symptoms: {', '.join(matched_symptoms)}")
                print(f"  Control measures: {control}")
        else:
            print(f"No matching disease found for {normalized_crop} with the provided symptoms.")

def main():
    print("Welcome to the Crop and Soil Management System")
    
    while True:
        # Validate and get normalized soil type and climate input with help option
        soil_type = get_normalized_input("Enter your soil type", soil_data.keys())
        climate = get_normalized_input("Enter your climate type", set(info["climate"] for info in crop_data.values()))
        
        # Crop Selection
        select_crop(soil_type, climate)
        
        while True:
            # Disease Identification for Multiple Crops
            crops = input("\nEnter the crops you want to check for diseases (comma-separated, or type 'help' for options): ").split(", ")
            crops = [get_normalized_input(f"Confirm crop '{crop.strip()}'", crop_data.keys(), display_help=False) for crop in crops]
            
            # Symptoms input with help feature
            all_symptoms = set()
            for info in disease_data.values():
                all_symptoms.update(info["symptoms"].split(", "))
            
            symptoms = get_symptoms_input("Enter the symptoms observed", all_symptoms)
            identify_disease(crops, symptoms)
            
            # Ask user if they want to check another crop
            cont = input("\nDo you want to check another crop? (yes/no): ").strip().lower()
            if cont != 'yes':
                break
        
        # Ask user if they want to start over
        restart = input("\nDo you want to start over with a new soil type and climate? (yes/no): ").strip().lower()
        if restart != 'yes':
            break
    
    print("\nThank you for using the Crop and Soil Management System!")

if __name__ == "__main__":
    main()
