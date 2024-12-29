from functions import (
    preparing_system,
    install_packages,
    chrome_install,
    flatpak_enable,
    remove_packages,
    install_miniconda,
    configure_git,
    tweaks,
    system_cleanning,
)
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
        preparing_system()
        install_packages()
        chrome_install()
        flatpak_enable()
        remove_packages()
        install_miniconda()
        configure_git()
        tweaks()
        system_cleanning()
        print(
            Fore.GREEN
            + "\n\nSUCESS! Now reboot your PC for apply all the changes."
            + Style.RESET_ALL
        )
        print("========Script End========")
        sleep(2)
        return
    else:
        print("========Script End========")
        sleep(0.6)
        return


if __name__ == "__main__":
    main()
