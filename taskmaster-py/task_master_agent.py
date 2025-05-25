import json
import os
from dotenv import load_dotenv
from autogen import UserProxyAgent, AssistantAgent
from task_master import TaskMaster

class TaskMasterAgent:
    def __init__(self):
        """Initialize TaskMasterAgent with an AutoGen 0.5.7 agent and TaskMaster."""
        # Load environment variables from .env
        load_dotenv()
        
        # Get LLM configuration
        api_key = os.getenv("LLM_API_KEY")
        model = os.getenv("LLM_MODEL")
        api_base = os.getenv("LLM_API_BASE")
        api_provider = os.getenv("LLM_PROVIDER")
        
        if not api_key: raise Exception("LLM_API_KEY not defined")
        if not model: raise Exception("LLM_MODEL not defined")
        if not api_base: raise Exception("LLM_API_BASE not defined")
        if not api_provider: raise Exception("LLM_PROVIDER not defined")

        # Configure LLM for AutoGen 0.5.7
        config_list = [{
            "model": model,
            "api_key": api_key,
            "base_url": api_base,
            "api_type": api_provider
        }]
        
        # Initialize AutoGen agents
        self.user_proxy = UserProxyAgent(
            name="UserProxy",
            human_input_mode="NEVER",
            max_consecutive_auto_reply=0,
            code_execution_config=False
        )
        
        self.assistant = AssistantAgent(
            name="Assistant",
            llm_config={"config_list": config_list},
            system_message="You are a task management assistant. Provide precise, formatted responses as instructed in the prompts, without additional explanations or comments."
        )
        
        # Initialize TaskMaster
        self.task_master = TaskMaster()

    def _call_llm(self, prompt):
        """
        Helper method to make a single LLM call using AutoGen.
        
        Args:
            prompt (str): The prompt to send to the LLM.
        
        Returns:
            str: The LLM's response content.
        """
        response = self.user_proxy.initiate_chat(
            recipient=self.assistant,
            message=prompt,
            clear_history=True,
            silent=True
        )
        return response.chat_history[-1]["content"]

    def initialize_project(self, project_context):
        """
        Initialize a project configuration using the LLM.
        
        Args:
            project_context (str): High-level project description.
        
        Returns:
            str: LLM response (JSON string for tasks.json).
        """
        prompt = self.task_master.initialize_project(project_context)
        return self._call_llm(prompt)

    def parse_prd(self, prd_text, project_context):
        """
        Parse a PRD to create a task list using the LLM.
        
        Args:
            prd_text (str): Full PRD text.
            project_context (str): Project tech stack and context.
        
        Returns:
            str: LLM response (JSON array for tasks.json).
        """
        prompt = self.task_master.parse_prd(prd_text, project_context)
        return self._call_llm(prompt)

    def list_tasks(self, task_list_json=None, project_context=None):
        """
        List all tasks in a markdown table using the LLM.
        
        Args:
            task_list_json (str, optional): JSON string of the task list.
            project_context (str, optional): Project context for sample tasks.
        
        Returns:
            str: LLM response (markdown table for tasks.md).
        """
        prompt = self.task_master.list_tasks(task_list_json, project_context)
        return self._call_llm(prompt)

    def view_next_task(self, task_list_json=None, project_context=None):
        """
        Identify the next actionable task using the LLM.
        
        Args:
            task_list_json (str, optional): JSON string of the task list.
            project_context (str, optional): Project context for sample tasks.
        
        Returns:
            str: LLM response (JSON object for next task).
        """
        prompt = self.task_master.view_next_task(task_list_json, project_context)
        return self._call_llm(prompt)

    def generate_task_files(self, task_list_json=None, project_context=None, implementation_context=None):
        """
        Generate markdown files for each task using the LLM.
        
        Args:
            task_list_json (str, optional): JSON string of the task list.
            project_context (str, optional): Project context for sample tasks.
            implementation_context (str, optional): Implementation guidance.
        
        Returns:
            str: LLM response (markdown content for task files).
        """
        prompt = self.task_master.generate_task_files(task_list_json, project_context, implementation_context)
        return self._call_llm(prompt)

    def expand_tasks(self, task_list_json, task_id, num_subtasks, expansion_context):
        """
        Expand a task into subtasks using the LLM.
        
        Args:
            task_list_json (str): JSON string of the task list.
            task_id (str): ID of the task to expand.
            num_subtasks (int): Number of subtasks to generate.
            expansion_context (str): Context for subtask creation.
        
        Returns:
            str: LLM response (JSON array for subtasks).
        """
        prompt = self.task_master.expand_tasks(task_list_json, task_id, num_subtasks, expansion_context)
        return self._call_llm(prompt)

    def update_tasks(self, task_list_json, task_id, change_context):
        """
        Update tasks from a specified ID using the LLM.
        
        Args:
            task_list_json (str): JSON string of the task list.
            task_id (str): ID of the task to start updating from.
            change_context (str): Description of the change.
        
        Returns:
            str: LLM response (JSON array for updated tasks).
        """
        prompt = self.task_master.update_tasks(task_list_json, task_id, change_context)
        return self._call_llm(prompt)