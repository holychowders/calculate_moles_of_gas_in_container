#!/usr/bin/env/ python
import sys
import argparse


# Gas constant units: (L * Pa) / K * mol
GAS_CONSTANT = 8_314


def main(pressure_pascals, volume_litres, temperature_kelvin):
    result = calculate(pressure_pascals, volume_litres, temperature_kelvin)
    result_formatted = float(str.format("{:.8f}", result))

    return result_formatted


def calculate(pressure_pascals, volume_litres, temperature_kelvin):
    moles_of_gas = (
        (pressure_pascals * volume_litres) /
        (GAS_CONSTANT * temperature_kelvin))

    return moles_of_gas


def determine_input_strategy():
    if is_at_least_one_cli_argument():
        return InputsFromCommandLine
    else:
        return InputsFromPrompt


def is_at_least_one_cli_argument():
    # The first arg (sys.argv[0]) is technically the program name,
    # so we actually check for at least two args.
    return len(sys.argv) > 1


class InputsFromCommandLine:

    def __init__(self):
        cli_parser = self.__setup_parser()
        variables = self.__get_arguments_from_parser(cli_parser)

        self.pressure_pascals = variables.pressure_pascals
        self.volume_litres = variables.volume_litres
        self.temperature_kelvin = variables.temperature_kelvin


    def get_pressure_pascals(self):
        return self.pressure_pascals

    def get_volume_litres(self):
        return self.volume_litres

    def get_temperature_kelvin(self):
        return self.temperature_kelvin


    @staticmethod
    def __setup_parser():
        cli_parser = argparse.ArgumentParser()

        cli_parser.add_argument(
            '-p', '--pressure', help="Pressure of gas in Pascals",
            type=float, dest="pressure_pascals", required=True)

        cli_parser.add_argument(
            '-v', '--volume', help="Volume of container in litres",
            type=float, dest="volume_litres", required=True)

        cli_parser.add_argument(
            '-t', '--temperature', help="Temperature of gas in Kelvin",
            type=float, dest="temperature_kelvin", required=True)

        return cli_parser


    @staticmethod
    def __get_arguments_from_parser(cli_parser):
        return cli_parser.parse_args()


class InputsFromPrompt:

    def __init__(self):
        self.pressure_pascals = self.__get_pressure_pascals()
        self.volume_litres = self.__get_volume_litres()
        self.temperature_kelvin = self.__get_temperature_kelvin()


    def get_pressure_pascals(self):
        return self.pressure_pascals

    def get_volume_litres(self):
        return self.volume_litres

    def get_temperature_kelvin(self):
        return self.temperature_kelvin


    def __get_pressure_pascals(self):
        try: return float(input("Pressure (Pascals): "))
        except ValueError: return self.__get_pressure_pascals()

    def __get_volume_litres(self):
        try: return float(input("Volume (litres): "))
        except ValueError: return self.__get_volume_litres()

    def __get_temperature_kelvin(self):
        try: return float(input("Temperature (Kelvin): "))
        except ValueError: return self.__get_temperature_kelvin()


is_program_running_standalone = (__name__ == "__main__")
if is_program_running_standalone:

    get_inputs = determine_input_strategy()
    inputs = get_inputs()

    pressure_pascals = inputs.get_pressure_pascals()
    volume_litres = inputs.get_volume_litres()
    temperature_kelvin = inputs.get_temperature_kelvin()

    result = main(pressure_pascals, volume_litres, temperature_kelvin)
    print(result)
