# Engineering Guidelines & Cursor Rules

This repository contains the consolidated engineering guidelines for our full-stack development team. The core of this is the `fullstack_guide.mdc` file, designed to be used as a set of rules within the [Cursor](https://cursor.sh/) IDE.

## `fullstack_guide.mdc`

This file provides a comprehensive set of rules and best practices for developing high-quality code using our technology stack:

* **Front-End:** ReactJS, JavaScript, TypeScript, TailwindCSS, HTML, CSS
* **Back-End:** Python, FastAPI, SQLModel

It ensures consistency, quality, and adherence to best practices across all our projects.

### Sources

This guide is built upon a foundation of established best practices and insights from experienced developers and resources, including:

* **Internal Best Practice Documents:** Synthesized knowledge from our existing `guide1.md`, `guide2.md`, `guide3.md`, `guide4.md`, and `guide5.md`.
* **React State Management & Hooks:** Insights from videos like:
    * [Learn useState In 15 Minutes - React Hooks Explained](https://www.youtube.com/watch?v=O6P86uwfdR0): Covering the fundamentals and usage of the `useState` hook in React.
    * [State Managers Are Making Your Code Worse In React](https://www.youtube.com/watch?v=VenLRGHx3D4): Discussing the evolution of state management in React, advocating for built-in tools like Context API, `useReducer`, and URL-based state over external libraries in many cases.
* **Programming Experience:** General wisdom from sources such as:
    * [5 Things I Have Learned from 10+ Years of Programming](https://www.youtube.com/watch?v=dQfqbL3GjYA): Offering key lessons learned over a decade of programming to foster a more enjoyable and effective development journey.
* **SQLModel Resources:** Best practices gathered from various web resources and documentation regarding SQLModel, FastAPI integration, and Pydantic v2.

## Using with Cursor

To leverage these guidelines directly within your Cursor IDE for features like `@rules` chat and code generation:

1.  **Locate/Create the Cursor Rules Directory:** In the root directory of your project, find or create a hidden directory named `.cursor`. Inside it, find or create another directory named `rules`.
2.  **Copy the Guide:** Place the `fullstack_guide.mdc` file from this repository into the `.cursor/rules/` directory.
