from functions import update_system, install_packages, configure_git
from colorama import Fore, Style
from time import sleep


def main():
    print("========Pos-installation Script========")
    print(
        Fore.RED
        + "WARNING! THIS SCRIPT WAS MADE BASED ON UBUNTU 24.04 LTS. IT IS NOT GUARANTEED THAT IT WILL WORK ON ANOTHER LINUX DISTRO"
    )
    sleep(1)
    exec = input(Style.RESET_ALL + "Start script?(y/n) ")
    if exec.upper() == "Y":
        update_system()
        install_packages()
        configure_git()
        print(
            Fore.GREEN
            + "\n\nSUCESS! Now reboot your PC for apply all the changes."
            + Style.RESET_ALL
        )
        sleep(2)
        return
    else:
        return


if __name__ == "__main__":
    main()
