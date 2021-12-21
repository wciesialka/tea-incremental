import pickle
import argparse
import pathlib
import os
import logging
import pygame
from typing import Optional, BinaryIO
from time import sleep, time
from tea_incremental.game.tea_game import StopGame, TeaGame
from tea_incremental.interface.screen import Screen

SAVE_PATH: pathlib.Path = pathlib.Path(os.path.expanduser("~/Documents")) / "My Games" / "Tea Incremental" / "save.tea"

def parse_args():
    '''Parse args and return the namespace.

    :returns: Parsed args.
    :rtype: argparse.Namespace'''
    argparser = argparse.ArgumentParser("tea", description="Incremental game about tea!")
    argparser.add_argument("--load", "-l", type=argparse.FileType("rb"), help="Save file.")
    return argparser.parse_args()

def load_game(load_from: Optional[BinaryIO] = None):
    '''Load game from file. If file does note exist, create a new game.

    :param load_from: Binary file to load from.
    :type load_from: optional(binaryIO)
    :returns: A TeaGame instance.
    :rtype: TeaGame'''
    game = None
    if not load_from is None:
        try:
           game = pickle.load(load_from)
        except:
            print(f"Could not load file {load_from.name}!")
        finally:
            load_from.close()
    # If we could not successfully load the game, or if there was just
    # nothing there, we need to try to load the game from the default
    # save file. If there isn't anything there, either, we need to create
    # a new game.
    if game is None:
        if(SAVE_PATH.exists() and SAVE_PATH.is_file()):
            with open(SAVE_PATH,"rb") as f:
                game = pickle.load(f)
        else:
            game = TeaGame()
    return game

def save_game(game: TeaGame, save_to: str):
    '''Save game to file.

    :param game: Game to save.
    :type game: TeaGame
    :param save_to: Save path.
    :type save_to: str'''
    path_parent = os.path.dirname(save_to)
    os.makedirs(path_parent, exist_ok=True)
    with open(save_to, "wb") as f:
        pickle.dump(game, f)

def main():
    '''Main functionality.'''

    logging.basicConfig(level=logging.DEBUG)
    args = parse_args()

    game = load_game(args.load)
    screen = Screen(game)

    # Make sure we start on a solid second
    if (catchup := round(time() % 1, 2)) != 0:
        sleep(catchup)

    try:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game.end()
            game.game_loop()
            screen.draw()

    except Exception as ex:
        if not isinstance(ex, StopGame):
            raise ex
            logging.debug("Error: %s", ex)
            print("An error occured and we had to quit!")
    finally:
        screen.dispose()
        save_game(game, SAVE_PATH if args.load is None else args.load.name)
        print("Your game has been saved.")


if __name__ == "__main__":
    main()
