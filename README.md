# Uillihans' Custom Hermes Web UI

This is my custom-crafted, vibe-coded Web UI for the **Hermes Agent**. 

It takes inspiration from the original design but has been customized to provide a streamlined, beautiful, and completely clean interface to interact with my AI agent.

## Key Customizations

- **Clean Selector Layout:** Corrected the view switcher layout under the `.main-content-split` wrapper so inactive panels (Skills, Memory, Tasks, Kanban, Logs) are correctly hidden, and only the active panel is visible in the main canvas.
- **Polished Main Dashboard:** Removed inline display constraints to ensure the dashboard toggles correctly inside the workspace split.
- **Standalone Package:** Optimized, fast, and structured for simple personal deployments on local port `8787`.

## How to Run the Web UI

1. Make sure your Hermes Agent is running.
2. Launch the bootstrap script from this folder:
   ```bash
   python3 bootstrap.py
   ```
3. Alternatively, launch the background daemon:
   ```bash
   ./ctl.sh start
   ```
4. Access your interface directly at **[http://127.0.0.1:8787](http://127.0.0.1:8787)**!
