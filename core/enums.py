import json
from enum import Enum


def load_lottie_file(filepath):
    """Load Lottie animation from local JSON file."""
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except:
        pass
    return None


class Graphic(Enum):
    coding_boy=load_lottie_file("lottiefiles/coding-boy.json")
    tech_stack=load_lottie_file("lottiefiles/tech_stack.json")
    certifications=load_lottie_file("lottiefiles/t.json")


class Texture(Enum):
    rainbow_line="""
    <hr style="
        border: none;
        height: 4px;
        background: linear-gradient(to right, 
            red, orange, yellow, green, blue, indigo, violet);
        border-radius: 5px;
    ">
    """

class InfoSection(Enum):
    title="Welcome to My Portfolio!"
    intro="I'm Your Name"
    description="I am a passionate **Developer** with experience building scalable and efficient systems. Replace this text with a short introduction about yourself and your interests."
