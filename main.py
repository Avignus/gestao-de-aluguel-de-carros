import os
execute = True


class Car:
    def __init__(self, name, price_per_day):
        self.name = name
        self.price_per_day = price_per_day
        self.rented = False


fiat_uno = Car("Fiat Uno", 120)
ford_ka = Car("Ford Ka", 90)
volkswagen_gol = Car("Volkswagen Gol", 150)
volkswagen_polo = Car("Volkswagen Polo", 85)
volkswagen_jetta = Car("Volkswagen Jetta", 120)
volkswagen_passat = Car("Volkswagen Passat", 130)


def show_cars(cars_available, renting=False):
    print("Carros disponíveis\n")
    for index, car in enumerate(cars_available):
        if (car.rented):
            print(
                f"{index + 1} {car.name} - R$ {car.price_per_day} / dia - ALUGADO\n")
        else:
            print(f"{index + 1} {car.name} - R$ {car.price_per_day} / dia\n")
    if (renting):
        car_selected = input(
            "Selecione o carro que deseja alugar ou pressione 0 para voltar ao menu inicial:\n")
        if (car_selected.isdigit()):
            if (car_selected == "0"):
                show_menu()
            elif (cars_available[int(car_selected) - 1].rented == True):
                os.system("cls")
                print("Carro indisponivel, selecione outro")
                show_cars(cars_available)
            else:
                days = input("\nQuantos dias de aluguel?\n")
                rent_value = int(days) * \
                    cars_available[int(car_selected) - 1].price_per_day
                print(f"\nValor total: R$ {rent_value}")
                choice = confirm_option("Deseja alugar o carro?")
                if (choice == True):
                    cars_available[int(car_selected) - 1].rented = True
                    input(
                        "\nCarro alugado com sucesso! Pressione qualquer tecla para voltar ao menu inicial!")

                if (choice == False):
                    os.system("cls")
                    show_cars(cars_available)

    else:
        choice = confirm_option("Voltar ao menu inicial?")
        if (choice == True):
            pass
        elif (choice == False):
            os.system("cls")
            show_cars(cars_available)


def choose_car_to_rent(cars_available):
    car_selected = input(
        "Selecione o carro que deseja alugar ou pressione 0 para voltar ao menu inicial:\n")
    if (car_selected.isdigit()):
        if (car_selected == "0"):
            show_menu()
        elif (cars_available[int(car_selected) - 1].rented == True):
            os.system("cls")
            print("Carro indisponivel, selecione outro")
            show_cars(cars_available)
        else:
            days = input("\nQuantos dias de aluguel?\n")
            rent_value = int(days) * \
                cars_available[int(car_selected) - 1].price_per_day
            print(f"\nValor total: R$ {rent_value}")
            choice = confirm_option("Deseja alugar o carro?")
            if (choice == True):
                cars_available[int(car_selected) - 1].rented = True
                input(
                    "\nCarro alugado com sucesso! Pressione qualquer tecla para voltar ao menu inicial!")

            if (choice == False):
                os.system("cls")
                show_cars(cars_available)
    else:
        print("Opção inválida, tente novamente")
        choose_car_to_rent(cars_available)


def show_portfolio(cars_available):

    print("Portfólio\n")
    show_cars(cars_available)
    confirm_option()
    if (choice == False):
        show_portfolio()
    else:
        os.system("cls")
        pass
    os.system("cls")


def show_menu():
    os.system("cls")
    print("1 - Ver portfólio\n2 - Alugar carro\n3 - Devolver carro\n")
    choice = input("Selecione uma opção:\n")
    if (choice == "1" or choice == "2" or choice == "3"):
        return choice
    else:
        os.system("cls")
        print("Opção inválida, tente novamente")
        show_menu()


def confirm_option(message):
    choice = input(f"\n{message} \n 1 - SIM | 2 - NÃO\n")
    if (choice.isdigit()):
        if (choice == "1"):
            return True
        elif (choice == "2"):
            return False
    else:
        print("Opção inválida, tente novamente")
        confirm_option(message)


def show_cars_rented(cars_available):
    print("Carros alugados por você:\n")
    cars_rented = 0
    for index, car in enumerate(cars_available):
        if (car.rented == True):
            print(f"{index + 1} {car.name}")
            cars_rented += 1
    if (cars_rented > 0):
        car_selected = input(
            "Selecione o carro que deseja devolver ou pressione 0 para retornar ao menu inicial.\n")
        if (car_selected == 0):
            os.system("cls")
            pass
        else:
            choice = confirm_option("Deseja realmente devolver o carro?")
            if (choice == True):
                os.system("cls")
                cars_available[int(car_selected) - 1].rented = False
                print("Carro devolvido com sucesso!")
            elif (choice == False):
                show_cars_rented(cars_available)
    else:
        print("Você não possui carros alugados.")
        choice = confirm_option(
            "Deseja alugar um carro?")
        if (choice == True):
            show_cars(cars_available, True)
        elif (choice == False):
            show_menu()


while (execute):
    os.system("cls")
    print("Bem vindo à locadora de carros!")
    cars_available = [fiat_uno, ford_ka, volkswagen_gol,
                      volkswagen_polo, volkswagen_jetta, volkswagen_passat]
    choice = show_menu()
    if (choice == "1"):
        show_cars(cars_available, False)
    if (choice == "2"):
        show_cars(cars_available, True)
    if (choice == "3"):
        show_cars_rented(cars_available)
