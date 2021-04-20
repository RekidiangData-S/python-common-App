import streamlit as st
from PIL import Image
from tip_calculator import tip_calculator


def main():

    image = Image.open('images/data_logo_resized.png')
    st.image(image, use_column_width=True)

    menu = ["Tip Calculator", "BMI", "Life Calendar",
            "Odd or Even", "Love Calculator", "Leap Year", "Treasure Island", "Banker Roulette", "Rock-Paper-Scisors", "Password Generator", "Hangman", "About"]
    choice = st.sidebar.selectbox('Selection Application', menu)
    ##"Tip Calculator"#################################################################################################
    if choice == "Tip Calculator":
        tip_calculator()

    if choice == "Life Calendar":
        # https://waitbutwhy.com/2014/05/life-weeks.html
        st.header('Life Calendar')
        st.markdown("""Supose you have 90 years to live according to your actual age
        how many days, weeks, months, years left ?""")
        st.subheader("Let check !!!")
        age = st.slider(
            "Select your age ?", 1, 90, 10)
        years = 90-int(age)
        month = years * 12
        weeks = years * 52
        days = years * 365
        st.write(age, "years old is your current age")
        st.write(
            "you have", days, "days", weeks, "Weeks", month, "Months", years, "Years  left")
        st.success("Life is very short be WISE")
        if st.checkbox("Learn more"):
            st.text("https://waitbutwhy.com/2014/05/life-weeks.html")

    ##"Odd or Even"#####################################################################################
    if choice == "Odd or Even":
        st.header('Odd or Even')
        num = st.number_input("Enter any Number")

        if st.button("Odd or Even"):
            if num % 2 == 0:
                st.write(num, " is a Even number")
            else:
                st.write(num, " is a Odd number")

    ##"Love Calculator"##################################################################################
    if choice == "Love Calculator":
        st.header("Love Calculator")
        image = Image.open('images/love_cal.jpg')
        st.image(image, use_column_width=True)
        print("Welcome to the Love Calculator!")

        name1 = st.text_input("What is your name? \n")
        name2 = st.text_input("What is their name? \n")
        # 🚨 Don't change the code above 👆
        name1 = name1.lower()
        name2 = name2.lower()
        two_names = name1 + name2
        true = str(two_names.count("t")+two_names.count("r") +
                   two_names.count("u")+two_names.count("e"))
        love = str(two_names.count("l")+two_names.count("0") +
                   two_names.count("v")+two_names.count("e"))
        score = int(true + love)
        if st.button("Calculate"):
            if score < 10 or score > 90:
                st.success(
                    f"Your score is {score}, you go together like coke and mentos")
            elif score >= 40 and score <= 50:
                st.success(f"Your score is {score}, you are alright together")
            else:
                st.warning(f"Your score is {score}.")
    ##"Leap Year"########################################################################################
    if choice == "Leap Year":
        from datetime import datetime
        today = datetime.today()
        datem = datetime(today.year, today.month, today.day)

        currentSecond = datetime.now().second
        currentMinute = datetime.now().minute
        currentHour = datetime.now().hour

        currentDay = datetime.now().day
        currentMonth = datetime.now().month
        currentYear = datetime.now().year

        "Leap Year"
        st.header("Leap Year")
        st.write("Date & Time : ", currentDay, "-", currentMonth, "-",
                 currentYear, "<>", currentHour, ":", currentMinute, ":", currentSecond)
        image = Image.open('images/leap_y.jpg')
        st.image(image, use_column_width=True)

        year = st.number_input("Which year do you want to check ? ")
        year = int(year)

        if st.button("Check"):
            if year % 4 == 0:
                if year % 100 == 0:
                    if year % 400 == 0:
                        if year == currentYear:
                            st.success(f"{year} Is a leap year")
                        elif year < currentYear:
                            st.success(f"{year} Was a leap year")
                        else:
                            st.success(f"{year} Will be a leap year")

                    else:
                        if year == currentYear:
                            st.success(f"{year} Is not a leap year")
                        elif year < currentYear:
                            st.success(f"{year} Was not a leap year")
                        else:
                            st.success(f"{year} Will not be a leap year")
                else:
                    if year == currentYear:
                        st.success(f"{year} Is a leap year")
                    elif year < currentYear:
                        st.success(f"{year} Was a leap year")
                    else:
                        st.success(f"{year} Will be a leap year")
            else:
                if year == currentYear:
                    st.success(f"{year} Is not a leap year")
                elif year < currentYear:
                    st.success(f"{year} Was not a leap year")
                else:
                    st.success(f"{year} Will not be a leap year")
    ##"Treasure Island"##################################################################################
    if choice == "Treasure Island":
        st.header("Treasure Island")
        image = Image.open('images/treasure.jfif')
        st.image(image, use_column_width=True)

        st.markdown("# Your mission is to find the treasure.")

        direction = st.radio(
            "You're at across road. Choose the direction", ("left", "right"))
        direction.lower()
        if direction == "left":
            st.subheader(
                "You're to a lake. There is an island in the middle of the lake")
            whattodo = st.radio(
                "Type 'Wait' to wait for a boat or type 'Swim' to swim across : ", ("wait", "swim"))
            whattodo.lower()
            if whattodo == "wait":
                st.subheader(
                    "You arrive at the island unharmed. There is a house with 3 doors")
                which_door = st.radio(
                    "One red, one yellow, one blue. Which colour do you choose :  ", ("blue", "yellow", "red"))

                which_door.lower()
                if which_door == "red":
                    st.error("Barned by fire GAMEOVER")
                elif which_door == "blue":
                    st.error("Eaten by beast GAME OVER")
                elif which_door == "yellow":
                    st.success("YOU WIN !!!!")
                else:
                    st.error("GAME OVER")
            else:
                st.error("Attacked by trout GAME OVER")
        else:
            st.error("Fall into a hole GAME OVER")
    ##"Banker Roulette"##################################################################################
    if choice == "Banker Roulette":
        st.header("Banker Roulette")
        image = Image.open('images/diner.jpg')
        st.image(image, use_column_width=True)
        # Split string method
        import time
        names_string = st.text_input(
            "Type everybody's names, separated by a comma. ")
        st.text(
            "NB: notice that there is a space between the comma and the next name. ")
        names = names_string.split(", ")
        if st.checkbox("We are "):
            st.write(names)
        if st.button("Who will pay the bill today ? "):

            progress_bar = st.progress(0)
            for percent_complete in range(100):
                time.sleep(0.1)
                progress_bar.progress(percent_complete+1)

            with st.spinner('wait a moment ....'):
                time.sleep(5)
            # 🚨 Don't change the code above 👆

            # Write your code below this line 👇
            import random
            rando = random.randint(0, len(names))
            name = str(names[rando]).upper()
            st.success(f"{name} is going to buy the meal today")
            st.balloons()
        ############################"Banker Roulette"##############################################
    ##"Rock-Paper-Scisors"##############################################################################
    if choice == "Rock-Paper-Scisors":
        st.header("Rock-Paper-Scisors")
        image = Image.open('images/rock_paper_scisor.jpg')
        st.image(image, use_column_width=True)

        import random

        select = st.radio("Select either Rock or Paper or Scisors",
                          ("Rock", "Paper", "Scisors"))
        machine = ["Rock", "Paper", "Scisors"]
        rando = random.randint(0, len(machine)+1)

        if st.button("Play"):

            if select == "Rock":
                if machine[rando] == "Rock":
                    st.warning("It's a draw")

                    st.write("You play : Rock")
                    rock = Image.open('images/h_rock.jpg')
                    st.image(rock, use_column_width=True)

                    st.write("Machine play : Rock")
                    rock = Image.open('images/m_rock.jpg')
                    st.image(rock, use_column_width=True)
                    st.warning("It's a draw")

            if select == "Rock":
                if machine[rando] == "Paper":
                    st.error("machine WIN")

                    st.write("You play : Rock")
                    rock = Image.open('images/h_rock.jpg')
                    st.image(rock, use_column_width=True)

                    st.write("Machine play : Paper")
                    paper = Image.open('images/m_paper.jpg')
                    st.image(paper, use_column_width=True)

                    st.error("machine WIN")

            if select == "Rock":
                if machine[rando] == "Scisors":
                    st.success("You WIN")
                    st.write("You play : Rock")
                    rock = Image.open('images/h_rock.jpg')
                    st.image(rock, use_column_width=True)

                    st.write("Machine play : Scisors")
                    scisor = Image.open('images/m_scisor.jpg')
                    st.image(scisor, use_column_width=True)
                    st.success("You WIN")
                    st.balloons()

            if select == "Paper":
                if machine[rando] == "Rock":
                    st.success("You WIN")

                    st.write("You play : Paper")
                    rock = Image.open('images/h_paper.jpg')
                    st.image(rock, use_column_width=True)

                    st.write("Machine play : Rock")
                    rock = Image.open('images/m_rock.jpg')
                    st.image(rock, use_column_width=True)
                    st.success("You WIN")
                    st.balloons()

            if select == "Paper":
                if machine[rando] == "Paper":
                    st.warning("It's a draw")

                    st.write("You play : Paper")
                    rock = Image.open('images/h_paper.jpg')
                    st.image(rock, use_column_width=True)

                    st.write("Machine play : Paper")
                    paper = Image.open('images/m_paper.jpg')
                    st.image(paper, use_column_width=True)

                    st.warning("It's a draw")

            if select == "Paper":
                if machine[rando] == "Scisors":
                    st.error("Machine WIN")

                    st.write("You play : Paper")
                    rock = Image.open('images/h_paper.jpg')
                    st.image(rock, use_column_width=True)

                    st.write("Machine play : Scisors")
                    scisor = Image.open('images/m_scisor.jpg')
                    st.image(scisor, use_column_width=True)
                    st.error("Machine WIN")

            ###################################
            if select == "Scisors":
                if machine[rando] == "Rock":
                    st.error("Machine WIN")

                    st.write("You play : Scisors")
                    rock = Image.open('images/h_scisor.jpg')
                    st.image(rock, use_column_width=True)

                    st.write("Machine play : Rock")
                    rock = Image.open('images/m_rock.jpg')
                    st.image(rock, use_column_width=True)
                    st.error("Machine WIN")

            if select == "Scisors":
                if machine[rando] == "Paper":
                    st.success("You WIN")
                    st.write("You play : Scisors")
                    rock = Image.open('images/h_scisor.jpg')
                    st.image(rock, use_column_width=True)

                    st.write("Machine play : Paper")
                    paper = Image.open('images/m_paper.jpg')
                    st.image(paper, use_column_width=True)

                    st.success("You WIN")
                    st.balloons()

            if select == "Scisors":
                if machine[rando] == "Scisors":
                    st.warning("It's a draw")

                    st.write("You play : Scisors")
                    rock = Image.open('images/h_scisor.jpg')
                    st.image(rock, use_column_width=True)

                    st.write("Machine play : Scisors")
                    scisor = Image.open('images/m_scisor.jpg')
                    st.image(scisor, use_column_width=True)
                    st.warning("It's a draw")

    st.markdown("""--------------------------------""")
    image = Image.open('images/my_ethiquette.png')
    st.image(image, use_column_width=True)


if __name__ == "__main__":
    main()
