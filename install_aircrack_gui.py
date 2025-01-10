import os
import subprocess
import sys

def ensure_tkinter_installed():
    """Ensure tkinter is installed."""
    try:
        # Attempt to import tkinter to check its availability
        import tkinter
    except ModuleNotFoundError:
        print("tkinter not found. Installing...")
        try:
            subprocess.run(["sudo", "apt", "update"], check=True)
            subprocess.run(["sudo", "apt", "install", "-y", "python3-tk"], check=True)
            print("tkinter installed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to install tkinter: {e}")
            sys.exit(1)

# Ensure tkinter is installed before importing
ensure_tkinter_installed()

# Now import tkinter
import tkinter as tk
from tkinter import messagebox


def install_dependencies():
    try:
        dependencies = [
            "autoconf",
            "automake",
            "libtool",
            "shtool",
            "libssl-dev",
            "pkg-config",
            "libgcrypt20-dev",
        ]
        subprocess.run(["sudo", "apt", "update"], check=True)
        subprocess.run(["sudo", "apt", "install", "-y"] + dependencies, check=True)
        messagebox.showinfo("Success", "Dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to install dependencies: {e}")


def install_aircrack():
    try:
        # Download the Aircrack-ng source
        subprocess.run(["wget", "https://download.aircrack-ng.org/aircrack-ng-1.7.tar.gz"], check=True)

        # Extract the tarball
        subprocess.run(["tar", "-zxvf", "aircrack-ng-1.7.tar.gz"], check=True)

        # Navigate into the directory
        os.chdir("aircrack-ng-1.7")

        # Run installation commands
        subprocess.run(["autoreconf", "-i"], check=True)
        subprocess.run(["./configure", "--with-experimental"], check=True)
        subprocess.run(["make"], check=True)
        subprocess.run(["sudo", "make", "install"], check=True)
        subprocess.run(["sudo", "ldconfig"], check=True)

        # Go back to the parent directory
        os.chdir("..")

        messagebox.showinfo("Success", "Aircrack-ng installed successfully.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to install Aircrack-ng: {e}")
    except FileNotFoundError as e:
        messagebox.showerror("Error", f"File not found during installation: {e}")


if __name__ == "__main__":
    # Create the GUI
    root = tk.Tk()
    root.title("Aircrack-ng Installer")

    tk.Label(root, text="Install Aircrack-ng and Dependencies", font=("Arial", 14)).pack(pady=10)

    tk.Button(root, text="Install Dependencies", command=install_dependencies, width=30).pack(pady=10)
    tk.Button(root, text="Install Aircrack-ng", command=install_aircrack, width=30).pack(pady=10)


    root.mainloop()
