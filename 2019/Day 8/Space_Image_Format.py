from typing import Tuple, List
import numpy as np


def get_depth(image, layer_shape):
    return len(image) / (layer_shape[0] * layer_shape[1])


def split(s):
    return [char for char in s]


def print_image(np_array, shape):
    counter = 0
    for _ in range(shape[0]):
        for _ in range(shape[1]):
            print(np_array[counter], end="")
            counter += 1
        print()


def decrypt_image(image: str, layer_shape: Tuple[int, int]):

    height = layer_shape[0]
    width = layer_shape[1]
    depth = int(get_depth(image, layer_shape))

    array = np.asarray(split(image), dtype=int)

    reshaped_array = array.reshape((depth, height * width))

    non_zero_array = np.count_nonzero(reshaped_array, axis=1)
    layer_idx = np.argmax(non_zero_array)

    # the number of 1 digits multiplied by the number of 2 digits?
    unique, counts = np.unique(reshaped_array[layer_idx], return_counts=True)

    number_of_one = dict(zip(unique, counts))[1]
    number_of_two = dict(zip(unique, counts))[2]

    return number_of_one * number_of_two


def decoding_image(image: str, layer_shape: Tuple[int, int]):
    response_image = []

    height = layer_shape[0]
    width = layer_shape[1]
    depth = int(get_depth(image, layer_shape))

    array = np.asarray(split(image), dtype=int)

    reshaped_array = array.reshape((depth, height, width))

    for i in range(layer_shape[0]):
        for j in range(layer_shape[1]):
            for k in range(depth):
                if reshaped_array[k, i, j] != 2:
                    response_image.append(reshaped_array[k, i, j])
                    break
    print_image(response_image, layer_shape)
    return response_image


if __name__ == "__main__":
    # PART 1
    test1 = "123456789012"
    shapet1 = (2, 3)
    assert decrypt_image(test1, shapet1) == 1
    # PART 2
    test2 = "0222112222120000"
    shape2 = (2, 2)
    assert decoding_image(test2, shape2) == [0, 1, 1, 0]

    SHAPE = (6, 25)  # puzzle shape
    with open("input.txt", "r") as puzzle_input:
        image_puzzle = puzzle_input.readline()
        print(decrypt_image(image_puzzle, SHAPE))

        rep = decoding_image(image_puzzle, SHAPE)
        # YEHEX
