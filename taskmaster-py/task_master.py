python
import json

class TaskMaster:
    def __init__(self):
        """Initialize the TaskMaster class."""
        pass

    def initialize_project(self, project_context):
        """
        Generate a prompt to initialize a project configuration.
        
        Args:
            project_context (str): High-level project description (e.g., 'E-commerce web app with user authentication').
        
        Returns:
            str: Formatted ChatGPT prompt for project initialization.
        """
        prompt = f"""
I want to initialize a project plan for a software development project, acting as an AI task management tool. Prompt me to provide the following details: project name, description, primary programming language, database choice, and deployment platform. Use the provided context: {project_context}. After I provide the details, generate a JSON object formatted exactly as follows, with no additional text or comments, so I can copy-paste it into a `tasks.json` file:
```json
{{
  "projectName": "<provided project name>",
  "description": "<provided description>",
  "language": "<provided language>",
  "database": "<provided database>",
  "deployment": "<provided deployment platform>",
  "tasks": []
}}
Ensure the JSON is minified (no extra whitespace) and valid for direct use in a codebase file. Do not include any explanation or additional output beyond the JSON object.
"""
        return prompt

def parse_prd(self, prd_text, project_context):
    """
    Generate a prompt to parse a PRD and create a task list.
    
    Args:
        prd_text (str): Full text of the PRD (e.g., 'Project: E-commerce Web App, Features: User registration...').
        project_context (str): Project tech stack and context (e.g., 'Node.js backend, React frontend, MongoDB').
    
    Returns:
        str: Formatted ChatGPT prompt for parsing PRD.
    """
    prompt = f"""
Act as an AI task management tool to parse a Product Requirements Document (PRD) and generate a structured task list for my project. The PRD content is: {prd_text}. Use the project context: {project_context}. Analyze the PRD and generate a JSON task list formatted exactly as follows, with no additional text or comments, so I can copy-paste it into the tasks array of a tasks.json file:
json
[
  {{
    "id": 1,
    "description": "<clear, actionable task description>",
    "status": "pending",
    "dependencies": [<array of task IDs, e.g., 0 for no dependencies>]
  }},
  ...
]
Ensure each task has a sequential integer ID starting from 1, a clear description aligned with the PRD and project context, status set to "pending", and dependencies as an array of prior task IDs based on logical order (e.g., database setup before authentication). The JSON must be minified (no extra whitespace) and valid for direct insertion into a codebase file. Do not include explanations or additional output beyond the JSON array.
"""
        return prompt

def list_tasks(self, task_list_json=None, project_context=None):
    """
    Generate a prompt to list all tasks in a markdown table.
    
    Args:
        task_list_json (str, optional): JSON string of the task list (e.g., '[{"id": 1, "description": ...}]').
        project_context (str, optional): Project context for sample tasks if task_list_json is None.
    
    Returns:
        str: Formatted ChatGPT prompt for listing tasks.
    """
    task_list_str = task_list_json if task_list_json else ""
    project_context_str = project_context if project_context else ""
    prompt = f"""
Act as an AI task management tool to list all tasks in my project plan. The current task list is: {task_list_str}. If no task list is provided, generate a sample task list for a project with context: {project_context_str} using the JSON format:
json
[
  {{
    "id": 1,
    "description": "<actionable task>",
    "status": "pending",
    "dependencies": []
  }},
  ...
]
Output the tasks in a markdown table formatted exactly as follows, with no additional text or comments, so I can copy-paste it into a documentation file (e.g., tasks.md):
markdown

| ID  | Description  | Status | Dependencies |
|-----|--------------|--------|--------------|
|<id> | <description>|<status>| <dependencies as comma-separated IDs> |
...

Ensure the table lists all tasks with their IDs, descriptions, statuses, and dependencies (as comma-separated IDs, e.g., "1,2" or "None" if empty). The output must be clean and ready for direct use in a markdown file.
"""
        return prompt

def view_next_task(self, task_list_json=None, project_context=None):
    """
    Generate a prompt to identify the next actionable task.
    
    Args:
        task_list_json (str, optional): JSON string of the task list (e.g., '[{"id": 1, "description": ...}]').
        project_context (str, optional): Project context for sample tasks if task_list_json is None.
    
    Returns:
        str: Formatted ChatGPT prompt for viewing the next task.
    """
    task_list_str = task_list_json if task_list_json else ""
    project_context_str = project_context if project_context else ""
    prompt = f"""
Act as an AI task management tool to identify the next actionable task in my project plan. The current task list is: {task_list_str}. If no task list is provided, generate a sample task list for a project with context: {project_context_str} using the JSON format:
json
[
  {{
    "id": 1,
    "description": "<actionable task>",
    "status": "pending",
    "dependencies": []
  }},
  ...
]
Analyze the tasks, considering their 'status' ("pending" or "completed") and 'dependencies' (task IDs that must be completed). Output the next pending task with all dependencies resolved in the following JSON format, with no additional text or comments, so I can copy-paste it into a task management system:
json
{{
  "id": <task ID>,
  "description": "<task description>",
  "status": "<task status>",
  "dependencies": [<array of dependency IDs>]
}}
If no task is ready (e.g., dependencies not met), output an empty JSON object {{}}. Ensure the JSON is minified and valid for direct use.
"""
        return prompt

def generate_task_files(self, task_list_json=None, project_context=None, implementation_context=None):
    """
    Generate a prompt to create markdown files for each task.
    
    Args:
        task_list_json (str, optional): JSON string of the task list (e.g., '[{"id": 1, "description": ...}]').
        project_context (str, optional): Project context for sample tasks if task_list_json is None.
        implementation_context (str, optional): Specific implementation guidance (e.g., 'Use Express for the server').
    
    Returns:
        str: Formatted ChatGPT prompt for generating task files.
    """
    task_list_str = task_list_json if task_list_json else ""
    project_context_str = project_context if project_context else ""
    implementation_context_str = implementation_context if implementation_context else ""
    prompt = f"""
Act as an AI task management tool to generate detailed implementation guides for each task in my project plan, formatted as markdown files. The current task list is: {task_list_str}. If no task list is provided, generate a sample task list for a project with context: {project_context_str} using the JSON format:
json
[
  {{
    "id": 1,
    "description": "<actionable task>",
    "status": "pending",
    "dependencies": []
  }},
  ...
]
For each task, generate a markdown file content formatted exactly as follows, with no additional text or comments, so I can copy-paste each into a separate file (e.g., task-1.md):
markdown
# Task <id>: <description>

**Status**: <status>  
**Dependencies**: <comma-separated dependency IDs or "None">

## Implementation Steps
- <Step 1: Detailed action aligned with project context>
- <Step 2: ...>
...

## Technologies
- <Relevant technology 1, e.g., Node.js, Express>
- <Relevant technology 2, e.g., MongoDB>

## Notes
- <Any relevant notes, e.g., reference to <specific file or codebase element>>
Output each task’s markdown content separated by a line of --- to indicate different files. Align steps and technologies with the project context: {implementation_context_str}. If tasks reference specific files, note them as placeholders (e.g., '<file reference>'). Ensure the output is clean and ready for direct use in markdown files.
"""
        return prompt

def expand_tasks(self, task_list_json, task_id, num_subtasks, expansion_context):
    """
    Generate a prompt to expand a task into subtasks.
    
    Args:
        task_list_json (str): JSON string of the task list (e.g., '[{"id": 1, "description": ...}]').
        task_id (str): ID of the task to expand (e.g., '3').
        num_subtasks (int): Number of subtasks to generate.
        expansion_context (str): Context for subtask creation (e.g., 'Focus on security best practices').
    
    Returns:
        str: Formatted ChatGPT prompt for expanding tasks.
    """
    prompt = f"""
Act as an AI task management tool to expand a specific task into subtasks. The current task list is: {task_list_json}. Focus on the task with ID {task_id}. If no task list is provided, generate a sample task list for a project with context: <PLACEHOLDER: e.g., 'E-commerce web app with Node.js and MongoDB'> using the JSON format:
json
[
  {{
    "id": 1,
    "description": "<actionable task>",
    "status": "pending",
    "dependencies": []
  }},
  ...
]
Break the specified task into {num_subtasks} subtasks, using the additional context: {expansion_context}. Generate subtasks in the following JSON format, with no additional text or comments, so I can copy-paste them into my tasks.json file:
json
[
  {{
    "id": "<parent-id>.1",
    "description": "<subtask description>",
    "status": "pending",
    "dependencies": [<parent task ID or subtask IDs, e.g., "3" or "3.1"]>
  }},
  ...
]
Ensure subtask IDs are formatted as <parent-id>.<subtask-number> (e.g., 3.1, 3.2), descriptions are actionable and aligned with the context, status is "pending", and dependencies reference the parent task or prior subtasks. The JSON must be minified and valid for direct use in a codebase file.
"""
        return prompt

def update_tasks(self, task_list_json, task_id, change_context):
    """
    Generate a prompt to update tasks from a specified ID.
    
    Args:
        task_list_json (str): JSON string of the task list (e.g., '[{"id": 1, "description": ...}]').
        task_id (str): ID of the task to start updating from (e.g., '2').
        change_context (str): Description of the change (e.g., 'Switch from MongoDB to PostgreSQL').
    
    Returns:
        str: Formatted ChatGPT prompt for updating tasks.
    """
    prompt = f"""
Act as an AI task management tool to update my project plan’s tasks due to a change in requirements. The current task list is: {task_list_json}. If no task list is provided, generate a sample task list for a project with context: <PLACEHOLDER: e.g., 'E-commerce web app with Node.js and MongoDB'> using the JSON format:
json
[
  {{
    "id": 1,
    "description": "<actionable task>",
    "status": "pending",
    "dependencies": []
  }},
  ...
]
Start updating from the task with ID {task_id} and apply the change: {change_context}. Re-generate all tasks from the specified ID onward, preserving the exact JSON structure (id, description, status, dependencies) of tasks before it. Output the updated task list in the following JSON format, with no additional text or comments, so I can copy-paste it into my tasks.json file:
json
[
  {{
    "id": <task ID>,
    "description": "<task description>",
    "status": "<task status>",
    "dependencies": [<dependency IDs>]
  }},
  ...
]
Ensure the JSON is minified, maintains sequential IDs for new tasks, aligns with the project context, and includes logical dependencies. The output must be valid for direct use in a codebase file.
"""
        return prompt

import json
from task_master import TaskMaster

def main():
    # Initialize TaskMaster
    tm = TaskMaster()

    # Step 1: Initialize project
    project_context = "E-commerce web app with user authentication and payment integration"
    init_prompt = tm.initialize_project(project_context)
    print("Step 1: Initialize Project Prompt")
    print(init_prompt)
    print("\n---\n")
    # Assume ChatGPT output is saved to tasks.json:
    # {"projectName":"E-commerce Web App","description":"Build a responsive e-commerce platform","language":"Node.js","database":"MongoDB","deployment":"Vercel","tasks":[]}

    # Step 2: Parse PRD
    prd_text = "Project: E-commerce Web App\nFeatures: User registration and login (OAuth and email/password), Product listing with search and filter, Shopping cart and checkout with Stripe integration, Admin dashboard for managing products"
    project_context = "Node.js backend, React frontend, MongoDB database"
    parse_prompt = tm.parse_prd(prd_text, project_context)
    print("Step 2: Parse PRD Prompt")
    print(parse_prompt)
    print("\n---\n")
    # Assume ChatGPT output is saved to tasks.json:
    sample_tasks = [
        {"id": 1, "description": "Set up Node.js server", "status": "pending", "dependencies": []},
        {"id": 2, "description": "Configure MongoDB database", "status": "pending", "dependencies": [1]},
        {"id": 3, "description": "Implement user authentication", "status": "pending", "dependencies": [2]},
        {"id": 4, "description": "Develop React product listing", "status": "pending", "dependencies": [1]}
    ]
    # Save to tasks.json
    with open("tasks.json", "w") as f:
        json.dump({"projectName": "E-commerce Web App", "description": "Build a responsive e-commerce platform", "language": "Node.js", "database": "MongoDB", "deployment": "Vercel", "tasks": sample_tasks}, f)

    # Step 3: List tasks
    with open("tasks.json", "r") as f:
        tasks_data = json.load(f)
    task_list_json = json.dumps(tasks_data["tasks"])
    list_prompt = tm.list_tasks(task_list_json)
    print("Step 3: List Tasks Prompt")
    print(list_prompt)
    print("\n---\n")
    # Assume ChatGPT output is saved to tasks.md

    # Step 4: View next task
    view_next_prompt = tm.view_next_task(task_list_json)
    print("Step 4: View Next Task Prompt")
    print(view_next_prompt)
    print("\n---\n")
    # Assume ChatGPT output: {"id":1,"description":"Set up Node.js server","status":"pending","dependencies":[]}

    # Step 5: Generate task files
    implementation_context = "Use Express for the server, follow REST API best practices"
    generate_prompt = tm.generate_task_files(task_list_json, project_context, implementation_context)
    print("Step 5: Generate Task Files Prompt")
    print(generate_prompt)
    print("\n---\n")
    # Assume ChatGPT output is saved to task-1.md, task-2.md, etc.

    # Step 6: Expand tasks
    task_id = "3"
    num_subtasks = 3
    expansion_context = "Focus on security best practices for OAuth and password hashing"
    expand_prompt = tm.expand_tasks(task_list_json, task_id, num_subtasks, expansion_context)
    print("Step 6: Expand Tasks Prompt")
    print(expansion_context)
    print("\n---\n")
    # Assume ChatGPT output is appended to tasks.json

    # Step 7: Update tasks
    task_id = "2"
    change_context = "Switch from MongoDB to PostgreSQL"
    update_prompt = tm.update_tasks(task_list_json, task_id, change_context)
    print("Step 7: Update Tasks Prompt")
    print(update_prompt)
    print("\n---\n")
    # Assume ChatGPT output replaces tasks in tasks.json

if __name__ == "__main__":
    main()

