import secrets

try:
    otp_length = int(input("Enter the lenght(4 or 6 digits only) of OTP you needed: "))
except(ValueError):
    print("Value error! Enter valid input.")

def otp_generator(otp_length):

    generated_otp = ""

    for i in range(otp_length):
        generated_otp += str(secrets.randbelow(10))
        
    otp_verification(generated_otp)

def otp_verification(generated_otp):

    incorrect_tries = 0

    while(incorrect_tries < 3):

        print(f"\nGenerated OTP: {generated_otp}")
        try:
            entered_otp = input("\nEnter OTP:     ")

            if(generated_otp == entered_otp):
                print("OTP verification successful.\n")
                break
            else:
                incorrect_tries += 1
                print(f"\nWrong OTP!\n{3-incorrect_tries} tries left!")
        except:
            incorrect_tries += 1
            print(f"\nPlease enter valid OTP!\n{3-incorrect_tries} tries left!")

    else:
        new_otp = input("Do you want to resend new OTP?(y/n): ").lower()
        if(new_otp == 'y'):
            otp_generator(otp_length)
            incorrect_tries = 0
        else:
            print("\nVerification is terminated!")

if(otp_length == 4 or otp_length == 6):
    otp_generator(otp_length)
else:
    print("Enter valid length for OTP!")