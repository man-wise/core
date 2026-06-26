from core.graph.graph import build_graph
from core.utils.dicts import AgentState
from core.utils.console_utils import console_utils
from core.utils.config_handler import config

def run_app():
    model_config = config()
    app = build_graph(model_config)
    console = console_utils(model_config)

    state: AgentState = {"messages": [], "logger": console}

    console.release_banner()

    while True:
        input_text = console.get_user_input()
        if input_text == "exit" or input_text == "/quit":
            break
        
        state["messages"].append({
            "role": "user",
            "content": input_text
        })

        state = app.invoke(state)