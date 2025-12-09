import random
database = []

class BankApp:
    def __init__(self):
        pass
    def home(self):
        while True:
            print('''
            1. Register
            2. Login
            3. Deposit
            4. Withdraw
            5. Check Balance
            6. Exit
                ''')
            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.register()
            elif choice == 2:
                pass
            elif choice == 3:
                pass
            elif choice == 4:
                pass
            elif choice == 5:
                exit()
    def _generate_account(self):
        while True:
            acc = random.randint(1000000000, 9999999999)
            if not any(u["account_number"] == acc for u in database):
                return acc
    
    def register(self):
        print("\n=== REGISTER ACCOUNT ===\n")
        self.user1 = str(input("   Enter Your First Name: ")).strip()
        self.user2 = str(input("   Enter Your Surname: ")).strip()
        self.email = input("   Enter Your Email Address: ").strip().lower()
        self.phone = int(input("   Enter Your Phone Number: "))

        if not (self.user1 and self.user2 and self.email and self.phone):
            print("\n All fields are required. Registration cancelled")
            return
        if any(user["email"] == self.email for user in database):
            print("\n Email already registered. Try logging in.\n")
            return

        self.account_number = self._generate_account()
        self.balance = 0

        user_record = {
            "first_name": self.user1,
            "surname": self.user2,
            "email": self.email,
            "phone": self.phone,
            "account_number": self.account_number,
            "balance": self.balance
        }
        database.append(user_record)

        print("\n Registration Successful!")
        print(f"Welcome, {self.user2} {self.user1}!")
        print(f"Your Account Number: {self.account_number}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}\n")
        return user_record


app = BankApp()
app.home()