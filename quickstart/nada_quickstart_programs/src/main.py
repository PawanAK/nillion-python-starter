from nada_dsl import *

def nada_main():
    # Define parties
    user = Party(name="User")
    computer = Party(name="Computer")
    game_master = Party(name="GameMaster")

    # Get user's guess (1-5)
    user_guess = SecretInteger(Input(name="UserGuess", party=user))

    # Get secret seeds from each party (1-5)
    seed1 = SecretInteger(Input(name="Seed1", party=user))
    seed2 = SecretInteger(Input(name="Seed2", party=computer))
    seed3 = SecretInteger(Input(name="Seed3", party=game_master))

    # Combine seeds to create a pseudo-random number (3-15)
    combined_seed = seed1 + seed2 + seed3

    # Get current score from game master
    current_score = SecretInteger(Input(name="CurrentScore", party=game_master))

    # Calculate if numbers match
    # This will be 0 only when user_guess equals combined_seed
    match_check = (user_guess - seed1) * (user_guess - seed2) * (user_guess - seed3)

    # Calculate new score
    # If match_check is 0 (numbers match), new_score will be current_score
    # Otherwise, new_score will be current_score + 1
    new_score = current_score + (match_check * match_check)

    # Calculate game over flag (0 if game over, non-zero if not)
    game_over = match_check * match_check

    return [
        Output(combined_seed, "ComputerNumber", game_master),
        Output(new_score, "NewScore", game_master),
        Output(game_over, "GameOver", game_master)
    ]