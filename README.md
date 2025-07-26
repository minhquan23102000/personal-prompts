# Personal Prompts & Workflows

A collection of AI agent prompts and workflows to enhance your development productivity and coding experience.

## 🚀 Quick Start

1. **Clone the repository:**
   ```bash
   cd your-project-folder  
   git clone https://github.com/minhquan23102000/personal-prompts.git .local

   ```

   or you can fork this repo for personal use and storage.

2. **How it works:**
   - **Rules**: Add specific coding rules to your AI agent
   - **Workflows**: Enable command-based workflow execution
   - **Generator**: Create custom prompts and workflows


## 🛠️ Setup Instructions

### Using Rules

Add rules to your AI agent's system prompt (Claude, Cursor, or other AI tools):

1. Copy the content from any rule file in the `rules/` directory
2. Paste it into your AI agent's system prompt
3. The agent will now follow those coding standards

### Using Workflows

Enable command-based workflow execution:

1. Add this to your AI agent's system prompt:
   ```
   When I type "COMMAND: {command-file}.md", you must read and follow the command inside the file for execution.
   ```

2. Execute workflows by typing:
   ```
   COMMAND: .local/workflows/{command-file}.md
   
   {Additional Context}
   ```

### Generating Custom Prompts

Create your own prompts and workflows:

1. Visit [Google AI Studio](https://aistudio.google.com/app/prompts/new_chat)
2. Use one of these system prompts:
   - `rules-workflow-generator.md` - Basic generator
   - `v2_rules-workflow-generator.md` - Enhanced generator
3. Input your requirements and generate custom prompts or workflows


---

**Happy coding! 🎉**






