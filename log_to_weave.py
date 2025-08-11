import json
import weave

def log_trace_from_json(filename):
    with open(filename, "r") as f:
        trace_data = json.load(f)

    weave.init(project_name="handoff-demo")

    weave.publish(trace_data, name="agent_handoff_trace")

    print("Trace enviado para Weave com sucesso.")

if __name__ == "__main__":
    log_trace_from_json("handoff_trace.json")
