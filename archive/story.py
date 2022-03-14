import random

# settings
settingA = [
    "Snowy north",
    "Country side",
    "Farmstead",
    "City",
    "Dystopian wasteland"
]

settingB = [
    "Dark",
    "Normal seasoned",
    "Crowded",
    "Isolated"
]

settingC = [
    "Poor",
    "Rich",
    "Moderate"
]

# time of year
settingD = [
    "Winter",
    "Autumn",
    "Summer",
    "Spring"
]

# protagonist
protagA = [
    "Employed",
    "Unemployed"
]

protagA1 = [
    "cashier",
    "server",
    "Hacker",
    "Office worker",
    "Food preparation worker",
    "janitor",
    "Bartender",
    "Retail sales associate"
    "Laborer"
    "Administrative assistant",
    "Medical assistant",
    "Construction worker",
    "Mechanic",
    "Police officer",
    "Truck Driver",
    "Lawyer",
    "Software developer"
]

protagB = [
    "Married",
    "Single (Divorced)",
    "Single (Never married)",
    "Divorced"
]

protagC = [
    "many",
    "some",
    "a lot"
]

protagD = [
    "Old 60 years",
    "Young 18 years",
    "Middle age 35 years"
]

protagE = [
    "fat",
    "slim",
    "average",
]

protagHobbies = [
    "reading",
    "Hiking",
    "Backpacking",
    "Camping",
    "Hunting",
    "Fishing",
    "Archery",
    "Canoeing",
    "Kayaking",
    "Running",
    "Geocaching",
    "Growing Vegetables",
    "Composting",
    "Metal Detecting",
    "Bird Watching",
    "Beekeeping",
    "Astronomy",
    "Meteorology",
    "Kite Flying",
    "Sand Castle Making",
    "Hobby Horsing",
    "Antiquing",
    "Coin Collecting",
    "Stamp Collecting",
    "Vintage Clothing Collecting",
    "Classic Car Collecting",
    "Antique Book and Manuscript Collecting",
    "Art Collecting",
    "Shell and Sea Glass Collecting",
    "Leaf Collecting and Pressing",
    "Record Collecting",
    "Postcard Collecting",
    "Shoe Collecting",
    "Toy Collecting",
    "Memorabilia Collecting (e.g. Star Wars products)",
    "Sports Memorabilia Collecting",
    "Rock Tumbling",
    "Cooking",
    "Baking",
]

# theme
themeA = [
    "Achluophobia Fear of darkness",
    "Algophobia Fear of pain",
    "Agoraphobia Fear of open spaces or crowds",
    "Anthrophobia Fear of flowers",
    "Aphenphosmphobia Fear of being touched",
    "Aphenphosmphobia Fear of being touched",
    "Arithmophobia Fear of numbers",
    "Atelophobia Fear of imperfection",
    "Cacophobia Fear of ugliness",
    "Catoptrophobia Fear of mirrors",
    "Necrophobia Fear of death or dead things",
    "Philophobia Fear of love",
    "Verminophobia Fear of germs",
    "Social Phobia (Social anxiety disorder)",
    "Pathophobia Fear of disease",
    "Pharmacophobia Fear of medicines",
    "nihilism - nothing exist, nothing matters",
    "Wanting something but ending up hurting the protagonist e.g. wanting a baby, but it turns out to be the next spawn of satan",
    "obsession",
    "duality",
    "jealousy",
]

# monster
monster1 = [
    "unseen face",
    "blades for hands"
]

monster2 = [
    "Foggy Lake",
    "Cave",
    "In dreams",
    "Cabin",
    "Nether/abyss"
]

# story circle
# comfort zone
circle1 = [
    "being trapped into a job they hate",
    "life with family",
    "physical limitations",
    "avoids scary things",
    "never follows through with goals",
    "never gets promoted at work",
    "works dead end job",
    "perfectionist",
    "constantly puts others down to feel important",
    "has never moved out of hometown",
    "always blames others for own mistakes",
    "addicted to social media",
    "addicted to worldly possessions",
    "never settles down in a city or job for longer than 2 years",
    "constantly learning new things and reinventing self",
    "very religious",
    "anti-religious, questions authority",
    "never misses a day exercising",
    "climbs the corporate ladder",
    "alcoholic",
    "Born and raised in home town",
    "Lives in anger with spouse",
]

circle2 = [
    "Achluophobia Fear of darkness"
]

circle3 = [
    "Achluophobia Fear of darkness"
]

circle4 = [
    "Achluophobia Fear of darkness"
]

circle5 = [
    "Achluophobia Fear of darkness"
]

circle6 = [
    "Achluophobia Fear of darkness"
]

# function to randomize
def getRandom(a):
    arrTotal = int(len(a))
    randomNum = random.randint(0, arrTotal-1)
    return randomNum

# print all settings
print("============================")
print ("1. SETTING")
print("Place: " + settingB[getRandom(settingB)]) + " " + settingA[getRandom(settingA)]
print ("Economy: " + settingC[getRandom(settingC)])
print ("Build a moodboard to help visualize the setting")
print ("---")

# print character qualities (flaw in employed vs Unemployed)
print ("2. PROTAGONIST")
print ("Job status: " + protagA[getRandom(protagA)])
print ("Marital Status: " + protagB[getRandom(protagB)])
print ("Job: " + protagA1[getRandom(protagA1)])
print ("Friends: " + protagC[getRandom(protagC)])
print ("Age: " + protagD[getRandom(protagD)])
print ("Hobbies: " + protagHobbies[getRandom(protagHobbies)])
print ("Comfort Zone: " + circle1[getRandom(circle1)])
print ("Fear: " + themeA[getRandom(themeA)])
print ("---")

# print theme
print ("3. THEME")
print ("Fear: " + themeA[getRandom(themeA)])
print ("Other: ")
print ("---")

# print monster
print ("4. MONSTER")
print ("Features: " + monster1[getRandom(monster1)])
print ("Represents the character's/metaphor for: " + themeA[getRandom(themeA)])
print ("Domicle: " + monster2[getRandom(monster2)])
print ("---")

# story circle
print ("5. STORY CIRCLE")
print ("You: Establish protagonist in their comfort zone: " + circle1[getRandom(circle1)])
print ("Need: But they desperately want something: " + circle2[getRandom(circle2)])
print ("Go: enter into chaos realm: They enter an unfamiliar situation" + circle3[getRandom(circle3)])
print ("Search: Road of trials: The adapt to that unfamiliar situation" + circle4[getRandom(circle4)])
print ("Find: They get what they wanted after much effort: " + circle5[getRandom(circle5)])
print ("Take: Knowingly or unknowingly, they pay a heavy price: " + circle6[getRandom(circle6)])
print ("Return: They return back to their zone of comfort: " + circle6[getRandom(circle6)])
print ("Change: they are changed forever: " + circle6[getRandom(circle6)])
print ("1. BRAINSTORMING")
print ("2. NOW OPEN UP YOUR 3 ACT STORY STRUCTURE IN NUMBERS AND GET TO WORK")
print ("3. Write")
print ("============================")
# End
