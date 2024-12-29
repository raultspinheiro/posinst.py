import subprocess
from time import sleep
from colorama import Fore, Style


def run_command(command):
    try:
        print(Fore.GREEN + f"Running: {command}" + Style.RESET_ALL)
        sleep(1)
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"Error while running: {command}\n{e}" + Style.RESET_ALL)


def update_system():
    print("=======Running System Update========")
    run_command("sudo apt update && sudo apt dist-upgrade -y")
    print("==================================")


def install_packages():
    exec = input(Fore.YELLOW + "Start packages installation?(y/n)" + Style.RESET_ALL)
    if exec.upper() == "Y":
        print("=======Installing Packages========")
        try:
            with open("packages.txt", "r") as file:
                packages = [linha.strip() for linha in file if linha.strip()]
            if not packages:
                print(Fore.CYAN + "No packages found!")
                sleep(1)
                run_command(f"Sudo apt install -y git")
                print("==================================")
                return
            print(
                Fore.CYAN
                + f"Installing the following packages: {', '.join(packages)}"
                + Style.RESET_ALL
            )
            sleep(2)
            run_command(f"sudo apt install -y git {' '.join(packages)}")
            print("==================================")

        except FileNotFoundError:
            print(Fore.RED + f"Error: Packages list file not found!" + Style.RESET_ALL)
            sleep(1)
            print("==================================")
            return
    else:
        print("Skipping packages installation...")
        sleep(0.6)
        return


def configure_git():
    exec = input(Fore.YELLOW + "Start git configuration?(y/n) " + Style.RESET_ALL)
    if exec.upper() == "Y":
        print("========Git Config========")
        name = str(input("Insert your git username: "))
        email = str(input("Insert your git email: "))
        run_command(f"git config --global user.name '{name}'")
        run_command(f"git config --global user.email '{email}'")
        print("==================================")
    else:
        print("Skipping git configuration...")
        sleep(0.6)
        return
