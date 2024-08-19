# data.py

crop_data = {
    "Wheat": {"soil_type": "Loamy", "climate": "Temperate", "water_requirement": "Moderate"},
    "Rice": {"soil_type": "Clayey", "climate": "Tropical", "water_requirement": "High"},
    "Maize": {"soil_type": "Sandy", "climate": "Warm", "water_requirement": "Low"},
    "Soybean": {"soil_type": "Loamy", "climate": "Subtropical", "water_requirement": "Moderate"},
    "Cotton": {"soil_type": "Sandy", "climate": "Arid", "water_requirement": "Low"},
    "Barley": {"soil_type": "Clayey", "climate": "Temperate", "water_requirement": "Moderate"},
    "Sugarcane": {"soil_type": "Alluvial", "climate": "Tropical", "water_requirement": "High"},
    "Potato": {"soil_type": "Silty", "climate": "Cool", "water_requirement": "High"},
}

soil_data = {
    "Loamy": {"pH": 6.0, "nutrients": "High", "drainage": "Good"},
    "Clayey": {"pH": 5.5, "nutrients": "Moderate", "drainage": "Poor"},
    "Sandy": {"pH": 7.0, "nutrients": "Low", "drainage": "Excellent"},
    "Alluvial": {"pH": 6.5, "nutrients": "High", "drainage": "Moderate"},
    "Silty": {"pH": 6.2, "nutrients": "High", "drainage": "Moderate"},
    "Peaty": {"pH": 4.5, "nutrients": "Very High", "drainage": "Poor"},
}

disease_data = {
    "Rust": {"crops_affected": ["Wheat", "Barley"], "symptoms": "Orange-brown pustules", "control": "Use resistant varieties"},
    "Blight": {"crops_affected": ["Rice", "Potato"], "symptoms": "Leaf spots", "control": "Apply fungicides"},
    "Wilt": {"crops_affected": ["Maize", "Soybean"], "symptoms": "Wilting leaves", "control": "Remove infected plants"},
    "Bollworm": {"crops_affected": ["Cotton"], "symptoms": "Holes in bolls", "control": "Use biopesticides or insecticides"},
    "Downy Mildew": {"crops_affected": ["Grapes", "Sugarcane"], "symptoms": "Yellow spots on leaves", "control": "Apply fungicides"},
    "Root Rot": {"crops_affected": ["Potato", "Soybean"], "symptoms": "Decaying roots", "control": "Improve soil drainage"},
    "Leaf Curl": {"crops_affected": ["Tomato", "Cotton"], "symptoms": "Curling leaves", "control": "Use disease-free seeds and control pests"},
}
