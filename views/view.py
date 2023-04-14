from models.tournament import Tournament
import datetime

ERR_NOT_NUMERIC_VALUE = "please fill this field in digits"

class View:
    def __init__(self):
        return

    @staticmethod
    def input_main_menu():
        digit_menu_selection = ""
        print("\n \n --- Chess Manager --- \n\n")
        print("(1) Register a player in the database")
        print("(2) Create a new tournament (turns and players management in progress ...) ")
        print("(3) Exit the application \n")
        try:
            digit_menu_selection = int(
                input("please insert the digit corresponding to the action you want to make: \n"))
        except ValueError:
            print("please enter a digit value")
        return int(digit_menu_selection)

    @staticmethod
    def input_tournament_name():
        tournament_name = input("enter the name of the tournament: \n")
        return tournament_name

    @staticmethod
    def input_tournament_place():
        tournament_place = input("enter the place of the tournament: \n")
        return tournament_place

    @staticmethod
    def input_tournament_start_day():
        start_day = None
        while start_day is None:
            try:
                start_day = int(input("please enter the day the tournament will start (in digits): \n"))
                return start_day
            except ValueError:
                print(ERR_NOT_NUMERIC_VALUE)

    @staticmethod
    def input_tournament_start_month():
        start_month = None
        while start_month is None:
            try:
                start_month = int(input("please enter the month the tournament will start (in digits): \n"))
                return start_month
            except ValueError:
                print(ERR_NOT_NUMERIC_VALUE)

    @staticmethod
    def input_tournament_start_year():
        start_year = None
        while start_year is None:
            try:
                start_year = int(input("please enter the year the tournament will start (in digits): \n"))
                return start_year
            except ValueError:
                print(ERR_NOT_NUMERIC_VALUE)

    @staticmethod
    def input_tournament_end_day():
        end_day = None
        while end_day is None:
            try:
                end_day = int(input("please enter the day the tournament will end (in digits): \n"))
                return end_day
            except ValueError:
                print(ERR_NOT_NUMERIC_VALUE)

    @staticmethod
    def input_tournament_end_month():
        end_month = None
        while end_month is None:
            try:
                end_month = int(input("please enter the month the tournament will end (in digits): \n"))
                return end_month
            except ValueError:
                print(ERR_NOT_NUMERIC_VALUE)

    @staticmethod
    def input_tournament_end_year():
        end_year = None
        while end_year is None:
            try:
                end_year = int(input("please enter the year the tournament will end (in digits): \n"))
                return end_year
            except ValueError:
                print(ERR_NOT_NUMERIC_VALUE)

    @staticmethod
    def input_tournament_start_date():
        start_day = View.input_tournament_start_day()
        start_month = View.input_tournament_start_month()
        start_year = View.input_tournament_start_year()
        start_date = datetime.date(start_year, start_month, start_day)
        return start_date

    @staticmethod
    def input_tournament_end_date():
        end_day = View.input_tournament_end_day()
        end_month = View.input_tournament_end_month()
        end_year = View.input_tournament_end_year()
        end_date = datetime.date(end_year, end_month, end_day)
        return end_date

    @staticmethod
    def input_tournament_description():
        tournament_description = input("please enter the description of the tournament: \n")
        return tournament_description

    @staticmethod
    def input_tournament_register_player():
        player_to_register_id = input(
            "please enter the national chess ID of the player you want to register for the tournament: \n"
        )
        return player_to_register_id

    @staticmethod
    def input_tournament_number_of_turns():
        number_of_turns = None
        while number_of_turns is None:
            try:
                number_of_turns = int(input("how much turns this tournament will count ? (in digits) \n"))
                return number_of_turns
            except ValueError:
                print(ERR_NOT_NUMERIC_VALUE)

    @staticmethod
    def input_tournament_number_of_players():
        number_of_players = None
        while number_of_players is None:
            try:
                number_of_players = int(
                    input("please enter how much players will participate to the tournament(in digits) \n"))
                return number_of_players
            except ValueError:
                print(ERR_NOT_NUMERIC_VALUE)

    @staticmethod
    def input_player_chess_id():
        national_chess_id = input("please enter the national chess ID of the player you want to register: \n")
        return national_chess_id

    @staticmethod
    def input_player_first_name():
        player_first_name = input("please enter the first name of the player you want to register: \n")
        return player_first_name

    @staticmethod
    def input_player_last_name():
        player_last_name = input("plase enter the last name of the player you want to register: \n")
        return player_last_name

    @staticmethod
    def input_player_birth_date():
        birth_day, birth_month, birth_year = 0, 0, 0
        try:
            birth_day = int(input("please enter the birth's day of the player (in digits): \n"))
            birth_month = int(input("please enter the birth's month of the player (in digits): \n"))
            birth_year = int(input("please enter the birth's year of the player (in digits): \n"))
        except ValueError:
            print("you must enter the date in digits please")
        birth_date = datetime.date(birth_year, birth_month, birth_day)
        return birth_date


