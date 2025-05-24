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
  - `overall_score`: Are you the chosen one? 🔮
  - `matches`: Stuff you nailed 🎯
  - `missing`: Stuff you forgot like a noob 😬
  - `summary`: TL;DR of your job life 📝

---

## 🛠️ How to run this beast

1. Clone the repo (duh)  
```bash
git clone https://github.com/patryk-pszeniczny/bitbridge-ai-cv-analiser.git
cd cv-analyzer
```

2. Throw your CVs into the `input/` folder like you're feeding a monster 👹  
3. Set up your `.env` file like a pro:
```
OPENAI_API_KEY=your-super-secret-api-key
OPENAI_API_MODEL=gpt-4
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
  "must_have": ["Python", "Teamwork", "AI experience"],
  "nice_to_have": ["Docker", "Kubernetes", "Astral projection"]
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
