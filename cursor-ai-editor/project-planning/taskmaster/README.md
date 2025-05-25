# 🤖 TaskMaster - AI-Powered Task Management

An intelligent task management system designed to work seamlessly with AI development tools.

## 📁 Contents

- **`task_master.py`** - Core TaskMaster implementation
- **`task_master_agent.py`** - AI agent for task management
- **`demo_task_master_agent.py`** - Demo and example usage
- **`requirements.txt`** - Python dependencies
- **`template.env`** - Environment configuration template

## 🚀 Quick Start

### Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Copy and configure environment
cp template.env .env
# Edit .env with your configuration
```

### Running the Demo

```bash
python demo_task_master_agent.py
```

## 🎯 Features

- **Intelligent Task Breakdown** - Automatically decompose complex projects
- **AI-Assisted Planning** - Get smart suggestions for prioritization
- **Workflow Integration** - Designed to work with Cursor and other AI tools
- **Flexible Architecture** - Easily extensible and customizable

## 🔧 Configuration

Copy `template.env` to `.env` and configure your settings:

- API keys for AI services
- Database connections (if applicable)
- Custom workflow preferences

## 💡 Usage Examples

### Basic Task Management

```python
from task_master import TaskMaster

tm = TaskMaster()
project = tm.create_project("My AI Project")
tasks = tm.break_down_project(project)
```

### AI Agent Integration

```python
from task_master_agent import TaskMasterAgent

agent = TaskMasterAgent()
agent.process_project_requirements("Build a web app with React and FastAPI")
```

## 🔗 Integration with Cursor

Use the TaskMaster system alongside Cursor rules for:

- Context-aware code generation
- Task-driven development workflows
- Automatic progress tracking
- Intelligent project planning

## 🛠️ Extending TaskMaster

The system is designed to be extensible. You can:

- Add custom task types
- Integrate with external project management tools
- Customize AI prompting strategies
- Build domain-specific workflows
