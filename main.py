from cps7003.cps7003_assessment_2.tui import main_tui, employee_tui


def employee_system():
    employee_service = employeeService()

    selected = employee_tui.employee_menu()

    if selected == 1:
        role_name = role_tui.role_name()
        created_role = role_service.create_role(role_name)
        if created_role:
            role_tui.status(f"The {role_name} role has been created.")
        else:
            role_tui.status(f"The {role_name} could not be created.")
    else:
        role_tui.status("Invalid role action.")


def run():
    while True:

        selected = main_tui.main_menu()

        if selected == 1:
            role_system()
        else:
            main_tui.status("Invalid menu action.")


if __name__ == "__main__":
    run()
