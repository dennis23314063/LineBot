from fsm import TocMachine
def multiple_machine():
    machine = TocMachine(
    states=["user", "menu", "introduction","draw","fsm"],
    transitions=[
        {
            "trigger": "advance",
            "source": "menu",
            "dest": "introduction",
            "conditions": "is_going_to_introduction",
        },
        {
            "trigger": "advance",
            "source": "menu",
            "dest": "menu",
            "conditions": "is_going_to_menu",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "menu",
            "conditions": "is_going_to_menu",
        },
        {
            "trigger": "go_back",
            "source":["introduction","fsm","draw"],
            "dest": "menu"
        },
        {
            "trigger": "advance",
            "source":"menu",
            "dest": "fsm",
            "conditions": "is_going_to_fsm",
        },
        {
            "trigger": "advance",
            "source":"menu",
            "dest": "draw",
            "conditions": "is_going_to_draw",
        },
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
    )
    return machine