from subprocess import run, CalledProcessError
from time import sleep
from colorama import Fore, Style


DOWNLOADS_FOLDER = "${HOME}/posinstfiles/"
CHROME_LINK = (
    "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"
)
CONDA_LINK = "https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh"


def run_command(command):
    try:
        print(Fore.GREEN + f"Running: {command}" + Style.RESET_ALL)
        sleep(1)
        run(command, shell=True, check=True)
    except CalledProcessError as e:
        print(Fore.RED + f"Error while running: {command}\n{e}" + Style.RESET_ALL)


def preparing_system():
    print("=======Preparing System========")
    print(Fore.CYAN + "Running system update..." + Style.RESET_ALL)
    run_command("sudo apt update && sudo apt dist-upgrade -y")
    print(Fore.CYAN + "Creating temporary files..." + Style.RESET_ALL)
    run_command(f"mkdir {DOWNLOADS_FOLDER}")
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
                print("==================================")
                return
            print(
                Fore.CYAN
                + f"Installing the following packages: {', '.join(packages)}"
                + Style.RESET_ALL
            )
            sleep(2)
            run_command(f"sudo apt install -y {' '.join(packages)}")
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


def chrome_install():
    exec = input(Fore.YELLOW + "Start chrome installation?(y/n)" + Style.RESET_ALL)
    if exec.upper() == "Y":
        print("=======Chrome Install========")
        print(Fore.CYAN + "Installing wget..." + Style.RESET_ALL)
        run_command("sudo apt install wget")
        print(Fore.CYAN + "Downloading chrome .deb file..." + Style.RESET_ALL)
        run_command(f"wget {CHROME_LINK} -c -P {DOWNLOADS_FOLDER} ")
        run_command(f"sudo apt -f {DOWNLOADS_FOLDER}/google-chrome*.deb")
    else:
        print("Skipping chrome installation...")
        sleep(0.6)
        return


def flatpak_enable():
    exec = input(Fore.YELLOW + "Start flatpak enable?(y/n)" + Style.RESET_ALL)
    if exec.upper() == "Y":
        print("=======Flatpak Enable========")
        run_command(
            "sudo apt install flatpak -y && flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo"
        )
    else:
        print("Skipping flatpak enable...")
        sleep(0.6)
        return


def remove_packages():
    exec = input(Fore.YELLOW + "Start removing packages?(y/n)" + Style.RESET_ALL)
    if exec.upper() == "Y":
        print("=======Removing Packages========")
        try:
            with open("unpackages.txt", "r") as file:
                packages = [linha.strip() for linha in file if linha.strip()]
            if not packages:
                print(Fore.CYAN + "No packages found!")
                sleep(1)
                print("==================================")
                return
            print(
                Fore.CYAN
                + f"Removing the following packages: {', '.join(packages)}"
                + Style.RESET_ALL
            )
            sleep(2)
            run_command(f"sudo apt purge -y {' '.join(packages)}")
            print("==================================")

        except FileNotFoundError:
            print(Fore.RED + f"Error: Packages list file not found!" + Style.RESET_ALL)
            sleep(1)
            print("==================================")
            return
    else:
        print("Skipping removing packages...")
        sleep(0.6)
        return


def install_miniconda():
    exec = input(Fore.YELLOW + "Start miniconda installation?(y/n) " + Style.RESET_ALL)
    if exec.upper() == "Y":
        print("========Miniconda Installation========")
        print(Fore.CYAN + "Installing curl..." + Style.RESET_ALL)
        run_command("sudo apt install -y curl")
        print(Fore.CYAN + "Downloading 'miniconda.sh'..." + Style.RESET_ALL)
        run_command(f"curl -O {CONDA_LINK} --output-dir {DOWNLOADS_FOLDER}")
        print(Fore.CYAN + "Running 'miniconda.sh'..." + Style.RESET_ALL)
        run_command(f"bash {DOWNLOADS_FOLDER}/Miniconda3-latest-Linux-x86_64.sh")
    else:
        print("Skipping miniconda installation...")
        sleep(0.6)
        return


def configure_git():
    exec = input(Fore.YELLOW + "Start git configuration?(y/n) " + Style.RESET_ALL)
    if exec.upper() == "Y":
        print("========Git Config========")
        print(Fore.CYAN + "Installing git..." + Style.RESET_ALL)
        run_command("sudo apt install -y git")
        name = str(input("Insert your git username: "))
        email = str(input("Insert your git email: "))
        run_command(f"git config --global user.name '{name}'")
        run_command(f"git config --global user.email '{email}'")
        print("==================================")
    else:
        print("Skipping git configuration...")
        sleep(0.6)
        return


def tweaks():
    exec = input(Fore.YELLOW + "Start system tweaks?(y/n)" + Style.RESET_ALL)
    if exec.upper() == "Y":
        print("=======Personal Tweaks========")
        run_command(
            """sudo awk '/[General]/ && !added {print $0; print "Disable=Handsfree"; added=1; next} 1' /etc/bluetooth/main.conf > temp.b
"""
        )
        run_command("sudo rm /etc/bluetooth/main.conf")
        run_command("sudo mv temp.b /etc/bluetooth/main.conf")
    else:
        print("Skipping system tweaks...")
        sleep(0.6)
        return


def system_cleanning():
    print("========System Cleaner========")
    run_command(
        "sudo apt update && sudo apt autoremove -y && sudo apt autoclean -y && sudo apt clean -y"
    )
    print("==================================")
