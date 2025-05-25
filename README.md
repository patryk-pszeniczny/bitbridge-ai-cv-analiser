![logo](https://imgur.com/6iItBJn.png)
# 🤖 CV Analyzer 3000™ — by BitBridge.pl 💼✨
Welcome to **CV Analyzer 3000™**, the *AI overlord* of all job applications 🤓  
It reads your CV 📄, judges you silently 🤐, and then tells you how awesome (or not) you are.  
Used on [bitbridge.pl](https://bitbridge.pl) — because manual recruiting is sooo 2012 🕸️💀

---

## 💡 What does it do?

- 🧠 Reads your boring ol' PDF resume  
- 🔍 Checks if you match the *secret sauce* criteria from our JSON file  
- 🤯 Sends it to OpenAI’s GPT (aka the robot with the brain of 1,000 HR people)  
- 📊 Gives you back a brutally honest JSON report with:
  - `overall_score` (0–100): Are you the chosen one? 🔮  
  - `best_fit` (0–100): How well you fit the juiciest role 💼  
  - `candidate`: Your name, if you remembered to put it 😅  
  - `matches`: Stuff you nailed 🎯  
  - `missing`: Stuff you forgot like a noob 😬  
  - `summary`: Bullet-point roast of your job life 📝  
  - `follow_up_questions`: 10 questions to make you sweat in the interview 🔥

---

## 🛠️ How to run this beast

1. Clone the repo (duh)  
```bash
git clone https://github.com/patryk-pszeniczny/bitbridge-ai-cv-analyzer.git
cd cv-analyzer
```

2. Throw your CVs into the `input/` folder like you're feeding a monster 👹  
3. Set up your `.env` file like a pro:
```
OPENAI_API_KEY=your-super-secret-api-key
OPENAI_API_MODEL=gpt-4
OPENAI_API_TEMPERATURE=0.3
OPENAI_API_CONTENT=secret :)
```

4. Create a `config/config.json` file with all your juicy criteria (or steal ours 🤫)  
5. Run the magic spell 🪄:
```bash
python main.py
```

---

## 📁 Folder vibes

```
input/        # Drop your PDFs here 🧾
output/       # We'll dump the results here 🔮
config/       # Your sacred hiring criteria 🧙‍♂️
.env          # Your OpenAI API key (don't leak it or Skynet will come) 🤖
```

---

## 🧙 Sample Criteria (config/config.json)

```json
{
  "mandatory_requirements": [
    "Minimum 2 years of experience with Java (advanced level)",
    "Experience working with Spring Boot",
    "English proficiency at B2 level or higher",
    "Ability to work in a Scrum team (regular Scrum)",
    "Problem-solving skills in complex environments",
    "Ability to communicate with both technical and non-technical stakeholders"
  ],
  "additional_requirements": [
    "Familiarity with the Gosu language (Guidewire junior/regular)",
    "Experience with microservice architecture",
    "Knowledge of relational and non-relational databases",
    "Familiarity with Docker",
    "Experience with the Azure platform",
    "Experience with Python, GenAI, or Databricks",
    "AWS or other cloud-related certifications",
    "Interest in modern technologies and willingness to continuously develop",
    "Experience working with CI/CD",
    "Ability to work in a cloud-native environment"
  ]
}

```

---

## 😱 Why does this exist?

Because recruiters are tired 🥱  
And AI never sleeps 🧠⚡  
Also... it's fun to roast CVs with robots 🔥

---

## 🧠 Disclaimer

This bot has no feelings...  
...but it'll still judge you harder than your grandma at Christmas 🎄👵

---

## 🚀 Future Plans (maybe)

- HTML reports with ✨sparkles✨  
- Fancy GUI so you can click stuff instead of using Terminal like a hacker  
- Automatic meme rating system based on CV style 😎

---

Made with ❤️, caffeine ☕ and a little existential dread 😵  
By the wizards at [bitbridge.pl](https://bitbridge.pl) 🧙‍♀️🧙
