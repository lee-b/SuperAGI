<h2>SuperAGI</h2>

<p align="center"><i>Open-source framework to build, manage and run useful Autonomous AI Agents</i></p>

### 💡 Features

- <b>Provision, Spawn & Deploy Autonomous AI Agents</b> - Create production-ready & scalable autonomous agents.
- <b>Extend Agent Capabilities with Toolkits</b> - Add Toolkits from our marketplace to your agent workflows.
- <b>Graphical User Interface</b> - Access your agents through a graphical user interface.
- <b>Action Console</b> - Interact with agents by giving them input and permissions.
- <b>Multiple Vector DBs</b> - Connect to multiple Vector DBs to enhance your agent’s performance.
- <b>Performance Telemetry</b> - Get insights into your agent’s performance and optimize accordingly.
- <b>Optimized Token Usage</b> - Control token usage to manage costs effectively.
- <b>Agent Memory Storage</b> - Enable your agents to learn and adapt by storing their memory.
- <b>Models</b> - Custom fine tuned models for business specific usecases.
- <b>Workflows</b> - Automate tasks with ease using ReAct LLM's predefined steps.

### 🛠 Toolkits

Toolkits allow SuperAGI Agents to interact with external systems and third-party plugins.


### Installation

1. Open your terminal and clone the SuperAGI repository.
```
git clone https://github.com/lee-b/SuperAGI.git 
```

2. Navigate to the cloned repository directory using the command:
```
cd SuperAGI
```
3. Create a copy of config_template.yaml, and name it config.yaml.

4. Ensure that Docker is installed on your system. You can download and install it from [docker.com](https://docs.docker.com/get-docker/).

5. Once you have Docker Desktop running, run the following command in the SuperAGI directory:

   a. For regular usage:
      ```
      docker compose -f docker-compose.yaml up --build
      ```

   b. If you want to use SuperAGI with Local LLMs and have GPU, run the following command:
      ```
      docker compose -f docker-compose-gpu.yml up --build
      ```


6. Open your web browser and navigate to http://localhost:3000 to access SuperAGI.


### ⚠️ Under Development!
This project is under active development and may still have issues. We appreciate your understanding and patience. If you encounter any problems, please check the open issues first. If your issue is not listed, kindly create a new issue detailing the error or problem you experienced. Thank you for your support!
