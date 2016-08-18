
import uuid


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


def print_menu(handler_fn, screen, row_start, cid=None):
    """ Prints a menu from an object list
        Method arguments
        ================
        handler_fn - function reference that will return the list to print and
                     a price boolean that determines whether to print the item
                     as a product with a price
        screen - the instance of screen on Meow
        row_start - the row you would like to start adding strings
        cid - optional customerID argument
    """
    if cid is not None:
        temp_list, price = handler_fn(cid)
    else:
        temp_list, price = handler_fn()

    if price:
        for item in temp_list:
            screen.addstr(row_start, 40, '{0}. {1}-- ${2}'.format((temp_list.index(item) + 1), item[1], item[2]))
            row_start += 1
    else:
        for item in temp_list:
            screen.addstr(row_start, 40, '{0}. {1}'.format((temp_list.index(item) + 1), item[1]))
            row_start += 1

    return temp_list


def set_thing(temp_list, index):
    """ Returns the UID of the selected item in a temp list
        Method arguments
        ================
        temp_list - the temporary list created in print_menu
        index - the users choice from print_menu
    """
    try:
        return temp_list[(index - 1)][0]
    except:
        return None
