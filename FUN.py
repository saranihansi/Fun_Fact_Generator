import random

emotional_fun_facts = {
    "happy": [
        "😊 Smiling is contagious and can boost your mood even if you fake it!",
        "😄 Penguins propose to their mates with a pebble, and stay together for life!",
        "🌟 Dogs can understand over 150 words and can count up to five!"
    ],
    "curious": [
        "🤔 The human brain can process images in as little as 13 milliseconds!",
        "🔍 Honeybees can recognize human faces!",
        "🧪 A teaspoonful of neutron star would weigh about 6 billion tons!"
    ],
    "amazed": [
        "🌈 There are more possible iterations of a game of chess than atoms in the universe!",
        "✨ Dolphins give each other names and can call to each other specifically!",
        "🌟 A day on Saturn's moon Titan is 15.9 Earth days long!"
    ],
    "peaceful": [
        "🌸 Hummingbirds are the only birds that can fly backwards!",
        "🌿 Trees in a forest communicate and share nutrients through an underground network!",
        "🌙 The Moon moves approximately 3.8 cm away from Earth every year!"
    ]
}

def get_emotional_fact():
    emotion = random.choice(list(emotional_fun_facts.keys()))
    fact = random.choice(emotional_fun_facts[emotion])
    return f"[{emotion.upper()}] {fact}"

def main():
    print("Welcome to the Emotion-Powered Fun Fact Generator!")
    print("=-"*30 + "\n")
    
    while True:
        input("Press Enter to get an emotional fun fact (or Ctrl+C to exit)!")
        print("\n🎈 " + get_emotional_fact())
        print("\n" + "=-"*30 + "\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nThanks for learning with emotions! Goodbye! 👋")