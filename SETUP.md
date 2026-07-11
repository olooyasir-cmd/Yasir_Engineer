# 🏁 START HERE — Get Your Repo Ready

**Do this once, at the very start of the bootcamp.** It takes about 10 minutes.
By the end, you'll have your own copy of this project on YOUR GitHub, ready to fill in week by week.

---

## Step 1 · Make your own copy (click "Use this template")

1. Go to the starter repo: **`https://github.com/cloudwithshad/my-first-ai-app`**
2. Click the green **`Use this template`** button → **`Create a new repository`**
3. Name it **`my-first-ai-app`**
4. Make sure it's set to **Public** ✅
   _(Public = employers can see your work. That's the whole point!)_
5. Click **Create repository**

> 🎉 You now have your own copy at `github.com/YOUR-USERNAME/my-first-ai-app`

**⚠️ Don't just download the ZIP.** Use the template button — it makes the repo *yours*, with your own commit history.

---

## Step 2 · Get it onto your computer

Open your terminal (Git Bash on Windows) and run — **replace `YOUR-USERNAME`**:

```bash
git clone https://github.com/YOUR-USERNAME/my-first-ai-app.git
cd my-first-ai-app
```

You should now see the folders: `week1`, `week2`, `week3`, `week4`, `week5`, `capstone`.

---

## Step 3 · Install the libraries

```bash
pip install -r requirements.txt
```

---

## Step 4 · Set your OpenAI key (Week 2 onwards)

Your key is a **password**. It goes in an environment variable — **never** in your code.

**Mac / Linux / Git Bash:**
```bash
export OPENAI_API_KEY="sk-your-key-here"
```

**Windows PowerShell:**
```powershell
$env:OPENAI_API_KEY="sk-your-key-here"
```

Check it worked:
```bash
echo $OPENAI_API_KEY
```

> 🔐 **The `.gitignore` in this repo protects you** — it stops `.env` and secrets files from ever being committed. Don't delete it.
>
> **If you ever accidentally push your key: delete it immediately** at platform.openai.com and make a new one. Tell your mentor. It happens — just act fast.

---

## Step 5 · Make your first commit ✅

Prove everything works. Open `README.md`, add your name at the top, then:

```bash
git add .
git commit -m "Add my name — starting the bootcamp!"
git push
```

Refresh your GitHub page. **Your name is live on the internet.** That's your first push. 🎉

---

## 🔁 Your weekly rhythm

After every lab, run these three commands:

```bash
git add .
git commit -m "Complete Lab 2.1 — Market Assistant"
git push
```

Then **tick the box** in `README.md` for that lab.

> 💡 **Commit often.** Every push is a save point, and your commit history becomes proof of your journey. Employers genuinely look at this.

---

## 🆘 Stuck?

- **`git: command not found`** → Install Git (see the setup guide on the course dashboard)
- **Asked for a password when pushing?** → GitHub needs a *Personal Access Token*, not your password. Ask in the group — we'll walk you through it.
- **Anything else** → Bring it to the WhatsApp group or a live session. **Never stay stuck alone.**

---

_🇬🇭 Let's build._
