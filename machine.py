from fsm import TocMachine
def multiple_machine():
    machine = TocMachine(
    states=["user", "menu", "introduction","draw","fsm"],
    transitions=[
        {
            "trigger": "advance",
            "source": "user",
            "dest": "menu",
            "conditions": "is_going_to_menu",
        },
        {
            "trigger": "advance",
            "source": "menu",
            "dest": "introduction",
            "conditions": "is_going_to_introduction",
        },
        {
            "trigger": "go_back",
            "source":["introduction","fsm","draw"],
            "dest": "user"
        },
        # {
        #     "trigger": "go_back",
        #     "source":"draw",
        #     "dest": "draw"
        # },
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
        # {
        #     "trigger": "advance",
        #     "source":"draw",
        #     "dest": "menu",
        #     "conditions": "is_going_to_menu",
        # },
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
    )
    return machine