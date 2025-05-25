import json
import os
from task_master_agent import TaskMasterAgent

def save_to_file(content, filename):
    """Save content to a file."""
    with open(filename, "w") as f:
        f.write(content)

def main():
    # Initialize TaskMasterAgent
    tm_agent = TaskMasterAgent()

    # Step 1: Initialize project
    project_context = "E-commerce web app with user authentication and payment integration"
    init_response = tm_agent.initialize_project(project_context)
    print("Step 1: Initialize Project Response")
    print(init_response)
    save_to_file(init_response, "tasks.json")
    print("\n---\n")

    # Step 2: Parse PRD
    prd_text = "Project: E-commerce Web App\nFeatures: User registration and login (OAuth and email/password), Product listing with search and filter, Shopping cart and checkout with Stripe integration, Admin dashboard for managing products"
    project_context = "Node.js backend, React frontend, MongoDB database"
    parse_response = tm_agent.parse_prd(prd_text, project_context)
    print("Step 2: Parse PRD Response")
    print(parse_response)
    # Update tasks.json with tasks
    with open("tasks.json", "r") as f:
        tasks_data = json.load(f)
    tasks_data["tasks"] = json.loads(parse_response)
    with open("tasks.json", "w") as f:
        json.dump(tasks_data, f)
    print("\n---\n")

    # Step 3: List tasks
    with open("tasks.json", "r") as f:
        tasks_data = json.load(f)
    task_list_json = json.dumps(tasks_data["tasks"])
    list_response = tm_agent.list_tasks(task_list_json)
    print("Step 3: List Tasks Response")
    print(list_response)
    save_to_file(list_response, "tasks.md")
    print("\n---\n")

    # Step 4: View next task
    view_next_response = tm_agent.view_next_task(task_list_json)
    print("Step 4: View Next Task Response")
    print(view_next_response)
    save_to_file(view_next_response, "next_task.json")
    print("\n---\n")

    # Step 5: Generate task files
    implementation_context = "Use Express for the server, follow REST API best practices"
    generate_response = tm_agent.generate_task_files(task_list_json, project_context, implementation_context)
    print("Step 5: Generate Task Files Response")
    print(generate_response)
    # Split and save markdown files
    task_files = generate_response.split("---")
    for i, task_content in enumerate(task_files, 1):
        if task_content.strip():
            save_to_file(task_content.strip(), f"task-{i}.md")
    print("\n---\n")

    # Step 6: Expand tasks
    task_id = "3"
    num_subtasks = 3
    expansion_context = "Focus on security best practices for OAuth and password hashing"
    expand_response = tm_agent.expand_tasks(task_list_json, task_id, num_subtasks, expansion_context)
    print("Step 6: Expand Tasks Response")
    print(expand_response)
    # Append subtasks to tasks.json
    with open("tasks.json", "r") as f:
        tasks_data = json.load(f)
    tasks_data["tasks"].extend(json.loads(expand_response))
    with open("tasks.json", "w") as f:
        json.dump(tasks_data, f)
    print("\n---\n")

    # Step 7: Update tasks
    task_id = "2"
    change_context = "Switch from MongoDB to PostgreSQL"
    update_response = tm_agent.update_tasks(task_list_json, task_id, change_context)
    print("Step 7: Update Tasks Response")
    print(update_response)
    # Update tasks in tasks.json
    with open("tasks.json", "r") as f:
        tasks_data = json.load(f)
    tasks_data["tasks"] = json.loads(update_response)
    with open("tasks.json", "w") as f:
        json.dump(tasks_data, f)
    print("\n---\n")

if __name__ == "__main__":
    main()