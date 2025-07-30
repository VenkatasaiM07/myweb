import subprocess

def run_git_command(command):
    """Run a Git command and return the output or error."""
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error:", e.stderr)

def show_menu():
    print("\nGit Advanced Operations - DevOps Day 5")
    print("1. Rebase a branch onto main")
    print("2. Cherry-pick a commit")
    print("3. Simulate a merge conflict")
    print("4. Resolve conflict and continue rebase")
    print("5. Exit")

def main():
    while True:
        show_menu()
        choice = input("Select an option: ")

        if choice == '1':
            branch = input("Enter the branch you want to rebase onto main: ")
            run_git_command(f"git checkout {branch}")
            run_git_command("git fetch origin")
            run_git_command("git rebase origin/main")

        elif choice == '2':
            commit_hash = input("Enter the commit hash to cherry-pick: ")
            run_git_command(f"git cherry-pick {commit_hash}")

        elif choice == '3':
            print("Simulating a merge conflict (requires manual setup)...")
            print("Make conflicting changes on two branches before using this.")

        elif choice == '4':
            print("Add and continue after resolving conflict...")
            run_git_command("git add .")
            run_git_command("git rebase --continue")

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
