import json
import random

emotions = {
    "sad": [
        "I'm here for you. It's okay to cry.",
        "You’re not alone, and I care about you.",
        "That sounds really tough. Want to talk more about it?"
    ],
    "anxious": [
        "Try taking deep breaths. You're doing your best.",
        "It's okay to feel anxious. Let’s try grounding together.",
        "Let’s focus on what you can control right now."
    ],
    "lonely": [
        "I'm here with you. You're not alone.",
        "Would you like to talk or play a relaxing game?",
        "Even when it feels like it, you're never truly alone."
    ],
    "happy": [
        "That's wonderful! What made your day good?",
        "I'm so glad to hear that. Keep shining!",
        "Want to share your happiness? I'd love to hear!"
    ],
    "angry": [
        "Anger is a valid emotion. Want to vent about it?",
        "Try writing down what’s bothering you.",
        "I’m here to listen without judgment."
    ],
    "confused": [
        "Let’s break it down together. What's on your mind?",
        "Take a deep breath — you're doing fine.",
        "Would you like help figuring things out?"
    ]
}

# More realistic phrasings
templates = [
    "i feel {emotion}",
    "i am {emotion}",
    "i'm feeling very {emotion}",
    "i'm super {emotion} right now",
    "feeling kind of {emotion} today",
    "so {emotion} these days",
    "dealing with {emotion} again",
    "struggling with {emotion}",
    "been very {emotion} lately",
    "i can't stop being {emotion}"
]

dialog = {}

for emotion, responses in emotions.items():
    for i in range(1, 150):  # 150 × 10 = 1500 entries approx
        for template in templates:
            phrase = template.format(emotion=emotion)
            unique_phrase = f"{phrase} #{i}"
            dialog[unique_phrase] = random.choice(responses)

# Save dialog.json
with open("dialog.json", "w") as f:
    json.dump(dialog, f, indent=4)

print(f"Generated {len(dialog)} entries in dialog.json ✅")
