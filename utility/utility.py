import pickle
import uuid

def deserialize(self, input_file):
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
        return None


def serialize(self, output_file, updated_info):
    """ Writes binary data to the file passed in
        Method arguments
        ================
        updated_info - the complete library to be changed
        output_file - the file to write to
    """
    with open(output_file, 'wb+') as file:
        pickle.dump(updated_info, file)


def get_value(self, read_file, uid):
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
            print('There was an error getting the value you were looking for.')


def add_to_file(self, write_file, write_value):
    """ Adds the provided value to the provided file
        Method arguments
        ================
        write_file - the file to write to
        write_value - the new value to be written
    """
    to_write = deserialize(write_file)
    to_write[str(uuid.uuid4())] = write_value
    serialize(to_write)
