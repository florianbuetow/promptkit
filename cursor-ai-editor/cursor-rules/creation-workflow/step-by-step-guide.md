# 🎨 How to Create Your Own Cursor Rules

A step-by-step workflow for creating effective cursor rules using AI assistance.

## 🛠️ Preparation

Collect a list of resources that give good advice on coding and best practices with the technologies that you are using in your project.

I went to YouTube and searched and skimmed some of the videos that made sense to me.

Then grab an example prompt that comes close to what you are trying to do. It will serve as a starter for the AI to craft your own cursor rules file. I took mine from [cursor.directory](https://cursor.directory/rules) where I selected one of the React prompts that sounded good.

Then you go to your favorite AI chat. I used Gemini 2.5 Pro because it can process YouTube links and is supposed to be great with logic and code. I don't know if that means it also gives great coding advice, but I am willing to just try it out.

## 🚀 Prompt Sequence

### Initial Prompt

```
Please watch the following video and create me a list of rules and best practices to follow.

<INSERT LINK TO YOUTUBE VIDEO #1>

Here is an example document on how to specify the rules and best practices to follow:

<INSERT CONTENT OF EXAMPLE CURSOR RULES FILE>
```

### Follow-up Prompt (2)

```
Great thank you very much. Please now watch this video and add the advice and tips and best practices and guidelines given to your document:

<INSERT LINK TO YOUTUBE VIDEO #2>
```

### Follow-up Prompt (3)

```
Perfection! Now lets add the advice from yet another video in the same manner as before:

<INSERT LINK TO YOUTUBE VIDEO #3>
```

### Critical Review Prompt (4)

```text
Please critically review the guide we've created so far. Justify every single point on why it should be in the guide. If a point is not strong enough, admit it so we can remove it to keep our guide as informative and actionable as possible! THIS IS FOR MAKING THE BEST ENGINEERS POSSIBLE!!!!!!!!!
```

### Format Conversion Prompt (5)

```
Please create me a cursorrules file from this (markdown format with yaml header)
```

### Correction Prompt (6)

When proofreading the output, I discovered something unwanted, so I followed up with a correction:

```
We need to create a revision because we will use FastAPI and Python for the backend instead of NextJS.
```

## ✅ Final Result

I then got an updated version in Markdown format that I could save as a cursor rules mdc file.

## 💡 Tips for Success

- **Use multiple sources** - Don't rely on just one video or resource
- **Be critical** - Not every piece of advice needs to be included
- **Iterate** - Refine and improve your rules over time
- **Test** - Use your rules in real projects and adjust as needed
