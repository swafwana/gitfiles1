# Function to input a list of integers
def input_list():
    return list(map(int, input("Enter a list of integers (space-separated): ").split()))

# Function to check if the lists are of the same length
def check_length(list1, list2):
    return len(list1) == len(list2)

# Function to check if the sums of both lists are the same
def check_sum(list1, list2):
    return sum(list1) == sum(list2)

# Function to check if any value occurs in both lists
def check_common_values(list1, list2):
    return bool(set(list1) & set(list2))

def menu():
    # Enter two lists
    list1 = input_list()
    list2 = input_list()

    while True:
        print("\nMenu:")
        print("1. Check if lists are of the same length")
        print("2. Check if lists sum to the same value")
        print("3. Check if any value occurs in both lists")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            if check_length(list1, list2):
                print("The lists are of the same length.")
            else:
                print("The lists are of different lengths.")
        
        elif choice == "2":
            if check_sum(list1, list2):
                print("The lists sum to the same value.")
            else:
                print("The lists do not sum to the same value.")
        
        elif choice == "3":
            if check_common_values(list1, list2):
                print("There is at least one common value in both lists.")
            else:
                print("There are no common values in both lists.")
        
        elif choice == "4":
            print("Exiting program...")
            break
        
        else:
            print("Invalid choice! Please try again.")

# Run the menu-driven program
menu()
