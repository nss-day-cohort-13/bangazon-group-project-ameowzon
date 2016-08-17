import pickle
import uuid
import json


def read_json_file(input_file):
    """ Reads non-binary data from the file passed in as a
        json and returns the file as a parsed dictionary.
    """
    try:
        with open(input_file, 'r+') as file:
            return json.load(file)
    except EOFError:
        print('{0} is empty.'.format(input_file))
        return None


def get_param(prompt_string, screen):
    """ Helper function for working with curses. Clears screen, sets border to 0
        creates a popup that displays the text of the prompt string passed in and
        captures and returns the input to the calling function. Returns a string.
        ==============
        prompt_string - text the user wants displayed on the screen.
    """
    screen.clear()
    screen.border(0)
    screen.addstr(12, 40, prompt_string)
    screen.refresh()
    input = bytes.decode(screen.getstr(15, 40, 60))

    # self.screen.addstr(17, 40, "input = {0}".format(input))
    # pause = self.screen.getch()
    return input


def generate_uid():
    """ Returns a uuid to be used for a dictionary key.
        ===============
    """
    uid = str(uuid.uuid4())
    return uid


def write_json_file(data, output_file):
    """ Writes the product dictionary to json file.
        ===============
        data = dictionary
        output_file = the place to save the file.
    """
    try:
        with open(output_file, 'w+') as file:
            json.dump(data, file)
            return
    except EOFError:
        print('{0} is empty.'.format(input_file))
        return None


def deserialize(input_file):
    """ Reads binary data from the file passed in
        Method arguments
        ================
        input_file - the file to read from
    """
    try:
        with open(input_file, 'rb+') as file:
            return pickle.load(file)
    except EOFError:
        print('{0} is empty.'.format(input_file))
        return {}
    except FileNotFoundError:
        return {}


def serialize(output_file, updated_info):
    """ Writes binary data to the file passed in
        Method arguments
        ================
        updated_info - the complete library to be changed
        output_file - the file to write to
    """
    with open(output_file, 'wb+') as file:
        pickle.dump(updated_info, file)


def get_value(read_file, uid):
    """ Returns an object from read_file that matches
        the uid provided as argument
        Method arguments
        ================
        read_file - the file to read from
        uid - the uid to match
    """
    to_search = deserialize(read_file)
    try:
        return to_search[uid]
    except KeyError:
        return None


def add_to_file(write_file, write_value):
    """ Adds the provided value to the provided file
        Method arguments
        ================
        write_file - the file to write to
        write_value - the new value to be written
    """
    to_write = deserialize(write_file)
    uid = str(uuid.uuid4())
    to_write[uid] = write_value
    # print("to_write[uid] = {0}".format(to_write[uid]))
    serialize(write_file, to_write)
    return uid

def print_menu(handler_fn, screen):
    """ Prints a menu from an object list
        Method arguments
        ================
        handler_fn - function reference that will return the list to print and
                     a price boolean that determines whether to print the item
                     as a product with a price
        screen - the instance of screen on Meow
    """
    temp_list, price = handler_fn()
    row = 3

    if price:
        for item in temp_list:
            screen.addstr(row, 40, '{0}. {1}-- ${2}'.format(temp_list.index(item), temp_list[1], temp_list[2]))
            row += 1
    else:
        for item in temp_list:
            screen.addstr(row, 40, '{0}. {1}'.format(temp_list.index(item), temp_list[1]))
            row += 1

    return temp_list

def set_thing(temp_list, index):
    """ Returns the UID of the selected item in a temp list
        Method arguments
        ================
        temp_list - the temporary list created in print_menu
        index - the users choice from print_menu
    """
    return temp_list[index][0]
