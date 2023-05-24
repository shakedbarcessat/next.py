def read_file(file_name):
    try:
        f= open(file_name)
    except IOError:
        print("__CONTENT_START__\n__NO_SUCH_FILE__")
    else:
        print("__CONTENT_START__\n" + f.read())
    finally:
        print("__CONTENT_END__")


read_file(r'C:\Users\Shaked\Documents\alice.txt')
