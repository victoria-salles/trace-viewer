import json

def load_trace(filename):
    with open(filename, "r") as f:
        return json.load(f)

def display_trace(trace, agent_filter=None):
    for event in trace:
        agent = event["agent"]
        if agent_filter and agent_filter.lower() not in agent.lower():
            continue
        timestamp = event["timestamp"]
        event_type = event["event"]
        message = event.get("message", "")
        reason = event.get("reason", "")
        extra = message or reason or str(event)
        print(f"[{timestamp}] {agent} - {event_type}: {extra}")

def list_agents(trace):
    agents = sorted(set(event["agent"] for event in trace))
    print("\n Agents in trace:")
    for a in agents:
        print(f" - {a}")

def main():
    trace = load_trace("handoff_trace.json")
    print("\n Full Event Trace:\n")
    display_trace(trace)

    while True:
        print("\n Filter options:")
        print("1. Show events for a specific agent")
        print("2. List all agents")
        print("3. Show full trace again")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            agent = input("Enter agent name or keyword (e.g., AI_Assistant): ")
            print(f"\n Events for agent: {agent}\n")
            display_trace(trace, agent_filter=agent)
        elif choice == "2":
            list_agents(trace)
        elif choice == "3":
            display_trace(trace)
        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
