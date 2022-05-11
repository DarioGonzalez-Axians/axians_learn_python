# @Author            : Dario Gonzalez
# @Date              : 2022-05-11
# @Last Modified by  : Dario Gonzalez
# @Last Modified time: 2022-05-11

import mock

from main import main


def test_quitting():

    with mock.patch('builtins.input', return_value="rock"):
        result = main()
        assert result == "Rock smashes scissors! You win!" or \
            result == "Paper covers rock! You lose." or \
            result == "Both players selected rock. It's a tie!"

    with mock.patch('builtins.input', return_value="paper"):
        result = main()
        assert result == "Paper covers rock! You win!" or \
            result == "Scissors cuts paper! You lose." or \
            result == "Both players selected paper. It's a tie!"

    with mock.patch('builtins.input', return_value="scissors"):
        result = main()
        assert result == "Scissors cuts paper! You win!" or \
            result == "Rock smashes scissors! You lose." or \
            result == "Both players selected scissors. It's a tie!"


if __name__ == "__main__":
    test_quitting()
